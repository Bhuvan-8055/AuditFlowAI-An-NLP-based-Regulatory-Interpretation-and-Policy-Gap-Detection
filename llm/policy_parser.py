from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
import json
import re

llm = OllamaLLM(model="llama3.1")

PROMPT = PromptTemplate(
    input_variables=["text"],
    template="""
You are a regulatory compliance extraction system.

STRICT RULES:
- Output ONLY valid JSON
- Do NOT add explanations
- Do NOT add markdown
- Do NOT add text before or after JSON
- If unsure, lower confidence
- Never guess

INPUT TEXT:
{text}

OUTPUT FORMAT (JSON ONLY):
{{
  "entities": [],
  "obligations": [],
  "missing_controls": [],
  "risk_domains": [],
  "confidence": 0.0
}}
"""
)

def safe_json_parse(text: str):
    """
    Extracts the first JSON object found in text safely.
    """
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        return {
            "entities": [],
            "obligations": [],
            "missing_controls": [],
            "risk_domains": [],
            "confidence": 0.0
        }
    return json.loads(match.group())

def extract_policy_facts(text: str):
    raw = llm.invoke(PROMPT.format(text=text))
    return safe_json_parse(raw)

if __name__ == "__main__":
    test_inputs = [
        "The company may outsource IT services without conducting audits.",
        "All vendors are audited annually and comply with RBI guidelines.",
        "We follow industry best practices."
    ]

    for t in test_inputs:
        print("\nINPUT:", t)
        print("OUTPUT:")
        print(extract_policy_facts(t))
