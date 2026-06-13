from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "neo4j123"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def get_neo4j_driver():
    return driver
