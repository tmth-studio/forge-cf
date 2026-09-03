# Components Map — Generation Standard

The **primary operational-model deliverable** is the Components Map: a numbered
component register, not a spatial box picture. Reference implementation:
Calmly "Component / Activity / Owner / Journey Map".

Generate this format whenever a venture needs its operational model shown. A spatial
ops-map (boxes + flows) may accompany it as a secondary exhibit, but it does not
replace the register. The two prior box-diagram drafts were rejected for this reason.

---

## The unit of the map is the numbered product component

Every product flow is an addressable object with an ID, a type, and a state change.
Do not summarise flows into arrows between big boxes.

**The four component types (4-D product):**

| Type | Chip | Meaning |
|---|---|---|
| **CP** | Communications product | drives awareness / demand |
| **WP** | Working product | drives a state change in the case / customer |
| **PP** | Payment product | money flows |
| **PartP** | Partner product | partner-facing output |

**Numbering:** number sequentially within each type — CP1, WP1, WP2, PP1, PartP1.
The numbers narrate the transaction cycle in order.

**Flow subtypes** (state on each flow where a spatial ops-map accompanies the register):
- product flows: **core** (triggers payment) / **support** / **enabling**
- information flows: **production** / **marketing-TOFU** / **marketing-BOFU**
- money flows: **inflow** / **outflow**

---

## Two taxonomies every component carries

**HR role types** (who produces or manages the component):

| Tag | Meaning |
|---|---|
| Direct | produces or delivers the product |
| Managerial | oversees the producing role |
| Support | enables execution, not in the production chain |
| Venture-wide | strategic / one per venture |

**Journey actors** (who experiences the component):

| Tag | Meaning |
|---|---|
| Customer | the paying end user(s) — name them (e.g. Claimant, Borrower) |
| Partner | an enabler brought into the operating model |
| External | escalation-only / outside the chain |

Distinguish **People vs Places** where a spatial ops-map is drawn.

---

## Document structure (in order)

1. **Header** (navy) — eyebrow, title, one-paragraph subtitle, meta-row:
   `PCO · Traced from: CTM · AOM · ARM · Fin Sim · Version · Date`. Include the venture
   **archetype** (e.g. "high-touch digital service").
2. **Governing thought** (navy panel) — what the synthesis exposes that no single
   source document carries.
3. **Legend** (three-column grid) — product types · HR role types · journey actors.
4. **Overview table** — one row per component:
   `ID · Name · State change driven · Direct producer · Primary journey actor`.
5. **Component detail cards** — one per component, header colour-coded by type:
   - **State change** (+ recipient), stated as `before → after`
   - **Activities required** (arrow list, drawn from the ARM)
   - **Requirements** (grid, categorised: volume / regulatory / financial / structural / quality)
   - **HR positions** (direct / managerial / support, with role tags)
   - **Journey actors** (actor pills)
6. **Cross-ref table** (optional) — HR role × components touched.
7. **Footnote** — sources and version.

**Build right to left** — start from what the customer receives, work back to what
produces it. Activities are derived from the flows, not invented from an org chart.

---

## House style (mandatory)

Use the Dex design system: DM Sans (UI) + Lora (body), `#f5f4f1` background,
`#0f2744` navy panels, sharp corners (tags/chips at 3px only). Product-type chip
colours: CP blue `#1d4ed8` · WP red `#dc2626` · PP green `#16a34a` · PartP purple
`#7c3aed`. See CLAUDE.md for the full CSS boilerplate.

**File naming:** `[venture]-components-map.html`.

---

## The bridge to the financial model

Each component's activities must trace to the ARM (the HR positions that produce it)
and to the Fin Sim (the unit economics that constrain it). A component with no
producing role or no volume driver is incomplete — the same discipline as the AOM
activity table. Every money **outflow** (fraud loss, levy, refund, partner fee) must
appear as its own PP component or as an activity inside one.
