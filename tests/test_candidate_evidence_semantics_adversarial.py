#!/usr/bin/env python3
"""Adversarial unit tests for candidate semantic screening; synthetic only."""
import copy
import json
import runpy
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
schema = json.loads((ROOT / "schemas/candidate/evidence-record-v0.1.schema.json").read_text())
validator = Draft202012Validator(schema, format_checker=FormatChecker())
fixture_set = json.loads((ROOT / "tests/fixtures/candidate-evidence-record-fixtures-v0.1.json").read_text())
screen = runpy.run_path(str(ROOT / "tests/screen_candidate_evidence_semantics.py"))
disposition = screen["disposition"]
base = copy.deepcopy(fixture_set["cases"][0]["record"])

def check(name, record, expected):
    actual = disposition(record, validator)
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected}, got {actual}")
    print(f"PASS {name}: {actual}")

check("baseline synthetic remains review-only", base, "ELIGIBLE_FOR_SCOPED_REVIEW_ONLY")
r = copy.deepcopy(base); r["record_status"] = "REVOKED"
check("revoked record quarantined", r, "QUARANTINE_OR_LIMITED")
r = copy.deepcopy(base); r["result"] = "BLOCKED"
check("blocked record never passes", r, "BLOCKED_NOT_PASS")
r = copy.deepcopy(base); r["provenance"]["integrity_status"] = "FAILED"
check("failed integrity rejected", r, "REJECT")
r = copy.deepcopy(base); r["provenance"]["source_type"] = "EXTERNAL_CAPTURE"; r["provenance"]["integrity_status"] = "UNVERIFIED"
check("unverified external evidence limited", r, "QUARANTINE_OR_LIMITED")
r = copy.deepcopy(base); r["evidence_class"] = "TEST_PLAN"; r["provenance"]["source_type"] = "EXTERNAL_CAPTURE"; r["provenance"]["integrity_status"] = "VERIFIED"
check("test plan insufficient for execution", r, "INSUFFICIENT_FOR_EXECUTION_CLAIM")
r = copy.deepcopy(base); r["evidence_class"] = "EXTERNAL_PROVIDER_ARTIFACT"; r["provenance"]["source_type"] = "EXTERNAL_CAPTURE"; r["provenance"]["integrity_status"] = "VERIFIED"
check("provider artifact scope limited", r, "QUARANTINE_OR_LIMITED")
r = copy.deepcopy(base); r["unexpected"] = True
check("schema-invalid extra property rejected", r, "REJECT")
print("Adversarial semantic screening: 8/8 synthetic expectations passed.")
print("LIMIT: does not prove evidence authenticity, requirement satisfaction, or gate conformance.")
