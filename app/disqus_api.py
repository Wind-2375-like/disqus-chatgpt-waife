import requests
from .config import DISQUS_API_KEY, DISQUS_FORUM
from .comment_processor import group_comments_for_main_and_small_account

BASE_URL = "https://disqus.com/api/3.0"

def get_latest_comments(limit=100):
    """
    Collects the latest comments from the Disqus forum.
    """
    endpoint = f"{BASE_URL}/forums/listPosts.json"
    params = {
        "api_key": DISQUS_API_KEY,
        "forum": DISQUS_FORUM,
        "limit": limit,
        "order": "desc"
    }
    resp = requests.get(endpoint, params=params)
    resp.raise_for_status()
    data = resp.json()
    return group_comments_for_main_and_small_account(data["response"])


def post_reply(parent_post_id, message):
    """
    Posts a reply to a comment on the Disqus forum.
    """
    endpoint = f"{BASE_URL}/posts/create.json"
    params = {
        "api_key": DISQUS_API_KEY,
        "parent": parent_post_id,
        "message": message
    }
    resp = requests.post(endpoint, params=params)
    resp.raise_for_status()
    return resp.json()
