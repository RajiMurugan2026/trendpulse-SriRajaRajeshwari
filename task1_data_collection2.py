import requests
import time
import os
import json
from datetime import datetime

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "book", "show", "award", "streaming"]
}

def fetch_ids():
    try:
        r = requests.get(TOP_STORIES_URL, headers=headers)
        r.raise_for_status()
        return r.json()[:500]
    except:
        return []

def fetch_story(story_id):
    try:
        r = requests.get(ITEM_URL.format(story_id), headers=headers)
        r.raise_for_status()
        return r.json()
    except:
        return None

def categorize(title):
    title = title.lower()

    for cat, words in categories.items():
        for w in words:
            if w in title:
                return cat

    return "technology"  # fallback

def main():
    print("Starting TrendPulse Task 1...")

    ids = fetch_ids()

    results = []

    for story_id in ids:

        # 🔥 IMPORTANT FIX: stop based on TOTAL not categories
        if len(results) >= 120:
            break

        story = fetch_story(story_id)
        if not story:
            continue

        title = story.get("title", "")
        category = categorize(title)

        record = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        results.append(record)

    # save folder
    os.makedirs("data", exist_ok=True)

    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

    print(f"\nCollected {len(results)} stories.")
    print(f"Saved to {filename}")

if __name__ == "__main__":
    main()

