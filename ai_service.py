import time
import requests

def call_gemini(prompt, api_key):
    url = f"[https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=](https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=){api_key}"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
    for attempt in range(5):
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        time.sleep(2 ** attempt) # Exponential backoff
    return None