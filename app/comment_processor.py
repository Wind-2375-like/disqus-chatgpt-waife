from collections import defaultdict
from datetime import datetime
from .config import MAIN_ACCOUNT, SMALL_ACCOUNT

def group_comments_for_main_and_small_account(comments):
    """
    Return a list, each element is also a list, representing a thread (conversation).
    Containing only the dialogue participated by main_account and small_account.
    
    Logic:
    1. Group by thread
    2. Remove comments that are not from the two authors [main, small]
    3. Check if the thread contains the top-level comment of main_account (parent = None)
    4. Sort the remaining comments in the thread by time and collect them
    5. Return a list of all threads that meet the conditions
    """

    main_account = MAIN_ACCOUNT   # main account
    small_account = SMALL_ACCOUNT # small account
    
    # 1) Group by thread
    thread_map = defaultdict(list)
    for c in comments:
        thread_id = c["thread"]
        thread_map[thread_id].append(c)
    
    valid_threads = []
    
    for thread_id, thread_comments in thread_map.items():
        # 2) Only keep comments from main or small account
        filtered = [
            c for c in thread_comments
            if c["author"]["username"] in (main_account, small_account)
        ]
        if not filtered:
            continue  # No comments in this thread
        
        # 3) Check if the thread contains the top-level comment of main_account
        #    Top-level comment: c['parent'] is None
        has_main_top_comment = any(
            c["author"]["username"] == main_account and c["parent"] is None
            for c in filtered
        )
        if not has_main_top_comment:
            # "conversations starting from the top-level comment of the main account"
            continue
        
        # 4) Sort by creation 
        def parse_time(c):
            return datetime.strptime(c["createdAt"], "%Y-%m-%dT%H:%M:%S")
        
        filtered.sort(key=parse_time)
        
        # 5)  Add the thread to the result
        valid_threads.append(filtered)
    
    return valid_threads