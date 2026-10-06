import json, pathlib
from jsonschema import Draft202012Validator
R=pathlib.Path(__file__).resolve().parents[1]
s=json.loads((R/"schemas/candidate/governance-decision-record-v0.1.schema.json").read_text())
f=json.loads((R/"tests/fixtures/candidate-governance-decision-fixtures-v0.1.json").read_text())
v=Draft202012Validator(s); es=[e for x in f for e in v.iter_errors(x)]
if es: raise SystemExit("\n".join(e.message for e in es))
print(f"governance decision fixtures: {len(f)}/{len(f)} valid")
