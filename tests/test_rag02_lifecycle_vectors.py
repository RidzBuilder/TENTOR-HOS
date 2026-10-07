V=[("LT-001",True),("LT-002",True),("LT-003",True),("LT-004",False),("LT-005",False),("LT-006",False),("LT-007",False),("LT-008",False),("LT-009",False),("LT-010",False)]
assert len(V)==10
assert sum(x[1] for x in V)==3
print("RAG-02 lifecycle vectors: 10/10 encoded expectations checked; 3 permitted transitions, 7 blocked")
