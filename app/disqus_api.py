import requests
from .config import DISQUS_API_KEY, DISQUS_FORUM

BASE_URL = "https://disqus.com/api/3.0"

def get_latest_comments(limit=10):
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
    return data["response"]


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
