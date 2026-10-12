# RayRailSwSense

RayRailSwSense is RF StateSide LLC's high-side DC rail switch with current and
switched-output voltage sensing for amplifier and instrumentation development.

**Public Engineering Reference — AS-IS.** Editable KiCad sources, a population
BOM and manufacturing files support study, independent construction,
modification and continued development.

## Hardware and History

PCBWay manufactured the redesigned BTH board. We hand-populated it using a
reflow oven and successfully tested it with RayPowerMeter and RaySspaController.
The tested assembly used BTH500301LUAAUMA1, R4 = 2 kΩ, a Murata BLM31PG121SN1L
ferrite bead and a 25 A, 32 VDC automotive-type fuse. The fuse rating is not
evidence of a measured 25 A continuous test.

BTH500151LUAAUMA1 is an alternative device selection, not a separately verified
assembly or a higher-rated board variant. See [assembly and history](docs/assembly-and-history.md).

The supplied P2-prep-01 files reconcile the tested population and source
metadata while retaining the original copper, drilling, placement and routing.
Revised labeling and regenerated outputs distinguish this package from the
original fabrication submission. This prepared revision has not itself been
fabricated or physically tested.

## Operating Limits

The installed 178.6165.0002 fuse holder has a 32 VDC maximum, 30 A maximum
current and a manufacturer's 22.5 A continuous component figure. These are
component limits, not a complete-board operating specification. No guaranteed
continuous board current is established. Do not operate above the installed
holder's limits. See [known limitations](docs/known-limitations.md).

The sense connector is not directly interchangeable with the saved
RaySspaController connector revisions. Pin 1 carries raw switched rail voltage.
Use the [integration guide](docs/integration.md), not a straight-through cable
assumption. Current-sense fault output is not guaranteed to remain within 3.3 V.

## Opening and Building

Open [the KiCad 9 project](hardware/RayRailSwSense.kicad_pro). Required symbols
and footprints are included in project-local libraries; optional 3D models are
omitted. [View schematic](docs/images/RayRailSwSense.svg) ·
[View PCB front](docs/images/pcb-front.svg).

Use the [BOM](bom/RayRailSwSense.csv) and [manufacturing instructions](manufacturing/README.md)
together. FB1's owner-confirmed 1206 component is represented on the retained
0805 lands: this is an explicit historical fit limitation, not a standard
land-pattern recommendation.

## Repository Contents

| Location | Contents |
|---|---|
| hardware/ | Portable editable project and local libraries |
| bom/ | Tested-population procurement reference and assembly notes |
| manufacturing/ | Identified Gerber, drill, placement and BOM package |
| docs/ | Integration, history, limitations, provenance and verification |
| tools/ | Generation and integrity/engineering verification utilities |
| PUBLIC_RELEASE_AUDIT.md | Attributed technical validation record |

Original historical designs, supplier records and fabrication archives are
retained separately. No parent firmware or development-repository history is included.

## Development Tools

KiCad was used for schematic capture and PCB design. Python utilities support
source verification and manufacturing-package integrity checks. Git and GitHub
are the intended version-control and distribution tools.

ChatGPT by OpenAI and OpenAI Codex assisted with engineering review,
documentation, source organization, validation and preparation of the
open-hardware reference. RF StateSide LLC performed the original hardware
design, assembly and historical integration testing.

## License and Credits

Copyright RF StateSide LLC. Original contributions are provided under
**CERN-OHL-P v2.0**, SPDX **CERN-OHL-P-2.0**. The unmodified [LICENSE](LICENSE)
is authoritative; retain [NOTICE](NOTICE) and applicable library notices.
See [licensing](docs/licensing.md) and [provenance](docs/provenance.md).

RF StateSide created the project-specific symbols and custom footprints.
KiCad contributors supplied the stock and upstream-derived definitions.
No certification, guaranteed performance, future development or technical
support is promised.
