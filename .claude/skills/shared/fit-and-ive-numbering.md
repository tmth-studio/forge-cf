# FIT Startup and IVE: numbering and the price lines

**Owner:** Head of R&D · **Source:** RD-063, 5 November 2026 · **Status:** reference (RD-068, 6 November 2026). FIT Startup is Erik Simanis's method. It is not used for verdicts

## Which text means which

IVE runs R1 to R10 in number order, and R3 is a requirement. This file does not set an order.

In IVE text, the fit gate, the FIT reading, the `FMOS` figure and `ive-fit-verifier-custom` are IVE's own check. They do not mean FIT Startup.

## Name the system each time

FIT Startup has nine requirements and IVE has ten. The same number can mean different things, so write "FIT Startup R3" or "IVE R3", never a bare number, whenever FIT Startup's numbering is in use.

| FIT Startup | FIT Startup name | IVE | IVE name |
|---|---|---|---|
| FIT Startup R1 | Critical limiting operation | IVE R1 | Circumvent at-scale cost bottleneck |
| FIT Startup R2 | Value bottleneck | IVE R2 | Eliminate customers' value bottleneck |
| none | FIT Startup handles scaling and working capital in its financial model | IVE R3 | Circumvent scaling cost bottleneck |
| FIT Startup R3 | Gateway barrier | IVE R7 | Activate gateway partners |
| FIT Startup R4 | Want | IVE R4 | Want block |
| FIT Startup R5 | Use | IVE R5 | Use block |
| FIT Startup R6 | Buy | IVE R6 | Buy block |
| FIT Startup R7 | Customer defection | IVE R8 | Create a switching cost |
| FIT Startup R8 | Pricing race to the bottom | IVE R9 | Manufacture a resource moat |
| FIT Startup R9 | Supplier control over key input | IVE R10 | Replaceability of key supplier input |

The mapping for FIT Startup R4 to FIT Startup R9 rests on names and FIT Startup's paper The Wrong Level, because FIT Startup publishes no primers for them.

## Three price lines, three meanings

| Line | Form | What it is |
|---|---|---|
| Price clearing 25% margin | cost floor × 1.25 | The price at which (price − floor) ÷ floor is 25 per cent. A margin line |
| FIT Startup's required price | the price at which net present value is zero at the investors' target return | Corresponds to our cost floor with return on capital included. Not the line above |
| Capital bar (IVE R2) | from the PCO investment parameters | The same form as FIT Startup's screening price at the PCO |

FIT Startup's 25 to 40 per cent is an annual rate on invested capital. Our 25 per cent is a margin on unit cost. They are different quantities, and the matching number is a coincidence.

Our simulation page prints FIT Startup's form as "Price at zero net present value", information only, from `ive-fin-sim-custom/scripts/zero_npv_price.py`. We never label it "required". The margin line is "price clearing the target margin". Item 30 v0.5 does not read this figure (the standard, line 86). Item 30 v0.4 did, for one day; that text is a dated record.

The word "price clearing" changes a label and a formula for a printed line only. Every pass mark stays in `Forge/WS1/criteria-registry.md`, and the verdict still reads (ceiling − floor) ÷ floor.

Use the method in our own words. Nothing here implies that Erik Simanis or FIT Startup endorses our work.
