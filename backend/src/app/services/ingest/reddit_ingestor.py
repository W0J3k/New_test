from typing import List, Dict
import praw


def fetch_subreddit(subreddit: str, limit: int = 5) -> List[Dict[str, str]]:
    reddit = praw.Reddit(
        client_id="dummy", client_secret="dummy", user_agent="myinfo"
    )
    posts = []
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        posts.append({"title": submission.title, "url": submission.url})
    return posts
