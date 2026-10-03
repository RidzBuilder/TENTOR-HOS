# Source Intake Discrepancy — Extraction Note vs. Attached Baseline ZIP

**Record ID:** THOS-REC-002  
**Version:** 0.2  
**Date:** 2026-09-26  
**Status:** RESOLVED — count convention reconciled; source semantic review remains open  
**Scope:** Compare the user-provided text file `Ekstrak Evidence Project.txt` with the attached `UNIVERSE_TENTOR_HOS_EVIDENCE_BASELINE_v1.0.zip`.

## Source A — extraction note

The user-provided text states 76 captured evidence files, 7 binary Library artifacts marked source-reference-only, 128 ZIP entries, and SHA-256 `f4d6bc2999c33d97d3c6673c27517c8123d646548c1718c53886af6bde1d845c`.

## Source B — direct archive inspection

The currently attached ZIP's SHA-256 matches the digest stated in the extraction note. Direct listing with `unzip -Z -1` and counting archive paths by trailing slash establishes:
- 78 non-directory/file entries;
- 50 explicit directory entries;
- 128 total ZIP entries when both files and directories are counted.

An extraction to the working directory yields 79 filesystem directories including the extracted top-level root, equivalent to 50 directories inside the archive plus that root directory.

## Reconciliation

The values 128 and 78 refer to different counting populations, not conflicting archive revisions: 128 counts all ZIP entries (78 files + 50 directory entries), while 78 counts file entries only. The extraction note's count is consistent with the attached archive under the all-entry convention.

This resolution applies only to entry-count semantics and archive identity. It does not change the manifest/checksum populations or certify the semantic content of the evidence.

## Disposition

- Archive identity by SHA-256: MATCH.
- ZIP entry count: 128 total = 78 files + 50 explicit directories.
- Captured-file manifest: 76 entries; independently checked against path, size, SHA-256.
- Checksum list: 77 entries; independently checked against path and SHA-256.
- Count-convention discrepancy: RESOLVED.
- Evidence semantic review and acceptance: OPEN.
- No canonical architecture or implementation acceptance is implied.
