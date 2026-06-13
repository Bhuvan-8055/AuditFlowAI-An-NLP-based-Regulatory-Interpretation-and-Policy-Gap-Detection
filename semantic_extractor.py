def extract_semantic_signals(text: str):
    t = text.lower()

    signals = {
        "it_outsourcing": any(x in t for x in [
            "outsourced", "third party", "vendor", "external provider"
        ]),

        "audit_mentioned": any(x in t for x in [
            "audit", "review", "assessment", "inspection"
        ]),

        "personal_data": any(x in t for x in [
            "personal data", "customer data", "user data", "pii"
        ]),

        "consent_mentioned": any(x in t for x in [
            "consent", "permission", "approval"
        ]),

        "retention_mentioned": any(x in t for x in [
            "retention", "storage period", "data deletion"
        ]),

        "purpose_mentioned": any(x in t for x in [
            "purpose", "intended use", "processing purpose"
        ]),

        "notice_mentioned": any(x in t for x in [
            "notice", "privacy notice", "informed"
        ])
    }

    confidence = 0.9 if any(signals.values()) else 0.4

    return {
        "signals": signals,
        "confidence": confidence
    }
