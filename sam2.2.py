import requests
import csv

def get_api_comments(api_url):
    response = requests.get(api_url)
    return response.json()

api_url = "https://jsonplaceholder.typicode.com/comments"
api_comments = get_api_comments(api_url)

max_body_length = 150
short_comments = []

for comment in api_comments:
    if len(comment["body"]) < max_body_length:
        short_comments.append({"body": comment["body"]})

csv_file_name = "short_comments_data.csv"
with open(csv_file_name, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["body"])
    writer.writeheader()
    writer.writerows(short_comments)

print("Data loaded and saved into '{}' successfully.".format(csv_file_name))
