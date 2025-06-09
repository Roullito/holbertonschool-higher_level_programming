import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        for post in response.json():
            print(post["title"])
    print(response.status_code)

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        with open("posts.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Id", "Title", "Body"])
            for post in response.json():
                writer.writerow([post["id"], post["title"], post["body"]])
    else:
        print("Request failed with status:", response.status_code)
