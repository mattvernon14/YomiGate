import requests

LMSTUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL = "qwen2.5-vl-7b-instruct"

def llm_available():
    try:
        r = requests.get("http://localhost:1234/v1/models", timeout=1)
        return r.status_code == 200
    except Exception:
        return False
def generate_sentence(level, kanji, hiragana, english):
    
    llm_prompt = (
f"Write a single sentence in Japanese that uses JLPT {level} words/structure. " 
f"Use kanji for the words when available. Avoid any explanations of the sentence.\n" 
f"Kanji: {kanji}\n"
f"Hiragana: {hiragana}\n"
f"Meaning: {english}\n")
    
    try:
        response = requests.post(
        LMSTUDIO_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "user", "content": llm_prompt}
            ],
            "temperature": 0.7
        },
        timeout = 60
        )
        data = response.json()["choices"][0]["message"]["content"].strip()
        return data
    except requests.exceptions.RequestException:
        return None