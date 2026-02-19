#!/usr/bin/python3
"""
This module contains a function that makes a request to a URL
"""
import requests
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print("\t- {}".format(post.get("title")))


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        data = response.json()
        posts = []
        for post in data:
            post.data = {
                    'id': post["id"],
                    'title': post["title"],
                    'body': post["body"],
                    }
        posts.append(post)
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)
