#!/usr/bin/python3
"""
API of number of subscribers of a subreddit
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a custom User-Agent to avoid errors
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

# Example usage:
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
