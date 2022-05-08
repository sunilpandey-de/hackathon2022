import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint

def get_only_text(url):
    """
    return the title and the text of the article
    at the specified url
    """
    page = urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    print (text)
    return soup.title.text, text


url="https://www.wellsfargo.com/about/corporate/governance/carr/"
text = get_only_text(url)

import re
def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup (["script", "style", "aside"]):
        script.extract()
    return " ".join(re.split(r'[\n\t]',soup.get_text()))
print("\n")
print("\n")
pprint(url_to_string("https://www.wellsfargo.com/about/corporate/governance/carr/"))