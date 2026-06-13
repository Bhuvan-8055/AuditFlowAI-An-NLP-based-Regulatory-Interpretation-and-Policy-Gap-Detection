CONTROL_METADATA = {
    "CTRL-IT-AUDIT": {
        "law": "RBI Master Direction – IT Outsourcing",
        "clause": "Section 10.2",
        "page": "Page 42",
        "description": "Banks must conduct periodic vendor audits"
    },
    "CTRL-DPDP-CONSENT": {
        "law": "DPDP Act 2023",
        "clause": "Section 6",
        "page": "Page 11",
        "description": "Personal data processing requires consent"
    }
}

def attach_traceability(violations):
    enriched = []

    for v in violations:
        meta = CONTROL_METADATA.get(v["control_id"], {})

        enriched.append({
            "control_id": v["control_id"],
            "severity": v["severity"],
            "violation": v["description"],
            "law": meta.get("law", "Unknown"),
            "clause": meta.get("clause", "N/A"),
            "page": meta.get("page", "N/A")
        })

    return enriched
