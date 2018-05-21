from bs4 import BeautifulSoup as bs

def parse(raw):
    return bs(raw, "lxml")
