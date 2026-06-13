from knowledge_graph.neo4j_writer import write_violation

write_violation(
    policy_name="TEST POLICY",
    control_id="CTRL-TEST",
    control_name="Test Control",
    severity="HIGH",
    description="This is a forced test violation"
)
