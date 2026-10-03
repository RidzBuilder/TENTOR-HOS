# Candidate Schema CI Result — Negative Controls

**Date:** 2026-09-28  
**Status:** PASS, scoped to the checks listed below  
**Repository:** RidzBuilder/TENTOR-HOS  
**PR:** #1 (draft; open; unmerged)  
**PR head tested:** f17fbe48c8435e64930035fea129939f3c4457a8  
**GitHub Actions run:** 36404352177  
**Job:** 108869385155 — candidate-schema-conformance  
**Workflow:** Candidate Evidence Schema Conformance  
**Run URL:** https://github.com/RidzBuilder/TENTOR-HOS/actions/runs/36404352177

## 1. Verified outcomes

GitHub Actions job completed with conclusion SUCCESS.

- JSON Schema Draft 2020-12 check and synthetic fixture harness: 7/7 fixture expectations matched (FIX-001 through FIX-007).
- Negative control A: deliberately inverted expectation was detected as a mismatch.
- Negative control B: removing required `record_id` was rejected.
- Negative control C: adding an undeclared root property was rejected.
- Negative control summary: 3/3 passed.

The PR workflow checked out the GitHub pull-request merge ref at merge commit `2ec0a4642aa0f0b46f2d6eb03c2fdc8c37aef442`, which incorporated PR head `f17fbe48c8435e64930035fea129939f3c4457a8` against base `fe4ec95b0a430a742c3a43a7f20da18d33ef45ba`.

## 2. Environment observed in the job

- GitHub-hosted Ubuntu 24.04.5 runner image (image version 20260920.314.1).
- CPython 3.12.14.
- jsonschema 4.25.1.
- Installed transitives observed in this run: attrs 26.1.0, jsonschema-specifications 2025.9.1, referencing 0.37.0, rpds-py 2026.6.3, typing-extensions 4.16.0.
- Checkout and setup-python actions were referenced by commit SHA.

## 3. Limitations and unresolved conditions

1. This is synthetic schema/conformance evidence only. It does not establish evidence authenticity, claim truth, provenance, semantic requirement coverage, product/runtime behavior, or architecture acceptance.
2. Dependency installation is not yet fully reproducible: transitive versions were resolved during the run and no complete hash-locked requirements file was used. The runner image and Python patch release are also not fully pinned as immutable artifacts.
3. The workflow emitted Node.js 20 deprecation warnings for actions, although the job succeeded.
4. Semantic validator implementation, semantic adversarial fixtures, independent review, evidence registry acceptance, and architecture gate remain open.

## 4. Gate disposition

**PASS:** Current schema check, seven synthetic schema fixtures, and three negative controls in this exact workflow run.

**NOT PROVEN / OPEN:** Reproducible dependency installation, semantic conformance, evidence acceptance, independent review, runtime conformance, and canonical architecture approval.

No canonical promotion, overall project PASS, merge, or architecture lock is authorized by this record.
