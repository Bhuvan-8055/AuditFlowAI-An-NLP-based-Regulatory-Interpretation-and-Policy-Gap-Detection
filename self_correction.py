from neural_parser import parse_policy

def self_correct(policy_text, rejected_facts):
    """
    Re-run neural parsing with stricter assumptions
    if confidence was low earlier
    """

    if not rejected_facts:
        return []

    corrected_facts = []

    # stricter re-interpretation
    refined_text = (
        "Interpret strictly under Indian banking compliance law.\n"
        + policy_text
    )

    reparsed = parse_policy(refined_text)

    for fact in reparsed:
        if fact.get("confidence", 0) >= 0.75:
            corrected_facts.append(fact)

    return corrected_facts
