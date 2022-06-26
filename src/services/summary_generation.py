"""
This file is used to generate the summary from input text.
"""
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import logging


try:
    tokenizer = AutoTokenizer.from_pretrained("src/resources/summary_token")
    model = AutoModelForSeq2SeqLM.from_pretrained("src/resources/summary_model")
    classifier = pipeline("summarization", model=model, tokenizer=tokenizer)
    logging.warning("summary model loaded")

except Exception as e:
    tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
    tokenizer.save_pretrained('src/resources/summary_token')
    model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
    model.save_pretrained('src/resources/summary_model')
    classifier = pipeline("summarization", model=model, tokenizer=tokenizer)
    logging.warning("downloaded summary model loaded")


def generate_summary(text):
    global classifier
    return classifier(text)

