from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "neo4j123"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))


def fetch_violations():
    with driver.session() as session:
        result = session.run(
            """
            MATCH (v:Violation)-[:TRIGGERS]->(c:Control)
            RETURN v.id AS violation_id,
                   v.policy_name AS policy,
                   v.severity AS severity,
                   v.description AS description,
                   c.name AS control_name,
                   c.id AS control_id
            """
        )

        violations = []
        for record in result:
            violations.append({
                "violation_id": record["violation_id"],
                "policy": record["policy"],
                "severity": record["severity"],
                "description": record["description"],
                "control_name": record["control_name"],
                "control_id": record["control_id"]
            })

        return violations
