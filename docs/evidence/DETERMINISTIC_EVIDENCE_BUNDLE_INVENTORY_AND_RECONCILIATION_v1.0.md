# Deterministic Evidence Bundle Inventory and Reconciliation v1.0

**Status:** Structural inventory PASS; semantic evidence acceptance remains OPEN.  
**Baseline archive:** `UNIVERSE_TENTOR_HOS_EVIDENCE_BASELINE_v1.0.zip`  
**Purpose:** Reconcile every non-directory ZIP entry against bundle manifest and checksum list without promoting source claims to accepted architecture.

## 1. Deterministic counts

| Category | Count |
|---|---:|
| All file entries in ZIP | 78 |
| Captured files listed in `bundle_manifest.json` | 76 |
| Entries in `checksums.sha256` | 77 |
| Primary captured evidence (`01_EVIDENCE`) | 20 |
| GitHub repository snapshots (`02_GITHUB`) | 41 |
| Provenance metadata (`03_PROVENANCE`) | 3 |
| Source-reference and source-only index (`04_SOURCE_REFERENCES`) | 8 |
| Evolution input register (`05_EVOLUTION_INPUT`) | 1 |
| Index/audit/limitations (`00_INDEX`) | 3 |
| Bundle manifest | 1 |
| Checksum manifest | 1 |

The 61 project artifacts (20 primary evidence files + 41 repository snapshots) reconcile to the project-artifact aggregate previously reported in the bundle audit. The remaining 17 entries are bundle-support material (source references 8, provenance 3, evolution register 1, index/audit/limitations 3, and manifest/checksum 2).

## 1A. ZIP entry-count convention reconciliation

The attached archive was directly listed and counted. It contains **128 total ZIP entries = 78 file entries + 50 explicit directory entries**. The extraction note's count of 128 is therefore consistent when directories are included; the earlier 78 count refers only to non-directory/file entries. The attached archive SHA-256 matches the extraction note's recorded digest. This resolves the count-convention discrepancy (see `SOURCE_INTAKE_DISCREPANCY_EXTRACTION_NOTE_vs_ATTACHED_ZIP_v0.1.md`). It does not alter the manifest or checksum populations and does not constitute semantic evidence acceptance.

## 2. Integrity results

- Every archive file listed in the captured-files manifest was checked for path presence, byte size, and SHA-256: **76/76 matched**.
- Every path listed in the checksum manifest was checked for presence and SHA-256: **77/77 matched**.
- No SHA-256 or size mismatch was found among the entries governed by those lists.
- The checksum manifest does not checksum itself.
- The bundle manifest and checksum manifest are not entries in the manifest's 76 captured-file records. This is recorded as the bundle's manifest accounting convention, not as evidence that those two files were independently covered by the captured-files list.

## 3. Inventory artifact

The deterministic row-level inventory was generated from the ZIP archive and includes each of the 78 file paths, category, byte size, actual SHA-256, manifest membership and match fields, and checksum membership and match fields. The working inventory is retained as `DETERMINISTIC_BUNDLE_INVENTORY.csv` in the execution workspace. It has 78 data rows.

## 4. Reconciliation boundary

This PASS is limited to archive structure and integrity accounting. It does **not** establish:
- semantic correctness, completeness, or currentness of any source artifact;
- that historical PASS/FAIL/PARTIAL/GAP/BLOCKED states remain current;
- approval of any legacy architecture as the TENTOR HOS V.2 canonical architecture;
- conformance of a future implementation; or
- completion of independent U-AAFA.

Duplicates and source-only references remain separately identifiable and must not be silently merged or treated as independent corroboration. Evidence synthesis must preserve source identity, provenance, historical status, and epistemic class.

## 5. Gate disposition

**STEP 00 — structural bundle reconciliation: PASS.**  
**Evidence Registry semantic reconciliation and source-by-source acceptance: OPEN.**  
**Architecture synthesis / canonical specification / implementation / U-AAFA: NOT AUTHORIZED BY THIS RESULT ALONE.**

Next action: perform source-by-source semantic review of the 61 registry entries, capturing content-grounded summaries, provenance, historical status and context, limitations, duplicates/overlaps, conflicts, and acceptance rationale. Preserve unknowns as UNKNOWN/PENDING; only then begin controlled evidence synthesis against the agreed TENTOR HOS V.2 scope.
