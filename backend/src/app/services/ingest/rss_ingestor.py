import feedparser
from typing import List, Dict


def fetch_rss(url: str) -> List[Dict[str, str]]:
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries:
        items.append({"title": entry.title, "link": entry.link})
    return items
