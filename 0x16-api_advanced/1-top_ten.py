#!/usr/bin/python3
"""
dfhjksadvfjkghdfvkjhgdfv
"""
import requests


def top_ten(subreddit):
    """
    Return top ten titles for a given subreddit.
    Return None if invalid subreddit given.
    """
    # get user agent
    # https://stackoverflow.com/questions/10606133/ -->
    # sending-user-agent-using-requests-library-in-python
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
            print("No posts found for the subreddit:", subreddit)
    except requests.HTTPError as err:
        print("HTTP error occurred:", err)
    except requests.RequestException as e:
        print("Error connecting to Reddit API:", e)
    except ValueError:
        print("Invalid JSON response from Reddit API.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <subreddit>")
    else:
        top_ten(sys.argv[1])
