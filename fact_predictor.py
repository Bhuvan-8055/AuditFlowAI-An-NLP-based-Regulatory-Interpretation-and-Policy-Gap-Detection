def predict_facts(signals):
    facts = {}

    # RBI IT Outsourcing
    facts["IT_OUTSOURCING_PRESENT"] = 0.9 if signals.get("it_outsourcing") else 0.1

    facts["IT_OUTSOURCING_WITHOUT_AUDIT"] = (
        0.92
        if signals.get("it_outsourcing") and not signals.get("audit_mentioned")
        else 0.1
    )

    facts["VENDOR_USED"] = 0.85 if signals.get("it_outsourcing") else 0.1

    facts["NO_VENDOR_RISK_ASSESSMENT"] = (
        0.88
        if signals.get("it_outsourcing") and not signals.get("audit_mentioned")
        else 0.2
    )

    # DPDP Act
    facts["PERSONAL_DATA_PROCESSED"] = (
        0.9 if signals.get("personal_data") else 0.1
    )

    facts["DATA_SHARED_WITHOUT_CONSENT"] = (
        0.93
        if signals.get("personal_data") and not signals.get("consent_mentioned")
        else 0.1
    )

    facts["CONSENT_PRESENT"] = (
        0.9
        if signals.get("personal_data") and signals.get("consent_mentioned")
        else 0.1
    )

    facts["NO_DATA_RETENTION_POLICY"] = (
        0.85
        if signals.get("personal_data") and not signals.get("retention_mentioned")
        else 0.1
    )

    facts["PURPOSE_LIMITATION_VIOLATION"] = (
        0.8
        if signals.get("personal_data") and not signals.get("purpose_mentioned")
        else 0.1
    )

    facts["NOTICE_NOT_PROVIDED"] = (
        0.82
        if signals.get("personal_data") and not signals.get("notice_mentioned")
        else 0.1
    )

    return facts
