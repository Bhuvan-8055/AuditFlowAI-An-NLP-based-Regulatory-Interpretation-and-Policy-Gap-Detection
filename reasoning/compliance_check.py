from neo4j import GraphDatabase
from llm.policy_parser import extract_policy_facts
from classifier.predict_risk import predict_risk

uri = "neo4j://127.0.0.1:7687"
username = "neo4j"
password = "neo4j123"

CONFIDENCE_THRESHOLD = 0.85

driver = GraphDatabase.driver(uri, auth=(username, password))


def check_compliance(policy_text: str):
    print("\nINPUT POLICY:")
    print(policy_text)

    # 1. LLM extraction
    facts = extract_policy_facts(policy_text)
    print("\nLLAMA FACTS:")
    print(facts)

    llama_conf = facts.get("confidence", 0.0)

    # 2. Classifier prediction
    risk_pred = predict_risk(policy_text)
    print("\nCLASSIFIER RISK:")
    print(risk_pred)

    # 3. Confidence gate
    if llama_conf < CONFIDENCE_THRESHOLD and not any(v == 1 for v in risk_pred.values()):
        print("\n⚠️ RESULT: INSUFFICIENT CONFIDENCE")
        return

    # 4. Check if audit is missing (IMPORTANT FIX)
    audit_missing = any(
        "audit" in str(c).lower()
        for c in facts.get("missing_controls", [])
    )

    classifier_audit = risk_pred.get("audit") == 1

    with driver.session() as session:
        violations = []

        if audit_missing or classifier_audit:
            result = session.run(
                """
                MATCH (rule:Rule)-[:BELONGS_TO]->(:Category {name: "Audit & Compliance"})
                RETURN rule.text
                """
            )
            for r in result:
                violations.append(r["rule.text"])

        if violations:
            print("\n❌ RESULT: NON-COMPLIANT")
            print("Violated RBI Rules:")
            for v in violations:
                print("-", v)
        else:
            print("\n✅ RESULT: COMPLIANT")


if __name__ == "__main__":
    test_policies = [
        "The company may outsource IT services without conducting audits.",
        "We follow industry best practices.",
        "All vendors are audited annually as per RBI IT outsourcing guidelines."
    ]

    for policy in test_policies:
        check_compliance(policy)

    driver.close()
