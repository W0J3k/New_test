from typing import Dict
from playwright.sync_api import sync_playwright
from readability import Document


def fetch_page(url: str) -> Dict[str, str]:
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto(url)
        html = page.content()
        browser.close()
    doc = Document(html)
    return {"title": doc.short_title(), "content": doc.summary()}
