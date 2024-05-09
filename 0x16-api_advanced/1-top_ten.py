#!/usr/bin/python3
"""
dfhjksadvfjkghdfvkjhgdfv
"""
import requests
import sys

def top_ten(subreddit):
    """
    Return top ten titles for a given subreddit.
    Return None if invalid subreddit given.
    """
    # PEP8: Adding two blank lines before function definition
    # get user agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # Raise an exception for HTTP errors
        data = r.json()
        if 'data' in data and 'children' in data['data']:
            top_posts = data['data']['children']
            for post in top_posts:
                print(post['data']['title'])
        else:
            print("Subreddit not found or no posts available.")
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred:", err)
    except requests.exceptions.RequestException as e:
        print("Error connecting to Reddit API:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <subreddit>")
    else:
        top_ten(sys.argv[1])
