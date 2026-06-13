def resolve_conflicts(violations):
    if not violations:
        return []

    resolved = {}
    for v in violations:
        key = v["control_id"]

        if key not in resolved:
            resolved[key] = v
        else:
            if v["severity"] == "HIGH":
                resolved[key] = v

    return list(resolved.values())
