import argparse
from functools import partial

from lib.pool import run
from lib.page import save, load
from lib.connection import instance
from lib import api

def main(id, pw):
    _, opener = instance()

    content = api.login(opener, id, pw)
    if not content:
        raise Exception('Login Failed')
    print ('Hello!', id)

    page = load()
    while True:
        pages = api.get_pages(opener, page)
        print ('now page:', page, 'now point:', api.get_point(opener, next(pages)))
        result = run(partial(api.get_page, opener), pages)
        page += 1
        save(page)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="id of user", type=str)
    parser.add_argument("pw", help="pw of user", type=str)
    args = parser.parse_args()

    main(args.id, args.pw)
