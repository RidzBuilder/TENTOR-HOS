#!/usr/bin/env python3
"""Run candidate evidence-record fixtures against the Draft 2020-12 schema.

Synthetic conformance harness only; this does not validate real project evidence.
"""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/candidate/evidence-record-v0.1.schema.json"
FIXTURES_PATH = ROOT / "tests/fixtures/candidate-evidence-record-fixtures-v0.1.json"


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    fixture_set = json.loads(FIXTURES_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    failures = []
    cases = fixture_set.get("cases", [])
    if not cases:
        print("FAIL: no fixture cases found")
        return 1

    for case in cases:
        case_id = case.get("id", "<missing-id>")
        expected = case.get("expected_schema_valid")
        errors = list(validator.iter_errors(case.get("record")))
        actual = not errors
        if actual != expected:
            detail = "; ".join(
                f"{'/'.join(map(str, err.absolute_path)) or '<root>'}: {err.message}"
                for err in errors[:5]
            )
            failures.append(f"{case_id}: expected valid={expected}, actual={actual}; {detail}")
            print(f"FAIL {case_id}: expected valid={expected}, actual={actual}")
            if detail:
                print(f"  {detail}")
        else:
            print(f"PASS {case_id}: schema_valid={actual}")

    print(f"\nFixture summary: {len(cases) - len(failures)}/{len(cases)} expectations matched")
    print("Note: matching fixture expectations are synthetic schema-conformance results only.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
