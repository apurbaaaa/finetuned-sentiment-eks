from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
nlp = pipeline("sentiment-analysis", model="./sentiment_model")

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(inp: InputText):
    return nlp(inp.text)
