# Source Intake Discrepancy — Extraction Note vs. Attached Baseline ZIP

**Record ID:** THOS-REC-002  
**Version:** 0.1  
**Date:** 2026-09-26  
**Status:** OPEN — source-package identity/revision reconciliation required  
**Scope:** Compare the user-provided text file `Ekstrak Evidence Project.txt` with the attached `UNIVERSE_TENTOR_HOS_EVIDENCE_BASELINE_v1.0.zip`. This is a reconciliation note, not a judgment that either source is invalid.

## Source A — extraction note (user-provided text)

The text states:
- 76 captured evidence files;
- 7 binary Library artifacts marked source-reference-only;
- total 128 ZIP entries;
- final ZIP SHA-256 `f4d6bc2999c33d97d3c6673c27517c8123d646548c1718c53886af6bde1d845c`.

These are recorded as claims in the text artifact, not independently accepted solely by being written there.

## Source B — attached ZIP and repository reconciliation records

The currently attached ZIP was directly inspected and its recorded SHA-256 matches the digest above. The existing bundle audit records 78 ZIP file entries, 76 manifest-captured files, 77 checksum-list entries, and 7 source-only Library records. The bundle manifest and checksum records are independently represented in the bundle accounting.

## Discrepancy

The extraction note's stated total of 128 ZIP entries differs from the current attached ZIP's recorded 78 file entries. The evidence does not yet establish whether this is due to a different archive revision, counting convention (e.g. directories as entries), or a stale extraction note. Do not silently harmonize 128 and 78.

## Required resolution

1. Obtain or identify the exact archive revision that the extraction note describes, if distinct from the currently attached ZIP.
2. Determine whether “128 ZIP entries” includes directory entries or a different count population; record the counting method.
3. Compare the archive SHA-256 and manifest/checksum sets for each identified revision.
4. Preserve both source claims and document the reconciliation result with exact archive identity and reproducible counts.

## Disposition

- Current attached ZIP integrity: use the independently recorded integrity result in `EVIDENCE_CORPUS_RECONCILIATION_INITIAL_FINDINGS_v0.1.md`.
- Extraction-note claim of 128 entries: OPEN / not reconciled.
- No impact is asserted on the 76 manifest-listed files' byte integrity; no semantic or architectural acceptance is implied.
