from . import disqus_api, openai_api
from .config import TRIGGER_KEYWORD

def run_bot_logic():
    """
    Process: Get latest comments -> Check if reply needed -> Call OpenAI -> Post reply
    """
    comments = disqus_api.get_latest_comments(limit=10)
    
    for c in comments:
        post_id = c["id"]
        author = c["author"]["username"]
        message_text = c["raw_message"]

        # Skip comments made by the bot itself to avoid self-answering
        if author == "...":
            continue
        
        # Check if the trigger keyword is present in the message
        if TRIGGER_KEYWORD in message_text:  
            reply_content = openai_api.get_chatgpt_reply(message_text)
            disqus_api.post_reply(post_id, reply_content)
