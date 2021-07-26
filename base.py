from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)

html_byte = page.read()
html = html_byte.decode("utf-8")

print(html)
