import json
from compliance_checker import run_compliance_check

with open("eval_dataset.json", "r", encoding="utf-8") as f:
    eval_data = json.load(f)

results = []

for sample in eval_data:
    text = sample["text"]
    gt = sample["label"]

    violations = run_compliance_check(text)
    pred = 1 if len(violations) > 0 else 0

    results.append({
        "text": text,
        "ground_truth": gt,
        "model_prediction": pred
    })

with open("eval_predictions.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Saved", len(results), "predictions")
