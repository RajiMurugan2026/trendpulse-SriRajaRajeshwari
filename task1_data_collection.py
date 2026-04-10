import requests
import time
import os
import json
from datetime import datetime

# API endpoints
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Header
headers = {"User-Agent": "TrendPulse/1.0"}

# Category keywords (case-insensitive)
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship","match"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming","tv"],
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm", "app", "startup", "internet"],

}

def fetch_top_story_ids():
    """Fetch first 500 top story IDs"""
    try:
        response = requests.get(TOP_STORIES_URL, headers=headers)
        response.raise_for_status()
        return response.json()[:500]
    except Exception as e:
        print(f"Error fetching top stories: {e}")
        return []

def fetch_story(story_id):
    """Fetch single story details"""
    try:
        response = requests.get(ITEM_URL.format(story_id), headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch story {story_id}: {e}")
        return None

def categorize(title):
    """Assign category based on keywords"""
    title = title.lower()
    
    for category, keywords in categories.items():
        if any(keyword in title for keyword in keywords):
            return category
        return "technology"

def main():
    
    print("Script started...")
    story_ids = fetch_top_story_ids()

    collected = []
    counts = {cat: 0 for cat in categories}

    for story_id in story_ids:
        # Stop early if all categories filled
        print(f"Fetching story {story_id}")
        if all(count == 25 for count in counts.values()):
            break

        story = fetch_story(story_id)
        if not story:
            continue

        title = story.get("title", "")
        category = categorize(title)

        # Skip if no category match
       # if not category:
        #    continue
        if category not in categories:
             continue

        # Skip if category already full
        if counts[category] >= 25:
            continue

        # Extract required fields
        data = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collected.append(data)
        counts[category] += 1

    # Sleep between category processing (as per instruction)
    for _ in categories:
        time.sleep(2)

    # Create folder
    os.makedirs("data", exist_ok=True)

    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    # Save file
    with open(filename, "w") as f:
        json.dump(collected, f, indent=4)

    print(f"Collected {len(collected)} stories.")
    print(f"Saved to {filename}")


if __name__ == "__main__":
    main()
