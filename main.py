from fastapi import FastAPI
from pydantic import BaseModel
import json
from disease_model import detect_disease
import os
import uvicorn

app = FastAPI()

# Load medicines
with open("diseases_meds.json") as f:
    disease_db = json.load(f)

# Input structure
class SymptomInput(BaseModel):
    symptoms: str

@app.get("/")
def home():
    return {"message": "AI Medicine API is running."}

@app.post("/suggest")
def suggest_medicine(data: SymptomInput):
    detected_disease = detect_disease(data.symptoms)
    medicines = disease_db.get(detected_disease.lower(), [])

    if medicines:
        return {
            "disease_detected": detected_disease,
            "suggested_medicines": medicines,
            "disclaimer": "This is an AI-generated suggestion. Please consult a licensed medical professional."
        }
    else:
        return {
            "message": "No matching condition found. Please consult a doctor.",
            "disclaimer": "This tool is for educational purposes only."
        }

# Required to run on Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
