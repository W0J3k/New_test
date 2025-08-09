from typing import List, Dict
from telethon.sync import TelegramClient


def fetch_channel_messages(
    api_id: int, api_hash: str, channel: str, limit: int = 20
) -> List[Dict[str, str]]:
    with TelegramClient("anon", api_id, api_hash) as client:
        messages = []
        for msg in client.iter_messages(channel, limit=limit):
            messages.append({"text": msg.text or "", "id": msg.id})
    return messages
