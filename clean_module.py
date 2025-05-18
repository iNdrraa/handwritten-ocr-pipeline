# clean_module.py
import re

def clean_text(text):
    # Replace line breaks with space
    text = text.replace('\n', ' ')
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove unwanted characters but keep punctuation and brackets
    text = re.sub(r'[^A-Za-z0-9.,;:\-\'\"()\[\]\s]', '', text)
    return text.strip()