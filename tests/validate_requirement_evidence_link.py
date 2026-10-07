import json, pathlib
from jsonschema import Draft202012Validator
ROOT=pathlib.Path(__file__).resolve().parents[1]
schema=json.loads((ROOT/"schemas/candidate/requirement-evidence-link-v0.1.schema.json").read_text())
fixtures=json.loads((ROOT/"tests/fixtures/candidate-requirement-evidence-link-fixtures-v0.1.json").read_text())
v=Draft202012Validator(schema)
errors=[e for f in fixtures for e in v.iter_errors(f)]
if errors:
    for e in errors: print(e.message)
    raise SystemExit(1)
print(f"requirement-evidence linkage: {len(fixtures)}/{len(fixtures)} fixtures valid")
