# Evidence Baseline Intake & Integrity Report

**Artifact ID:** THOS-EVID-INTAKE-001  
**Version:** 1.0.0  
**Execution date:** 2026-09-26  
**Status:** PACKAGE INTEGRITY PASS; CONTENT RECONCILIATION IN PROGRESS

## 1. Input package

- Filename: `UNIVERSE_TENTOR_HOS_EVIDENCE_BASELINE_v1.0.zip`
- Reported archive SHA-256: `f4d6bc2999c33d97d3c6673c27517c8123d646548c1718c53886af6bde1d845c`
- Independently recomputed SHA-256: `f4d6bc2999c33d97d3c6673c27517c8123d646548c1718c53886af6bde1d845c`
- Checksum comparison: PASS
- ZIP CRC/archive integrity test: PASS (no corrupt member reported)
- ZIP entries: 128 total; 78 file entries; 50 directory entries.

## 2. Archive top-level structure

The archive has one root directory, `UNIVERSE_TENTOR_HOS_EVIDENCE_BASELINE_v1.0/`, containing:

- `00_INDEX/` — README, bundle audit, limitations.
- `01_EVIDENCE/` — recovered Library and research evidence.
- `02_GITHUB/` — evidence-bearing repository files grouped by ACPA, ACS, CCH-OS, LCH-OS, EVO.
- `03_PROVENANCE/` — repository metadata, pull request records, selected commit lineage.
- `04_SOURCE_REFERENCES/` — source-reference-only records and CSV for binary Library artifacts not materialized as raw bytes.
- `05_EVOLUTION_INPUT/` — evolution input register.
- `bundle_manifest.json` and `checksums.sha256`.

## 3. Evidence populations

The accompanying bundle audit and manifest must be used as authoritative internal classifications. The ZIP's 78 file entries include evidence, source-reference records, provenance, indexes, and manifests; therefore, ZIP file count is not equivalent to count of substantive evidence artifacts.

The package intake report previously described 76 captured evidence files and 7 binary Library artifacts as source-reference-only. Those counts are retained as reported classifications and will be reconciled against `bundle_manifest.json`, `00_INDEX/BUNDLE_AUDIT.md`, `00_INDEX/LIMITATIONS.md`, and `04_SOURCE_REFERENCES/source_only_library_artifacts.csv`.

## 4. Source and governance boundary

This package is a research/evidence baseline, not the canonical TENTOR HOS V.2 architecture. Source project specifications, historical decisions, implementation records, test outcomes, inferred convergence patterns, and open gaps must remain distinguishable.

No source project's historical PASS, FAIL, PARTIAL, GAP, or BLOCKED status is automatically inherited as current TENTOR HOS conformance.

## 5. Remaining acceptance criteria

- [x] Actual ZIP recovered in current execution.
- [x] SHA-256 independently recomputed and matched.
- [x] ZIP archive integrity tested successfully.
- [x] Archive directory/file inventory inspected.
- [ ] Internal manifest and bundle audit reconciled item-by-item.
- [ ] Source-reference-only artifacts reconciled against the CSV and limitations.
- [ ] Evidence IDs and provenance links registered in the TENTOR-HOS evidence registry.
- [ ] Cross-project convergence, conflict, and gap analysis completed.
- [ ] Fundamental TENTOR HOS V.2 specification derived and independently reviewed.

## 6. Gate decision

**GATE 00A — Package Integrity: PASS.**

**GATE 00B — Evidence Corpus Reconciliation: IN PROGRESS / NOT YET PASS.**

Proceed to detailed manifest and evidence reconciliation. Do not declare Evidence Synthesis complete or canonical specification ready until the remaining acceptance criteria are satisfied.
