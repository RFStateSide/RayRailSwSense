# Project-local Libraries

Open ../RayRailSwSense.kicad_pro with KiCad 9. Both tables use KIPRJMOD-relative
paths. No global Ray, Ray_C, MyConnectors or MyFootprints collection is required.
Optional 3D models are omitted.

The local symbols preserve working pins/graphics. Footprints preserve placed
pad shapes and geometry; U1 uses the PCB's established tab geometry instead of
the slightly different footprint formerly selected in the schematic.
Board-only H1–H4 retain their original grounded mounting geometry.

RF StateSide's owner personally created the custom BTH, fuse-holder, M4
terminal, TVS and mounting-hole footprints and project-specific schematic
symbols. Those original contributions use the project license.

Stock KiCad-derived resistors, capacitors, bead, terminal, power symbols and
retained upstream elements remain attributed to KiCad library contributors,
under CC-BY-SA-4.0 with the KiCad-libraries-exception. Retain LICENSE-KiCad.md
and KiCad-libraries-exception.txt. [KiCad library terms](https://www.kicad.org/libraries/license/).

Inherited library names are identifiers, not population instructions. R4 uses
a retained LED-named land pattern for a resistor; FB1 uses 0805-designated lands
for the confirmed 1206 bead. See the assembly guide before reproduction.
