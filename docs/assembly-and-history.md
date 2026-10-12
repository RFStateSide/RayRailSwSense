# Assembly and Development History

## Earlier LTC7001/INA240 Design

The original board used INA240A2QDRQ1, LTC7001EMSE-PBF and PSMN1R8-80SSFJ.
PCBWay manufactured and populated it. Q1's original footprint reversed pins
1 and 5; we reinstalled Q1 in the opposite orientation and successfully tested
the board with RaySspaController. The subsequent CAD correction was not
refabricated. That project is preserved separately and is not the build source
for this repository.

## Redesigned BTH Board

PCBWay order W764321AXZ20 produced the redesigned board. We hand-populated and
reflow-assembled it, then tested it with RayPowerMeter and RaySspaController.

| Item | Owner-confirmed assembly |
|---|---|
| U1 | BTH500301LUAAUMA1 |
| R4 | 2 kΩ |
| FB1 | Murata BLM31PG121SN1L; DigiKey 490-1056-1-ND |
| Fuse | Automotive-type, 25 A, 32 VDC; exact manufacturer and time/current curve unrecorded |

The originally supplied “490-1056-1-MD” was confirmed as a typo for “-ND”.
The installed fuse rating does not demonstrate a 25 A continuous load test.
Test voltage, maximum sustained current, duration, temperature and the exact
tested controller/harness revision are not established by the retained records.

## Assembly References

Use the BOM and placement CSV for the tested population. U1 is surface-mounted;
its large supply tab is pad 9, connected to the fused input. Pins 5–8 form the
switched output. Select and orient parts by electrical pin numbers and the
schematic, not by historical library names.

FB1 is a 1206 device fitted on the existing 0805-designated lands. This package
preserves that tested-layout geometry and explicitly records the mismatch.
It does not certify a standard reflow land pattern or authorize a silent
replacement with a different bead. Check component seating and solder joints
for any reproduction.

R4 retains the original two-pad LED-library land geometry; it is populated
with a nonpolar 1206 resistor. The footprint's inherited name is not a
requirement to fit an LED. H1–H4 identify four grounded mounting features;
mounting hardware dimensions and insulation depend on the installation.

The fuse holder and removable fuse are separate items. Select a suitable
32 VDC-or-higher interrupt-rated fuse for the actual circuit while respecting
the holder's 32 VDC maximum and its current/thermal limits. Fuse rating alone
does not establish holder or PCB continuous capacity.

BTH500151LUAAUMA1 is an unverified alternative population. It uses different
sense scaling and protection characteristics; it does not increase the
holder's limits. See [integration](integration.md).

## Prepared Revision

P2-prep-01 reconciles component records, local libraries, ratings and fabrication
metadata. Copper, pad geometry, holes, routing and placement are unchanged.
Historical v2.0 identification remains on the artwork; the title block and
package identifier distinguish the prepared revision. The source directories
and original submitted manufacturing archive remain unchanged.
