#!/usr/bin/python3
import requests
import csv

"""
Module: task_02_fetch_posts.py

This module contains two functions to interact with a placeholder API.
- `fetch_and_print_posts`
fetches posts and displays their titles in the console.
- `fetch_and_save_posts`
fetches posts and writes them to a CSV file.

The module uses the `requests`
library for HTTP requests and the `csv` module for file output.

API used: https://jsonplaceholder.typicode.com/posts
"""


def fetch_and_print_posts():
    """
    Fetch posts from a placeholder API and print their titles.

    Sends a GET request to https://jsonplaceholder.typicode.com/posts.
    If the request is successful (HTTP status 200),
    it prints the title of each post.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetch posts from a placeholder API and save them into a CSV file.

    Sends a GET request to https://jsonplaceholder.typicode.com/posts.
    If the request is successful (HTTP status 200),
    it writes the ID, title, and body
    of each post into a CSV file named 'posts.csv'.
    If the request fails, prints the HTTP error status.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        with open("posts.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Id", "Title", "Body"])
            for post in response.json():
                writer.writerow([post["id"], post["title"], post["body"]])
    else:
        print("Request failed with status:", response.status_code)
