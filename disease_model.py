from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
disease_labels = ["diabetes", "asthma", "hypertension", "flu", "arthritis"]

def detect_disease(text):
    result = classifier(text, disease_labels)
    return result['labels'][0]
