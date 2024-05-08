#!/usr/bin/python3
    """
    subreddit (str): The name of the subreddit.
    """
import requests


def number_of_subscribers(subreddit):
    """
    return number of subscribers
    """
    url = f"https://www.reddit.com/r/{}/about.json"
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    response = requests.get(url, headers=headers).json()
    subscribers = response.get('data', {}).get('subscribers')
    if not subscribers:
        return 0

    return subscribers

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
