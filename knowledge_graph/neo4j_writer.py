# knowledge_graph/neo4j_writer.py

from neo4j import GraphDatabase
import uuid

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "neo4j123"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def write_violation(policy_name, control_id, control_name, severity, description):
    violation_id = str(uuid.uuid4())

    with driver.session() as session:
        session.run(
            """
            MERGE (c:Control {id: $control_id})
            ON CREATE SET c.name = $control_name

            CREATE (v:Violation {
                id: $violation_id,
                policy: $policy_name,
                severity: $severity,
                description: $description
            })

            MERGE (v)-[:VIOLATES]->(c)
            """,
            violation_id=violation_id,
            policy_name=policy_name,
            control_id=control_id,
            control_name=control_name,
            severity=severity,
            description=description
        )

def close_driver():
    driver.close()
