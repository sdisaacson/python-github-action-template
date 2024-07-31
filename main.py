import requests
from bs4 import BeautifulSoup
import os

# The URL of the page to scrape
url = "https://developer.ukg.com/wfm/openapi/"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Raise an error for bad status

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> tags within <div> tags
div_tags = soup.find_all('div')
for div in div_tags:
    a_tag = div.find('a')
    if a_tag and 'href' in a_tag.attrs:
        link = a_tag['href']
        link_text = a_tag.get_text()
        filename = f"{link_text}.json"

        # Construct the full URL for the linked page
        full_url = "https://developer.ukg.com" + link

        # Fetch the content of the linked page
        linked_page_response = requests.get(full_url)
        linked_page_response.raise_for_status()

        # Save the content to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(linked_page_response.text)

        print(f"Saved {filename}")

print("All files have been downloaded and saved.")
