# Known Limitations

This is a **Public Engineering Reference — AS-IS**, not a qualified power module.
Historical integration tests do not establish a guaranteed operating envelope
for new assemblies, substitutions or the prepared revision.

## Fuse Holder and Board Ratings

F1 is Littelfuse 178.6165.0002. The manufacturer's ATO FLR datasheet, revision
032025, assigns its four-pin-per-terminal version a 32 VDC maximum, 30 A maximum
and 22.5 A continuous component current. The continuous figure applies to the
four-pin, silver-plated terminal construction, not the lower-current one-pin
version. The one-page sheet does not supply a complete ambient-temperature,
PCB copper or installation derating procedure. Do not invent such conditions.

Do not advertise or operate this assembly above either the 32 VDC or 30 A
maximum holder limit, or treat 30 A as continuous. Neither the 22.5 A holder
figure nor the installed 25 A fuse establishes a complete-board continuous
rating. Installation, heat, contacts, copper, wiring and other components can
impose lower limits. The actual demonstrated voltage/current/time envelope was
not recorded in the supplied evidence.

Historical 12–60 V, 80 V-holder, 25 A/50 A board-variant and 90 A-device labels
are not release operating ratings.
[Littelfuse ATO FLR datasheet](https://www.littelfuse.com/assetdocs/ato-flr-datasheet?assetguid=bef6771d-7ae2-4b18-8f55-8cde6402100a).

## Retained Electrical and Assembly Limitations

- D1 is specified as SMCJ85A, with 85 V standoff and 137 V clamping at the
  manufacturer's stated pulse condition. U1 has a 70 V absolute supply maximum;
  C1's BOM rating is 50 V. This TVS is not coordinated protection for the
  complete board. No surge-withstand claim is made.
- The sense/diagnostic output is not guaranteed to remain below 3.3 V in fault
  conditions. Receiver protection and fault handling are external responsibilities.
- The saved controller connector revisions are not straight-through compatible.
- FB1's confirmed 1206 part uses retained 0805 lands. Mechanical/reflow suitability
  is not generalized from the historical hand assembly.
- No complete thermal qualification, transient qualification, independent
  alternative-device test or commercial certification is included.
- Source DRC passes the saved design rules; that is not certification of the
  historical order's strict 8/8-mil fabrication limits. Fabricator CAM review
  must assess the supplied geometry and 2 oz copper.

The source preserves 18 ERC pin-type findings, including joined U1 output
pins and unspecified custom connector/fuse pins. See the
[engineering audit](../PUBLIC_RELEASE_AUDIT.md). The prepared revision has not
been refabricated or physically tested. No redesign is represented as having
resolved these limitations.

Sources: [SMCJ datasheet](https://www.littelfuse.com/assetdocs/tvs-diodes-smcj-datasheet?assetguid=37388813-0d6d-4329-969b-1aa8b7614ac1),
[BTH50030 datasheet](https://www.infineon.com/assets/row/public/documents/10/49/infineon-bth50030-1lua-datasheet-en.pdf).

No guaranteed protection, measurement accuracy, fitness, future development or
technical support is promised. The official LICENSE governs warranty and
liability terms; this summary does not amend them.
