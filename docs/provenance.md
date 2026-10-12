# Asset Provenance

RF StateSide LLC developed the original RayRailSwSense hardware. Original
contributions and retained upstream definitions have distinct rights.

| Included material | Authorship and treatment |
|---|---|
| Hardware, BOM and engineering documentation | RF StateSide original work and recorded preparation; CERN-OHL-P-2.0 |
| Custom BTH, fuse-holder, M4 terminal, TVS and grounded mounting footprints | Personally created by the RF StateSide owner |
| Project-specific BTH, fuse-holder, M4 terminal and TVS schematic symbols | Personally created by the RF StateSide owner |
| Stock and upstream-derived passive, connector and power definitions | KiCad contributors; CC-BY-SA-4.0 with KiCad library exception |
| Schematic/PCB SVGs | Generated from the supplied CAD; not physical-test photographs |
| Legal texts | Respective licensors' original wording retained |

The owner confirmed both custom footprint and project-specific symbol
authorship during preparation. DigiKey procurement references do not imply
downloaded CAD ownership. Retained upstream elements remain subject to their
own terms. See [library attribution](../hardware/libraries/README.md).

Definitions were extracted from the working schematic and placed PCB rather
than refreshed from changing global libraries. The U1 local symbol retains
the existing pin definitions and is labeled for the tested BTH50030 population.
Its four output pins and supply tab remain electrically unchanged.

The obsolete CSS2H-3920 vendor PDF embedded in the original schematic is
omitted from this package. Vendor STEP models, PDFs, supplier orders, quotations,
historical interactive-BOM software, databases and backups are not distributed.
No unknown external model is required to use the editable project.

The original fabrication archive and order document remain private source
evidence. [Source traceability](source-traceability.json) identifies their hashes;
[manufacturing history](manufacturing-history.md) describes their relationship
to this release. They are not relicensed by the project license.

ChatGPT/Codex assistance is acknowledged in README; the public engineering
audit is separately attributed. Original design, assembly and physical testing
remain RF StateSide's work.
