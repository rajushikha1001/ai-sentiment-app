from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_sentiment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Sentiment API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analysis API"}

@app.post("/predict/")
def predict(request: TextRequest):
    result = predict_sentiment(request.text)
    return {"sentiment": result}
