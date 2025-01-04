import openai
from .config import OPENAI_API_KEY, DEFAULT_MODEL

openai.api_key = OPENAI_API_KEY

def get_chatgpt_reply(user_text):
    """
    Get a reply from the ChatGPT model.
    """
    response = openai.ChatCompletion.create(
        model=DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": "..."},
            {"role": "user", "content": user_text}
        ],
        temperature=0.7,
        max_tokens=256,
    )
    return response.choices[0].message["content"]
