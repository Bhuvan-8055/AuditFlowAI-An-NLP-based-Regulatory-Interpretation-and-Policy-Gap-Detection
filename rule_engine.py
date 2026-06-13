CONFIDENCE_THRESHOLD = 0.7


DPDP_RULES = {
    "CTRL-DPDP-CONSENT": {
        "trigger": "DATA_SHARED_WITHOUT_CONSENT",
        "severity": "HIGH",
        "description": "Personal data was shared without explicit user consent, violating the DPDP Act."
    },
    "CTRL-DPDP-NOTICE": {
        "trigger": "NOTICE_NOT_PROVIDED",
        "severity": "MEDIUM",
        "description": "Data principals were not provided with a valid notice before data processing."
    },
    "CTRL-DPDP-RETENTION": {
        "trigger": "NO_DATA_RETENTION_POLICY",
        "severity": "MEDIUM",
        "description": "No data retention or deletion policy was specified, violating DPDP storage limitation."
    },
    "CTRL-DPDP-PURPOSE": {
        "trigger": "PURPOSE_LIMITATION_VIOLATION",
        "severity": "MEDIUM",
        "description": "Personal data was processed without a clearly defined lawful purpose."
    }
}


RBI_RULES = {
    "CTRL-IT-AUDIT": {
        "trigger": "IT_OUTSOURCING_WITHOUT_AUDIT",
        "severity": "HIGH",
        "description": "IT services were outsourced without conducting mandatory vendor audits."
    }
}


def evaluate_policy(facts):
    violations = []

    all_rules = {**RBI_RULES, **DPDP_RULES}

    for control_id, rule in all_rules.items():
        trigger = rule["trigger"]

        if facts.get(trigger, 0) >= CONFIDENCE_THRESHOLD:
            violations.append({
                "control_id": control_id,
                "severity": rule["severity"],
                "description": rule["description"],
                "confidence": facts[trigger]
            })

    return violations
