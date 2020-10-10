# This is my second attempt at making a webscraper with
# the help of a FCC blog post and Dr. Chuck's book

from bs4 import BeautifulSoup
import request
import urllib.request
import urllib.parse
import urllib.error
import ssl
# import random

#

# I do not fully understand this code as it is from Dr. Chuck's book.
# It looks like this may be replaced with one line of code
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

url = input()

# html = urllib.request.urlopen(url, context=ctx).read()
# test code re: above comment regarding ssl
# update: this works. Need to read ssl documentation to understand why

# OK. Still some learning to do. This is not validating the source, which on a
# larger scale would create security issues.
html = urllib.request.urlopen(url, context=ssl._create_unverified_context())

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


print(potentialLinks[0])
print('----------------------------------------')
print(badLinks)
