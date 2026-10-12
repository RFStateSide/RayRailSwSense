# RayRailSwSense — Public Release Engineering Audit

Prepared with OpenAI Codex. Reviewed by RF StateSide LLC.
This is a prepared review candidate; document-by-document owner acceptance is pending.

## Scope

P2-prep-01 is the standalone BTH hardware reference. The older LTC7001/INA240
project remains separate. No physical testing, refabrication or electrical
redesign was performed during preparation.

## Engineering Preparation

The tested population is BTH500301LUAAUMA1 with R4 = 2 kΩ, BLM31PG121SN1L
(DigiKey 490-1056-1-ND) and a 25 A, 32 VDC automotive fuse. BTH500151LUAAUMA1
is an unverified alternative. The installed fuse rating is not a measured
board-current result.

Corrected source/assembly metadata includes U1 identity and mounting type,
R4 value/MPN, FB1 procurement, F1 limitations, local library references and
consistent project/revision titles. The placed U1 geometry was preserved
instead of replacing it with the formerly selected schematic footprint.
The four board-only mounting features received H1–H4 references.
Optional models and the obsolete embedded shunt datasheet were omitted.

Misleading 12–60 V and device-current labels were corrected. The original
v2.0 artwork identification remains; P2-prep-01 identifies the prepared set.
Nominal copper stackup metadata now represents the original order's 2 oz.
No pad, copper, drill, outline, placement or routing geometry was changed.

## Automated Validation

KiCad 9.0.7 reports zero DRC violations, zero unconnected PCB items and zero
schematic-parity findings with the saved project rules. A separate exported
netlist comparison confirms the same pin-net partitions.

ERC retains 18 pin-type findings: three involve deliberately connected U1
output pins and fifteen involve unspecified fuse/terminal pin types.
Pin types were not changed merely to suppress findings.
The full reports are in [validation](docs/validation/).

The package checker confirms 15 electronic references, four board-only
mounting features, local library resolution, BOM/placement consistency,
critical population values, J3 assignments, 51 Gerber pad positions/nets and
127 drill locations/diameters. [Check results](docs/validation/checks.json).

The source's unchanged layout fingerprint and the submitted PCBWay archive
comparison are recorded in [source comparison](docs/validation/source-comparison.json).
Copper, mask, paste and outline drawing primitives agree after normalization
of order/identifiers; drill comparison allows 0.003 mm for historical inch
rounding. Corrected silkscreen and metadata are distinct release changes.
The generated files are not byte-identical to the historical submission.

## Inherited Limitations

The holder is limited to 32 VDC maximum, 30 A maximum and the manufacturer's
22.5 A continuous component figure. No complete-board continuous rating or
documented maximum sustained test point is established.
The FB1 1206-on-0805-land mismatch, fault-sense voltage range, uncoordinated
85 V TVS selection and saved-controller connector mismatch are disclosed in
[known limitations](docs/known-limitations.md) and [integration](docs/integration.md).
Saved DRC rules are not proof of strict 8/8-mil order compliance.

## Authorship and Acceptance

The owner confirmed authorship of the project-specific symbols and custom
footprints and approved CERN-OHL-P-2.0 for original hardware contributions.
Applicable KiCad notices remain. Supplier records and external vendor assets
are excluded. Official license bytes are checked against recorded provenance.

This audit records automated evidence and owner-supplied history; it does not
replace owner inspection, independent clone review, or later publication
authorization. The package and public wording still require owner acceptance.

## Portability and Distribution

A relocated directory containing spaces passed engineering verification,
DRC and the same 18 ERC findings with a newly created default KiCad profile
containing no owner-specific libraries. Native Linux execution was not tested.
See [portability results](docs/validation/portability.json).

The exact-byte distribution was checked with isolated temporary Git indexes
and object storage for core.autocrlf true/false/input and core.eol lf/crlf.
Every indexed blob and checkout byte matched the prepared payload, and the
manifest passed in each checkout. No Git repository, commit or branch was
created for this project. This distribution check is not publication approval.

