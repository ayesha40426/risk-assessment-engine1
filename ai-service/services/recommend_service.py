import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_PATH = os.path.join(BASE_DIR, "..", "prompts", "recommend_prompt.txt")

def build_prompt(user_text):
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    return template.replace("{input}", user_text)