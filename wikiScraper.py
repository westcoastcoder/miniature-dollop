# This is my second attempt at making a webscraper with
# the help of a FCC blog post and Dr. Chuck's book

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input()

html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

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


print(potentialLinks)
print('----------------------------------------')
print(badLinks)
