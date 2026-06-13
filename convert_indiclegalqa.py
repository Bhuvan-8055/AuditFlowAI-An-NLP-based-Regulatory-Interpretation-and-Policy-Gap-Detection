import json

inp = "IndicLegalQA Dataset_10K_Revised.json"
out = "indiclegalqa_instruction.jsonl"

data = json.load(open(inp, "r", encoding="utf-8"))

with open(out, "w", encoding="utf-8") as f:
    for x in data:
        item = {
            "instruction": "Answer the legal question clearly and precisely.",
            "input": x["question"],
            "output": x["answer"]
        }
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print("DONE")
