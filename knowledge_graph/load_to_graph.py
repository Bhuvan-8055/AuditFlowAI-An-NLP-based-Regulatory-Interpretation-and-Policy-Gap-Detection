from neo4j import GraphDatabase
import json

uri = "neo4j://127.0.0.1:7687"
username = "neo4j"
password = "neo4j123"

with open("extraction/rbi_it_rules.json", "r", encoding="utf-8") as f:
    rules = json.load(f)

driver = GraphDatabase.driver(uri, auth=(username, password))

with driver.session() as session:
    session.run(
        "MERGE (:Regulation {name: 'RBI IT Outsourcing 2023'})"
    )

    for r in rules:
        session.run(
            """
            MATCH (reg:Regulation {name: $reg_name})
            MERGE (cat:Category {name: $category})
            CREATE (rule:Rule {text: $text})
            CREATE (reg)-[:HAS_RULE]->(rule)
            CREATE (rule)-[:BELONGS_TO]->(cat)
            """,
            reg_name=r["regulation"],
            category=r["category"],
            text=r["text"]
        )

driver.close()

print("All rules loaded into Neo4j")
