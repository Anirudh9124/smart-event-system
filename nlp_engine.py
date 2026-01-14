from transformers import pipeline
# BERT for tone detection
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
# T5 for summary
summarizer = pipeline("summarization", model="t5-small")

def process_event_context(description):
    labels = ["Urgent", "Formal", "Informal"]
    tone = classifier(description, candidate_labels=labels)['labels'][0]
    return tone
