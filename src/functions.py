from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


def get_source(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url=url, headers=headers)
    html = urlopen(req).read()
    return html.decode()

def create_soup(url):
    html = get_source(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup