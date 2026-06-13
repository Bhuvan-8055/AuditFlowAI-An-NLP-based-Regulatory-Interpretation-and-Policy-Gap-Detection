import joblib
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "legal_risk_classifier.pkl")

model = joblib.load(MODEL_PATH)

RISK_LABELS = ["audit", "privacy", "vendor_risk", "data_security", "retention"]

def predict_risk(text: str):
    preds = model.predict([text])[0]
    return dict(zip(RISK_LABELS, preds))
