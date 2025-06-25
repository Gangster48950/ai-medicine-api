from transformers import pipeline

classifier = None  # Lazy loaded
disease_labels = ["diabetes", "asthma", "hypertension", "flu", "arthritis"]

def detect_disease(text):
    global classifier
    if classifier is None:
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    result = classifier(text, disease_labels)
    return result['labels'][0]
