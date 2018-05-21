from .connection import encode
from .connection import request
from .parser import parse

def login(opener, id, pw):
    url = 'http://www.weehan.com/'
    params = encode({
        "mid": "main2018",
        "vid": "",
        "ruleset": "@login",
        "act": "procMemberLogin",
        "user_id": id,
        "password": pw
    })
    req = request(url, params)
    content = parse(opener.open(req))
    return False if '잘못된 비밀번호입니다.' in content else content

def get_point(opener, content):
    return content.find('div', attrs={'class': 'point'}).get_text().strip().split('/')[0]

def get_pages(opener, page):
    url = 'http://www.weehan.com/index.php?mid=board_all&page={}'.format(page)
    content = parse(opener.open(request(url)))
    yield content
    for title in content.find_all('td', attrs={'class': 'title'}):
        yield title.find('a').get('href')

def get_page(opener, link):
    url = 'http://www.weehan.com/{}'.format(link)
    return opener.open(request(url))
