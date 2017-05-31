#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by tanghaifeng


import urllib
import urllib2
import time
import os
import random
from bs4 import BeautifulSoup




def get_Html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"}
    req = urllib2.Request(url,headers=headers)
    res = urllib2.urlopen(req)
    res_html = res.read().decode('UTF-8')
    return res_html

def urlPages(page):
    url = "http://jandan.net/ooxx/page-" + str(page) + '#comments'
    return url

def find_img_url(html):
    soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    img_urls = soup.find_all(class_='view_img_link')
    return img_urls



def download_img(url):
    fdir = "D://jiandan"
    if not os.path.exists(fdir):
        os.makedirs(fdir)
    try:
        #(p2) = os.path.split(url)
        #(p2, f2) = os.path.split(url)
        f2 = ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(16)))
        #if os.path.exists(fdir + "/" + f2):
        #    print "fdir is exists"
        if url:
            imgtype = url.split('/')[4].split('.')[1]
            urllib.urlretrieve(url, fdir + "/" + f2 + '.' + imgtype)
            if os.path.getsize(filename) < 100:
                os.remove(filename)
    except Exception,e:
        return "down image error!"


def run():
    for page in range(1,88):
        html = get_Html(urlPages(page))
        urls = find_img_url(html)
        for url in urls:
            s = 'http:'+url.get('href')
            print s
            download_img(s)

if __name__ == '__main__':
    run()
