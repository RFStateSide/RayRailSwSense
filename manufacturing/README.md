# Manufacturing Package

P2-prep-01 contains the manufacturing outputs generated from the supplied
RayRailSwSense KiCad source with KiCad 9.0.7. It includes two copper layers,
front/back mask, paste and silkscreen, board outline, plated/nonplated drills,
placement CSV, tested-population BOM, job metadata, LICENSE and NOTICE.

Use the entire identified set. Do not mix it with historical DcSwSense exports
or with the earlier LTC7001/INA240 design. The historical fabrication archive
is retained separately; this set contains revised labels and metadata.

## Fabrication Reference

Individual board: 60 × 40 mm, two layers, nominal 1.6 mm FR-4, 2 oz finished
copper per the original order. Original order material was TG150, leaded HASL,
blue mask, white silkscreen and tented vias. The source stackup now records
nominal 70 µm copper. Supplier panelization is not supplied as a release PCB.

The original order stated 8/8 mil and minimum 0.3 mm holes. The preserved
project rules include 0.15 mm minimum clearance; a passing source DRC does not
prove strict 8-mil compliance. Obtain CAM acceptance for the supplied geometry
and intended copper. Do not silently alter copper to fit an order preset.

The SMT assembly is a historical hand-reflow design. Read the FB1 fit limitation,
U1 tab/pin mapping and fuse information in [assembly](../docs/assembly-and-history.md).
A fuse is a separate purchase from the holder. No alternative-device assembly
has been separately tested.

## Verification

Run the [distribution checks](../docs/distribution-integrity.md) before using
or modifying files. Preserve the BOM, license and notices with the outputs.
Generation timestamps and corrected silkscreen distinguish these outputs from
the submitted PCBWay archive. See [manufacturing history](../docs/manufacturing-history.md).

No new fabrication, load testing or thermal qualification was performed for
P2-prep-01.
