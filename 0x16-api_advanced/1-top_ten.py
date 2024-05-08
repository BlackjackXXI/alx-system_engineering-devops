import requests


def top_ten(subreddit):
    """
    Query Reddit API for titles of top ten posts of a given subreddit.
    
    Args:
    subreddit (str): The name of the subreddit.
    
    Returns:
    None. Prints the top ten titles for the subreddit. Returns None if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid errors (details in link provided)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers).json()
    top_ten_posts = response.get('data', {}).get('children', [])

    # If no top posts are found, print None and return
    if not top_ten_posts:
        print(None)
        return

    # Print the titles of the top ten posts
    for post in top_ten_posts:
        print(post.get('data').get('title'))

# Example usage:
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
