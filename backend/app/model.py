import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "models" / "sentiment_model.pkl"

model = joblib.load(MODEL_PATH)

def predict_sentiment(text: str):
    prediction = model.predict([text])[0]
    return prediction
