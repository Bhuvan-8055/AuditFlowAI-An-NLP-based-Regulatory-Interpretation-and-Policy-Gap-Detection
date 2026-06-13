import json
from compliance_checker import run_compliance_check

def evaluate():
    with open("data/evaluation_scenarios.json", "r", encoding="utf-8") as f:
        scenarios = json.load(f)

    tp = fp = tn = fn = 0
    detailed_results = []

    for s in scenarios:
        result = run_compliance_check(s["policy_text"])

        predicted_violation = result["status"] == "NON_COMPLIANT"
        expected_violation = s["expected_violation"]

        if predicted_violation and expected_violation:
            tp += 1
        elif predicted_violation and not expected_violation:
            fp += 1
        elif not predicted_violation and not expected_violation:
            tn += 1
        elif not predicted_violation and expected_violation:
            fn += 1

        detailed_results.append({
            "id": s["id"],
            "expected": expected_violation,
            "predicted": predicted_violation,
            "status": result["status"]
        })

    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0

    print("=== AUDITFLOW AI EVALUATION ===")
    print(f"Total Scenarios: {len(scenarios)}")
    print(f"TP: {tp}, FP: {fp}, TN: {tn}, FN: {fn}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F1 Score: {f1:.3f}")

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1
    }

if __name__ == "__main__":
    evaluate()
