from fastapi import FastAPI
from pydantic import BaseModel
import json
from disease_model import detect_disease
import os
import uvicorn

app = FastAPI()

with open("diseases_meds.json") as f:
    disease_db = json.load(f)

class SymptomInput(BaseModel):
    symptoms: str

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

# ✅ This part is needed to bind the correct port on Render
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)