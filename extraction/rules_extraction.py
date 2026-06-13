import json

input_path = "data/cleaned_text/RBI_IT_Outsourcing_2023_cleaned.txt"
output_path = "extraction/rbi_it_rules.json"

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

sentences = text.split(".")

keywords = ["shall", "must", "required to"]

def categorize_rule(sentence):
    s = sentence.lower()
    if "vendor" in s or "service provider" in s:
        return "Vendor Risk Management"
    if "audit" in s or "inspection" in s:
        return "Audit & Compliance"
    if "data" in s or "information security" in s:
        return "Data Security"
    if "business continuity" in s or "disaster" in s:
        return "Business Continuity"
    return "Governance"

rules = []

for s in sentences:
    for k in keywords:
        if k in s.lower():
            rules.append({
                "regulation": "RBI IT Outsourcing 2023",
                "category": categorize_rule(s),
                "text": s.strip()
            })
            break

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(rules, f, indent=2)

print("Categorized rules saved:", len(rules))
