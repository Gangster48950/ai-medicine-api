from transformers import pipeline

# Lazy-load model
classifier = None

# Define supported disease labels
disease_labels = [
    "diabetes",
    "asthma",
    "hypertension",
    "flu",
    "arthritis",
    "migraine",
    "covid-19",
    "tuberculosis",
    "dengue",
    "malaria"
]

def detect_disease(text):
    global classifier
    if classifier is None:
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    result = classifier(text, disease_labels)
    return result["labels"][0]
