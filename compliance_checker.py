from semantic_extractor import extract_semantic_signals
from fact_predictor import predict_facts
from rule_engine import evaluate_policy
from confidence_gate import gate_facts


def run_compliance_check(policy_text):
    semantic = extract_semantic_signals(policy_text)
    facts = predict_facts(semantic["signals"])
    gated_facts = gate_facts(facts)

    violations = evaluate_policy(gated_facts)

    if not violations:
        return {
            "status": "COMPLIANT",
            "confidence": semantic["confidence"],
            "violations": []
        }

    return {
        "status": "NON-COMPLIANT",
        "confidence": semantic["confidence"],
        "violations": violations
    }
