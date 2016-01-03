#!/usr/bin/python
# -*- coding:utf-8 -*-
# MaybeS

import urllib.request as ur
import urllib.parse as up
import http.cookiejar
from sys import argv
from sys import exit
from os import path
from codecs import open
from bs4 import BeautifulSoup

def show(text):
	print (text)

def getView(url):
	try:
		view = opener.open(url)
	except:
		view = None
	return view

def getContent(view):
	return BeautifulSoup(view, "lxml")

def getPoint(content):
	point = content.find('div', attrs = {'class': 'gpe_levelpoint'})
	if (point == None):
		return None
	point = point.find('span', attrs = {'style': 'letter-spacing:0; font-weight:bold; color:#00a6d4;'}).get_text().strip()
	return point

pageurl = "page.ini"
def getPage():
	global pageurl
	fp = open(pageurl, "r")
	page = int(fp.read())
	fp.close()
	return int(page)

def setPage(page):
	global pageurl
	fp = open(pageurl, "w")
	fp.write(str(page))
	fp.close()

page = 0
targetUrl = "http://www.weehan.com"
actUrl = "/index.php?mid=mina&page="

if __name__ == "__main__":
	#start from existing storage page 
	if (path.exists(pageurl)):
		page = getPage()
	else:
		setPage(page)

	if(len(argv) < 2):
		show("""
Weehan Crawler, by MaybeS(mytryark@gmail.com)
developed by python 3.4

must input like
$> """ + argv[0] + " [ID] [PW]")
		exit()
	user_id = str(argv[1])
	user_pw = str(argv[2])

	#make cookie jar
	cj = http.cookiejar.LWPCookieJar()
	opener = ur.build_opener(ur.HTTPCookieProcessor(cj))

	show("login ...")
	#set parameter
	params = up.urlencode({"error_return_url": "/main2015_2", "mid": "main2015_2", "vid": "", "ruleset": "@login", "act": "procMemberLogin", "success_return_url": "/main2015_2", "user_id": user_id,"password": user_pw })
	params = params.encode('utf-8')

	#request, response
	req = ur.Request(targetUrl, params)
	point = getPoint(getContent(getView(req)))

	if (point == None):
		show("login failed!")
		exit()
	show("login success.")

	while True:
		#stop point save for after run
		setPage(page)
		page = page + 1

		#get links in page
		content = getContent(getView(targetUrl + actUrl + str(page)))
		point = getPoint(content)
		titles = content.find_all('a', attrs = {'class': 'hx'})
		print ("now point: " + str(point))
		print ("now page: " + str(page))

		for title in titles:
			title = title['data-viewer']
			if title!= None:
				content = getView(targetUrl + title)
else:
	print('it must run by itselft')