#!/usr/bin/python3
# -*- coding:utf-8 -*-
# MaybeS

import time 
import urllib.request as ur
import urllib.parse as up
import http.cookiejar
from sys import argv, exit
from os import path
from threading import Thread
from queue import Queue
from codecs import open
from bs4 import BeautifulSoup

queue = Queue()
pageurl = "page.ini"
page = 0

threadViewSize = 45
threadPageSize = 5

viewThreads=[]
pageThreads=[]

targetUrl = "http://www.weehan.com"
actUrl = "/index.php?mid=mina&page="

class ViewThread(Thread):
	def __init__(self):
		cj = http.cookiejar.LWPCookieJar()
		self.opener = ur.build_opener(ur.HTTPCookieProcessor(cj))
		request = ur.Request(targetUrl, params)


	def run(self):
		while True:
			url = queue.get()
			self.opener.open(url)
			print("poped " + url)

class PageThread(Thread):
	def __init__(self):
		self.opener
	
	def run(self, url):
		content = getContent(url)
		point = getPoint(content)
		show("now page: " + str(page) + ", point: " + str(point))
		titles = content.find_all('a', attrs = {'class': 'hx'})
		queue.put(url + titles[index]['data-viewer'])

def terminate(text):
	show(text)
	exit()
def show(text):
	print (text)
	#
def getContent(opener, url):
	return BeautifulSoup(opener.open(url), "lxml")
	#
def getPoint(content):
	point = content.find('div', attrs = {'class': 'gpe_levelpoint'})
	if (point == None):
		return None
	return point.find('span', attrs = {'style': 'letter-spacing:0; font-weight:bold; color:#00a6d4;'}).get_text().strip()
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

if __name__ == "__main__":
	#start from existing storage page 
	if (path.exists(pageurl)):
		page = getPage()
	else:
		setPage(page)

	if(len(argv) < 2):
		terminate("""
Weehan Crawler, by MaybeS(mytryark@gmail.com)
developed by python 3.4

must input like
$> """ + argv[0] + " [ID] [PW]")
	user_id = str(argv[1])
	user_pw = str(argv[2])

	#make cookie jar
	cj = http.cookiejar.LWPCookieJar()
	opener = ur.build_opener(ur.HTTPCookieProcessor(cj))

	show("login ...")
	params = up.urlencode({"error_return_url": "/main2015_2", "mid": "main2015_2", "vid": "", "ruleset": "@login", "act": "procMemberLogin", "success_return_url": "/main2015_2", "user_id": user_id,"password": user_pw })
	params = params.encode('utf-8')

	#request, response
	req = ur.Request(targetUrl, params)
	point = getPoint(getContent(opener, req))

	if (point == None):
		terminate("login failed!")
	show("login success.")

	show("thread(" + str(tsize) +") initilizing...")
	tchk = 0

	for index in range(tsize):
		cj = http.cookiejar.LWPCookieJar()
		openers.append(ur.build_opener(ur.HTTPCookieProcessor(cj)))
		request = ur.Request(targetUrl, params)
		if(getPoint(getContent(openers[index], request)) != None):
			tchk = tchk + 1
		threads.append(ThreadClass(openers[index], queue))
		threads[index].setDaemon(True)
		threads[index].run()

	if(tchk != tsize):
		terminate("thread initilize failed!")
	show("thread(" + str(tsize) +") initilize finished!")

	while True:
		#stop point save for after run
		setPage(page)
		page = page + 1


		content = getContent(opener, targetUrl + actUrl + str(page))
		point = getPoint(content)
		show("now page: " + str(page) + ", point: " + str(point))
		titles = content.find_all('a', attrs = {'class': 'hx'})

		t1 = time.time()
		for index in range(len(titles)):
			queue.put(targetUrl + titles[index]['data-viewer'])
			#openers[index].open(url + titles[index]['data-viewer'])
			#print ("visit: " + url + titles[index]['data-viewer'])

		print("queue added " + str(len(titles)))
		print ("exetime: " + str(time.time() - t1))
else:
	print('it must run by itselft')
