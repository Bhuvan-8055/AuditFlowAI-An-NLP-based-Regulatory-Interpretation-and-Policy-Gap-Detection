DPDP_RULES = [
    {
        "id": "DPDP-NOTICE",
        "trigger": ["collect", "process", "store"],
        "missing": ["notice"],
        "control_id": "CTRL-DPDP-NOTICE",
        "severity": "HIGH",
        "description": "Personal data processed without providing statutory notice."
    },
    {
        "id": "DPDP-CONSENT",
        "trigger": ["share", "transfer", "disclose"],
        "missing": ["consent"],
        "control_id": "CTRL-DPDP-CONSENT",
        "severity": "HIGH",
        "description": "Personal data shared without valid consent."
    },
    {
        "id": "DPDP-PURPOSE",
        "trigger": ["reuse", "repurpose"],
        "missing": ["purpose"],
        "control_id": "CTRL-DPDP-PURPOSE",
        "severity": "MEDIUM",
        "description": "Purpose limitation violated under DPDP Act."
    },
    {
        "id": "DPDP-RETENTION",
        "trigger": ["retain", "store indefinitely"],
        "missing": ["retention"],
        "control_id": "CTRL-DPDP-RETENTION",
        "severity": "MEDIUM",
        "description": "Data retained beyond lawful retention period."
    },
    {
        "id": "DPDP-RIGHTS",
        "trigger": ["deny access", "ignore request"],
        "missing": ["rights"],
        "control_id": "CTRL-DPDP-RIGHTS",
        "severity": "HIGH",
        "description": "Data Principal rights not honoured."
    }
]
