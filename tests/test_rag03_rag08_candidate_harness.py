CASES={
"RAG-03-provider-swap":["same capability contract","provider identity changes","semantic contract remains stable"],
"RAG-04-authorization":["authorized invocation","missing consent denied","withdrawn consent denied"],
"RAG-05-recovery":["restore does not invoke provider","history remains immutable","replay is explicit"],
"RAG-06-typed-results":["EXACT","PARTIAL","FALLBACK","FAILURE","DENIED","UNKNOWN"],
"RAG-07-domain-boundary":["domain A mapping","domain B mapping","domain C mapping","negative non-mappable case"],
"RAG-08-e2e-provenance":["runtime job identity","adapter/provider trace","input/output hashes","target artifact validation"]}

for name,controls in CASES.items():
    assert controls
    assert len(controls)>=3
print("RAG-03..08 candidate harness contracts encoded: 6/6; runtime execution remains NOT_RUN")
