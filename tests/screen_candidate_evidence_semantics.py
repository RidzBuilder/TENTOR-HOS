#!/usr/bin/env python3
"""Candidate semantic screening for synthetic evidence records.

This is a conservative prototype, not the normative gate aggregator and not a
validator of truth/authenticity. It applies only local, explicit screening rules.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES_PATH = ROOT / "tests/fixtures/candidate-evidence-record-fixtures-v0.1.json"\nSCHEMA_PATH = ROOT / "schemas/candidate/evidence-record-v0.1.schema.json"


def disposition(record, validator):
    """Return a conservative screening disposition, never a requirement PASS."""
    if not isinstance(record, dict):
        return "REJECT"
    if record.get("record_status") in {"REVOKED", "SUPERSEDED", "QUARANTINED"}:
        return "QUARANTINE_OR_LIMITED"
    provenance = record.get("provenance") or {}
    source_type = provenance.get("source_type")
    integrity = provenance.get("integrity_status")
    result = record.get("result")
    evidence_class = record.get("evidence_class")

    if integrity == "FAILED":
        return "REJECT"
    if result == "BLOCKED":
        return "BLOCKED_NOT_PASS"
    if source_type == "SYNTHETIC_FIXTURE":
        return "ELIGIBLE_FOR_SCOPED_REVIEW_ONLY"
    if integrity != "VERIFIED":
        return "QUARANTINE_OR_LIMITED"
    if evidence_class in {"TEST_PLAN", "SOURCE_DECLARATION"}:
        return "INSUFFICIENT_FOR_EXECUTION_CLAIM"
    if evidence_class == "EXTERNAL_PROVIDER_ARTIFACT":
        return "QUARANTINE_OR_LIMITED"
    if record.get("review", {}).get("review_status") != "INDEPENDENTLY_REVIEWED":
        return "ELIGIBLE_FOR_SCOPED_REVIEW_ONLY"
    return "ELIGIBLE_FOR_SCOPED_REVIEW_ONLY"


def main():
    fixture_set = json.loads(FIXTURES_PATH.read_text(encoding="utf-8"))
    cases = fixture_set.get("cases", [])
    failures = []
    for case in cases:
        actual = disposition(case.get("record"), validator)
        expected = case.get("expected_semantic_disposition")
        if actual != expected:
            failures.append((case.get("id"), expected, actual))
            print(f"FAIL {case.get('id')}: expected={expected}, actual={actual}")
        else:
            print(f"PASS {case.get('id')}: screening={actual}")
    print(f"\nSemantic screening summary: {len(cases)-len(failures)}/{len(cases)} expectations matched")
    print("LIMIT: synthetic fixture classification only; no authenticity, requirement satisfaction, or gate PASS is established.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
