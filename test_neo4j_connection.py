from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "neo4j123"

driver = GraphDatabase.driver(
    URI,
    auth=(USER, PASSWORD)
)

with driver.session() as session:
    result = session.run("RETURN 1 AS ok")
    print(result.single()["ok"])

driver.close()
