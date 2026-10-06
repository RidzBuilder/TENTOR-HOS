import json, pathlib, copy
from jsonschema import Draft202012Validator
ROOT=pathlib.Path(__file__).resolve().parents[1]
schema=json.loads((ROOT/"schemas/candidate/requirement-evidence-link-v0.1.schema.json").read_text())
v=Draft202012Validator(schema)
base=json.loads((ROOT/"tests/fixtures/candidate-requirement-evidence-link-fixtures-v0.1.json").read_text())[0]
cases=[]
x=copy.deepcopy(base); x.pop("evidence_refs"); cases.append(x)
x=copy.deepcopy(base); x["aggregation_result"]="TESTED"; cases.append(x)
x=copy.deepcopy(base); x["requirement_id"]="REQ-99"; cases.append(x)
for i,c in enumerate(cases,1):
    if not list(v.iter_errors(c)): raise AssertionError(f"negative control {i} unexpectedly valid")
print("RAG-01 negative controls: 3/3 rejected")
