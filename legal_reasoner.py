from compliance_checker import run_compliance_check

def generate_audit_report(policy_text):
    result = run_compliance_check(policy_text)

    if not result["violations"]:
        return {
            "status": "COMPLIANT",
            "message": "No regulatory violations detected."
        }

    return {
        "status": "NON-COMPLIANT",
        "accepted_facts": result["accepted_facts"],
        "violations": result["violations"]
    }
