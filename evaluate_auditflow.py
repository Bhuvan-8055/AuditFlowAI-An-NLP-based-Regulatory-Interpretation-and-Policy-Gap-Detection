import json
from collections import Counter
from sklearn.metrics import f1_score
import pandas as pd
import re

with open("data/eval/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

n = len(data)

y_true = [x["ground_truth_conflict"] for x in data]

y_naive = [
    1 if "conflict" in x["naive_rag_answer"].lower() or "violation" in x["naive_rag_answer"].lower() else 0
    for x in data
]

y_audit = [
    1 if x.get("auditflow_clause") not in [None, "", "NA"] else 0
    for x in data
]

f1_naive = f1_score(y_true, y_naive)
f1_audit = f1_score(y_true, y_audit)

trace_naive = (
    sum(
        1 for x in data
        if "section" in x["naive_rag_answer"].lower()
        or "clause" in x["naive_rag_answer"].lower()
    ) / n * 100
)

trace_audit = (
    sum(1 for x in data if x.get("auditflow_clause")) / n * 100
)

def consistency_score(path):
    with open(path, "r", encoding="utf-8") as f:
        runs = json.load(f)
    answers = [x["answer"] for x in runs]
    return Counter(answers).most_common(1)[0][1] / len(answers)

cons_naive = consistency_score("data/eval/consistency_naive.json")
cons_audit = consistency_score("data/eval/consistency_auditflow.json")

def tokenize(text):
    return set(re.findall(r"\b\w+\b", text.lower()))

def faithfulness_overlap(answer, context):
    a = tokenize(answer)
    c = tokenize(context)
    if not a:
        return 0.0
    return len(a & c) / len(a)

faith_naive = sum(
    faithfulness_overlap(x["naive_rag_answer"], x["context"]) for x in data
) / n

faith_audit = sum(
    faithfulness_overlap(x["auditflow_answer"], x["context"]) for x in data
) / n

results = pd.DataFrame({
    "Metric": [
        "Faithfulness (Context Overlap)",
        "Conflict F1-Score",
        "Traceability Coverage (%)",
        "Consistency Score"
    ],
    "Naive RAG": [
        round(faith_naive, 3),
        round(f1_naive, 3),
        round(trace_naive, 1),
        round(cons_naive, 3)
    ],
    "AuditFlow AI": [
        round(faith_audit, 3),
        round(f1_audit, 3),
        round(trace_audit, 1),
        round(cons_audit, 3)
    ]
})

results.to_csv("journal_results.csv", index=False)
print(results)
