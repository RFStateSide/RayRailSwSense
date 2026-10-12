# Manufacturing History and Source Correspondence

The owner identifies PCBWay order W764321AXZ20 as the redesigned BTH board.
The downloaded W764321AXZ20_DcSwSense.kicad_pcb_gerber.zip is authoritative
evidence of the submitted fabrication package. Its SHA-256 is
47e605185db54c0e42b0064dd97bae5ef975385d1ab60d0450195e9d52d2a8e2.

It is byte-identical to the October 26, 2025 production Gerber ZIP retained
with the engineering source. The order and archive establish fabrication
history; fitted parts and successful integration testing are separate
owner-confirmed evidence.

## Recorded Fabrication

The order specifies a supplier 2 × 5 panel, ten panels/100 individual boards,
130 × 208 mm, two-layer 1.6 mm TG150 FR-4, 2 oz finished copper, 8/8 mil
track/spacing, minimum hole 0.3 mm, blue mask, white silkscreen, leaded HASL and
tented vias. The submitted archive contains the individual 60 × 40 mm board.
The separately saved 308 × 82 mm local panel is not the order's supplier panel.

The original editable stackup said 35 µm copper. The release records nominal
70 µm copper layers and a corresponding 1.44 mm dielectric core within the
existing nominal 1.6 mm board; this is fabrication metadata reconciled to the
2 oz order, not a measurement of the fabricated stack.

## What Matches and What Changed

The current source and prepared source have identical pad geometry, placement,
routing, vias, zone polygons/fills and outline. The prepared copper, mask,
paste and outline Gerbers match the submitted archive's drawing primitives
after accounting for plot order, aperture numbering and metadata. All 51
numbered component pads match in position and net. All 127 drilled-hole
locations and diameters agree within 0.003 mm, allowing for the original
inch-output rounding.

P2-prep-01 changes source identities and metadata, corrects U1/R4/FB1 records,
localizes libraries, removes unused external assets, and updates misleading
rating text. Revised silkscreen and regenerated headers make the release
files different from the original submission. They are not byte-identical
reproductions of the submitted archive.

Historical root CSV/ZIP/interactive-BOM and August supplier artifacts describe
the earlier LTC7001/INA240 design. They are deliberately excluded.
See [machine comparison](validation/source-comparison.json) and
[source hashes](source-traceability.json).
