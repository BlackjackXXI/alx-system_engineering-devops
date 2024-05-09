#!/usr/bin/python3
"""
Query Reddit API recursively for all hot articles of a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Return all hot articles for a given subreddit recursively.
    Return None if an invalid subreddit is given.
    """
    # Set up the user agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # Update the URL for each recursive call with the 'after' parameter
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"

    # Make the request to Reddit API
    r = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if r.status_code != 200:
        print(f"Error: Unable to retrieve data for subreddit '{subreddit}'")
        return None

    # Extract data from the response
    data = r.json().get('data', {})
    children = data.get('children', [])

    # Append titles to hot_list
    for child in children:
        hot_list.append(child.get('data', {}).get('title'))

    # Get the 'after' parameter for the next page of results
    after = data.get('after')

    # Recurse if 'after' parameter exists, otherwise return the hot_list
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list

# Example usage:
# hot_articles = recurse("python")

# Uncomment the line above and replace "python" with your desired subreddit to test the function.
