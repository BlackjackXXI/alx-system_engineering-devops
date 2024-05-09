#!/usr/bin/python3
"""
dfhjksadvfjkghdfvkjhgdfv
"""
import requests


def top_ten(subreddit):


    """
    Return top ten titles for a given subreddit
    Return None if invalid subreddit given
    """
    # Set user agent
    headers = {'User-Agent': 'My User Agent 1.0'}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error: Failed to fetch data from Reddit API.")
        return None
    
    data = response.json()
    top_posts = data.get('data', {}).get('children', [])
    
    if not top_posts:
        print("No posts found.")
        return None

    for post in top_posts:
        print(post.get('data').get('title'))

# Example usage:
top_ten("python")
