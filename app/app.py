import sys
import os
import streamlit as st

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from compliance_checker import run_compliance_check

st.set_page_config(
    page_title="AuditFlow AI – Regulatory Compliance Checker",
    layout="centered"
)

st.title("AuditFlow AI – Regulatory Compliance Checker")

policy_text = st.text_area(
    "Enter policy / document text",
    height=200,
    placeholder="Paste bank policy, SOP, or compliance document text here..."
)

if st.button("Run Compliance Check"):
    if not policy_text.strip():
        st.warning("Please enter some policy text.")
    else:
        result = run_compliance_check(policy_text)

        if result["status"] == "COMPLIANT":
            st.success("✅ COMPLIANT — No violations found")
        else:
            st.error("❌ NON-COMPLIANT — Violations detected")

            for i, v in enumerate(result["violations"], start=1):
                st.markdown(f"""
**Violation {i}**
- **Control ID:** {v["control_id"]}
- **Severity:** {v["severity"]}
- **Description:** {v["description"]}
""")
