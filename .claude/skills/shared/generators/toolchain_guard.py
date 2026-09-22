#!/usr/bin/env python3
"""Hold the checking scripts back from the runs they check.

Landed 10 September 2026 on Tom's ruling, from escalation 5 of
`Forge/WS1/scorer-tiers-applied-to-ive-2026-09-10.md`.

THE PROBLEM. The scripts that decide whether a model is valid live in files the
run being checked can edit. A run under pressure to pass a gate has a cheaper
route than designing well. The studio already had one instance: a second copy of
the toolchain that ran a live model silently and would have passed a model the
canonical copy refuses.

THE DEFENCE, IN THREE LAYERS, AND NONE OF THEM IS SUFFICIENT ALONE.

 1. An integrity manifest of SHA-256 digests, held OUTSIDE the directory it
    protects, in the method's own register area. Every shared script verifies
    itself and its siblings before it does anything, and refuses on a mismatch.
    This is the studio's own held-back-answer defence, applied to the toolchain.
 2. Read-only file permissions. An ordinary edit fails. A deliberate edit needs
    an explicit unlock first, which is a separate and visible act.
 3. The origin check refuses rather than warns, from every shared script,
    whether or not it writes a document.

THE LIMIT, STATED PLAINLY. A process that can write files can also unlock them
and rewrite the manifest. This raises the cost of tampering and makes it
visible. It does not make it impossible. The only mechanism that forbids it is
a permission rule in the harness, outside these files, and that is the
principal's to set.

Usage:
    python3 toolchain_guard.py verify    # check every script against the manifest
    python3 toolchain_guard.py seal      # rewrite the manifest, then lock
    python3 toolchain_guard.py unlock    # make the scripts writable for a rule change
    python3 toolchain_guard.py lock      # make them read-only again (no re-seal)
"""
import hashlib
import os
import stat
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST_REL = os.path.join(
    "04-Projects", "TMTH_Venture_Studio", "Forge", "WS1", "toolchain-manifest.txt")


class GuardRefusal(Exception):
    pass


def vault_root(start=HERE):
    """Walk up to the directory holding both .claude and 04-Projects."""
    p = start
    while True:
        if (os.path.isdir(os.path.join(p, ".claude"))
                and os.path.isdir(os.path.join(p, "04-Projects"))):
            return p
        parent = os.path.dirname(p)
        if parent == p:
            return None
        p = parent


def manifest_path():
    root = vault_root()
    if root is None:
        raise GuardRefusal(
            "the vault root is not locatable from %s, so the integrity manifest "
            "cannot be found. A toolchain that cannot verify itself does not run." % HERE)
    return os.path.join(root, MANIFEST_REL)


def scripts():
    return sorted(f for f in os.listdir(HERE)
                  if f.endswith(".py") and os.path.isfile(os.path.join(HERE, f)))


def digest(name):
    h = hashlib.sha256()
    with open(os.path.join(HERE, name), "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def read_manifest():
    path = manifest_path()
    if not os.path.exists(path):
        raise GuardRefusal(
            "no integrity manifest at %s. Run `python3 toolchain_guard.py seal` "
            "to create one. Until then no script can prove it is the canonical "
            "copy." % path)
    out = {}
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        if len(parts) == 2:
            out[parts[1].strip()] = parts[0].strip()
    return out


def verify(quiet=True):
    """Raise GuardRefusal on any mismatch. Return the number of files checked."""
    recorded = read_manifest()
    present = scripts()
    problems = []
    for name in present:
        if name not in recorded:
            problems.append("%s is present and not in the manifest — an unlisted "
                            "script in the toolchain directory" % name)
        elif digest(name) != recorded[name]:
            problems.append("%s does not match its recorded digest — it has been "
                            "edited since the last seal" % name)
    for name in recorded:
        if name not in present:
            problems.append("%s is in the manifest and missing from disk" % name)
    if problems:
        raise GuardRefusal(
            "the toolchain does not match its manifest:\n    - "
            + "\n    - ".join(problems)
            + "\n  If the change was intended, run `python3 toolchain_guard.py seal` "
              "and say in the session record what changed and why.")
    if not quiet:
        print("Toolchain integrity: %d script(s) checked against %s"
              % (len(present), manifest_path()))
        print("  VERDICT: PASS — every digest matches")
    return len(present)


def seal():
    lines = ["# Toolchain integrity manifest.",
             "# SHA-256 of every script in .claude/skills/shared/generators/.",
             "# Held here, outside the directory it protects, so a forked copy of the",
             "# toolchain cannot carry its own manifest and pass its own check.",
             "# Re-seal only after a deliberate rule change, and record what changed.",
             ""]
    names = scripts()
    for name in names:
        lines.append("%s  %s" % (digest(name), name))
    path = manifest_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("Sealed %d script(s) into %s" % (len(names), path))
    lock()


def set_writable(writable):
    changed = 0
    for name in scripts():
        p = os.path.join(HERE, name)
        mode = os.stat(p).st_mode
        if writable:
            new = mode | stat.S_IWUSR
        else:
            new = mode & ~(stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)
        if new != mode:
            os.chmod(p, new)
            changed += 1
    return changed


def lock():
    n = set_writable(False)
    print("Locked: %d script(s) made read-only (%d already were)"
          % (n, len(scripts()) - n))


def unlock():
    n = set_writable(True)
    print("Unlocked: %d script(s) made writable." % n)
    print("A rule change is now possible. When it is done, run:")
    print("    python3 toolchain_guard.py seal")
    print("An unlocked toolchain that is never re-sealed will refuse every run.")


def require_canonical(model_path=None):
    """Called at the top of every shared script. Refuses rather than warns.

    Closes R-CTM8: the model checker writes no document, so a forked copy used
    to announce nothing at all.
    """
    canon = None
    if model_path:
        p = os.path.abspath(model_path)
        while True:
            cand = os.path.join(p, ".claude", "skills", "shared", "generators")
            if os.path.isdir(cand):
                canon = os.path.realpath(cand)
                break
            parent = os.path.dirname(p)
            if parent == p:
                break
            p = parent
    if canon and os.path.realpath(HERE) != canon:
        raise GuardRefusal(
            "this script is running from %s, which is not the canonical toolchain "
            "at %s. A forked copy may be behind the canon and may pass a model the "
            "canonical checker refuses. Run the canonical copy." % (HERE, canon))
    verify()


def main(argv):
    if not argv or argv[0] not in ("verify", "seal", "lock", "unlock"):
        print(__doc__)
        return 2
    try:
        if argv[0] == "verify":
            verify(quiet=False)
        elif argv[0] == "seal":
            seal()
        elif argv[0] == "lock":
            lock()
        elif argv[0] == "unlock":
            unlock()
    except GuardRefusal as exc:
        print("REFUSED: %s" % exc)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
