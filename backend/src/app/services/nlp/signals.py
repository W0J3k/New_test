import re
from statistics import mean


def credibility_signals(text: str) -> float:
    if not text:
        return 0.0
    caps_ratio = sum(1 for c in text if c.isupper()) / len(text)
    emoji_ratio = len(re.findall(r"[\U0001F600-\U0001F64F]", text)) / max(len(text), 1)
    return 1.0 - mean([caps_ratio, emoji_ratio])
