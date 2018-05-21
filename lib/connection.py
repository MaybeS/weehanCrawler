import urllib.request as ur
import urllib.parse as up
from http.cookiejar import LWPCookieJar

def encode(params):
    return up.urlencode(params).encode('utf-8')

def request(url, params=None):
    return ur.Request(url, params)

def instance():
    cj = LWPCookieJar()
    return cj, ur.build_opener(ur.HTTPCookieProcessor(cj))
