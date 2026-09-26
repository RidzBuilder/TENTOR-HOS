# Evidence Corpus Reconciliation — Initial Findings

**Artifact ID:** THOS-EVID-RECON-001  
**Version:** 0.1.0  
**Date:** 2026-09-26  
**Status:** PARTIAL — classification discrepancy requires reconciliation

## Verified results

1. Outer ZIP SHA-256 matches the recorded digest:
   `f4d6bc2999c33d97d3c6673c27517c8123d646548c1718c53886af6bde1d845c`.
2. ZIP CRC integrity test passes.
3. `bundle_manifest.json` declares 76 captured_files.
4. Every one of those 76 manifest entries exists and matches both declared size and SHA-256.
5. `checksums.sha256` contains 77 file entries; every listed path exists and every checksum matches.
6. Source-only Library CSV contains 7 records, including duplicates explicitly identified for ACS and LCH-OS.

## Classification discrepancy

`00_INDEX/BUNDLE_AUDIT.md` reports these captured evidence counts:

- ACOS: 3
- ACPA: 11
- ACS: 16
- CCH-OS: 11
- EVO: 15
- LCH-OS: 5

These values sum to 61, not 76. The manifest's 76 captured_files is a broader package-level population that includes different directory groups and metadata. The bundle's 78 ZIP file entries also include files not listed in the manifest/checksum populations.

This is not necessarily a content-integrity failure: all declared manifest/checksum file hashes match. It is a classification/accounting discrepancy that must be reconciled before declaring the evidence corpus inventory fully PASS.

## Required next actions

- Build a deterministic inventory with a classification for every ZIP file entry: substantive evidence, repository snapshot, provenance, index/audit, evolution register, source-reference record, checksum/manifest, or other.
- Reconcile the six per-project audit counts against actual per-project evidence classifications and manifest membership.
- Identify the two ZIP file entries not represented in the 77-entry checksum file (expected to be the checksum file itself and bundle manifest, subject to direct path-level verification).
- Preserve the seven source-only Library artifact records and duplicate relationships.
- Record evidence ID, source project, original path, package path, SHA-256 (where applicable), evidence class, source status, provenance pointer, and limitations.

## Gate status

- Package integrity: PASS.
- Manifest-listed file integrity: PASS (76/76).
- checksums.sha256-listed file integrity: PASS (77/77).
- Evidence classification/accounting: PARTIAL / GAP.
- Full evidence synthesis and canonical specification: NOT STARTED.
