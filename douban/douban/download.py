#-*- coding: utf-8 -*-

import urllib

def download(url,name):
    local = '/home/tong/musci/'+name+'.mp3'
    urllib.urlretrieve(url,local,cbk)

def cbk(a,b,c):
    per = 100.0 * a * b/c
    if per > 100:
        per = 100
    print '%.2f%%' % per

