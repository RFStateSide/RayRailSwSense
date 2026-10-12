# Source and Distribution Integrity

P2-prep-01 ties the editable design to the supplied manufacturing set.
SHA256SUMS records every payload file except itself. The Git attributes use
* -text to preserve exact bytes across future staging/checkouts, including
mixed historical line endings and the official license.

From the repository root, verify hashes with:

```text
python tools/integrity.py
```

For source/manufacturing checks, with KiCad 9 installed:

```text
python tools/verify.py --kicad-cli <kicad-cli executable>
```

The checker verifies pin-net partitions, local definitions, component identities,
BOM/placement coverage, connector assignments, 51 component-pad Gerber positions
and nets, and 127 drilled-hole locations/diameters. It also checks the retained
validation reports and original-layout fingerprint. Reports describe automated
file checks, not physical operating tests.

After an intentional design change:

```text
python tools/generate.py --kicad-cli <kicad-cli executable>
python tools/verify.py --kicad-cli <kicad-cli executable> --record
python tools/integrity.py --write
```

Review changed outputs and update revision/validation expectations first.
The verifier deliberately rejects departures from this prepared baseline;
engineering changes require corresponding reviewed changes to its expectations.
Generation changes timestamps and invalidates the manifest. --record writes a
check report but does not renew SHA256SUMS. Do not use manifest regeneration to
conceal unexplained mismatches.

The no-KiCad integrity checker rejects missing, extra and changed files.
Personal preferences, lock files, caches and backups are not release payload.
Keep original supplier archives outside the package.
