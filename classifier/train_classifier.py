import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv("classifier/train_data.csv")

X = df["text"]
y = df[["audit", "privacy", "vendor_risk", "data_security", "retention"]]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", OneVsRestClassifier(LogisticRegression(max_iter=1000)))
])

model.fit(X, y)

joblib.dump(model, "classifier/legal_risk_classifier.pkl")

print("✅ Classifier trained and saved")
