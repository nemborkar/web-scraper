from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)

html_byte = page.read()
html = html_byte.decode("utf-8")


pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)

print(title)
