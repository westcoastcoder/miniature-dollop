# This is my second attempt at making a webscraper with
# the help of a FCC blog post and Dr. Chuck's book

from bs4 import BeautifulSoup
import requests

# import random

# After a bit more research, it looks like requests is the better module to use
# at this stage (AKA as a beginner)

url = input()

# Requests handles the ssl automatically (default is set to true, so I guess
# Wikipedia has there certs set up...)

html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.text)

tags = soup.find(id='bodyContent').find_all('a')

potentialLinks = []
badLinks = []

for tag in tags:
    try:
        # We only want wikipedia links (no external links)
        if (tag['href'].find("/wiki/") != -1
                and tag['href'].find("https://") != 0):
            potentialLinks.append(tag['href'])
    # This is to catch any errors where an href attribute is not present
    except KeyError:
        print("Error: No href attribute present in 'a' tag.")
        badLinks.append(tag)
        continue

for link in potentialLinks:
    print(link)
