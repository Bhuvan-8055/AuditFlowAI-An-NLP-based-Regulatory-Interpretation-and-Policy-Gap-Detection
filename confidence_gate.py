CONFIDENCE_THRESHOLD = 0.75


def gate_facts(facts):
    """
    facts: dict[str, float]
    Example:
        {
          "IT_OUTSOURCING_WITHOUT_AUDIT": 0.92,
          "DATA_SHARED_WITHOUT_CONSENT": 0.40
        }
    """

    gated = {}

    for fact, confidence in facts.items():
        if confidence >= CONFIDENCE_THRESHOLD:
            gated[fact] = confidence

    return gated
