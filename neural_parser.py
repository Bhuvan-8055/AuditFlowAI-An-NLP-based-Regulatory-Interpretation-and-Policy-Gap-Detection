def parse_policy(text):
    """
    Simulated neural parser output.
    Later this can be replaced by actual LLM inference.
    """

    parsed_facts = []

    if "outsourc" in text.lower() and "audit" in text.lower():
        parsed_facts.append({
            "fact": "IT_OUTSOURCING_WITHOUT_AUDIT",
            "confidence": 0.92
        })

    if "data" in text.lower() and "consent" in text.lower():
        parsed_facts.append({
            "fact": "DATA_SHARED_WITH_CONSENT",
            "confidence": 0.85
        })

    return parsed_facts
