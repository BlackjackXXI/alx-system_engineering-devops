#!/usr/bin/python3
"""
Script that returns top 10 hot posts of a subreddit
"""
import requests
import json
import re

def count_words(subreddit, word_list):
    # Base case: If word_list is empty, return
    if not word_list:
        return

    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    # Make the request to the Reddit API
    response = requests.get(url)
    data = response.json()

    # Extract the titles of the hot articles
    titles = [post['data']['title'] for post in data['data']['children']]

    # Initialize a dictionary to store the count of each keyword
    keyword_counts = {}

    # Iterate through the titles and count the occurrences of each keyword
    for title in titles:
        for word in word_list:
            # Normalize the word to lowercase and remove special characters
            normalized_word = re.sub(r'\W+', '', word.lower())
            # Check if the normalized word is in the title
            if normalized_word in title.lower():
                # Increment the count for the keyword
                if word in keyword_counts:
                    keyword_counts[word] += 1
                else:
                    keyword_counts[word] = 1

    # Sort the keyword_counts dictionary by count in descending order and alphabetically
    sorted_counts = sorted(keyword_counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the results
    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")

# Example usage
count_words("programming", ["python", "java", "javascript", "scala"])
