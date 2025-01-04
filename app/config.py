import os
from dotenv import load_dotenv

load_dotenv()

DISQUS_ACCESS_TOKEN = os.getenv("DISQUS_ACCESS_TOKEN")
DISQUS_API_KEY = os.getenv("DISQUS_API_KEY")
DISQUS_FORUM = os.getenv("DISQUS_FORUM")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DEFAULT_MODEL = "gpt-4o"
TRIGGER_KEYWORD = "@ChatGPT"
