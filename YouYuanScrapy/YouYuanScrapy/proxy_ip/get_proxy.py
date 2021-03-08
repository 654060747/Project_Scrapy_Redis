# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import http.client
import threading
import os
from random import choice


# 代理ip(使用代理配置)
# proxys = ["111.11.100.13:8060","45.221.77.82:8080","112.109.198.106:3128","60.9.1.80:80","47.106.216.42:8000","116.196.115.209:8080"]
# #1.使用python random模块的choice方法随机选择某个元素
# proxy = choice(proxys)

# proxy_d = "http://"+proxy

# proxies = {
#     "http":proxy_d
# }

proxyip_dir = "./"
# 没有验证前所有的代理ip
proxyip_file = "proxy.csv"
# 验证后剩余有用的代理ip
verify_proxyip_file = "verified_proxy.csv"

lock = threading.Lock()

def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass

def getProxyList(targeturl):

    CheckDir(proxyip_dir)
    proxyFile = open(proxyip_dir+proxyip_file , 'a', encoding='utf-8') # 打开一次
    requestHeader = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
    for page in range(1, 50):
        url = targeturl +str(page)
        print(url)
        #print url
        # 使用代理
        # req = requests.get(url, proxies=proxies, headers=requestHeader)
        # 不使用代理
        time.sleep(1)
        rs = requests.get(url, headers=requestHeader, verify=False)
        rs.encoding = 'utf-8'
        soup = BeautifulSoup(rs.text, "lxml")
        #print soup
        trs = soup.select('#list > table > tbody > tr')
        # print(data)
        if trs != None:
            for tr in trs:
                tds = tr.find_all('td')
                # print(tds)
                ip      =   tds[0].text.strip() #IP
                port    =   tds[1].text.strip() #PORT
                anony   =   tds[2].text.strip() #匿名度
                protocol=   tds[3].text.strip() #类型
                speed   =   tds[4].text.strip() #位置
                response_time    =   tds[5].text.strip() #响应速度
                _time    =   tds[6].text.strip() #最后验证时间
                proxyFile.write('%s|%s|%s|%s|%s|%s|%s\n' % (ip, port, anony, protocol, speed, response_time, _time))
                print ('%s=%s:%s' % (protocol, ip, port))
    
    proxyFile.close()

    
def verifyProxyList():
    '''
    验证代理的有效性
    '''
    
    requestHeader = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
    myurl = 'https://www.baidu.com/'

    while True:
        lock.acquire()
        ll = inFile.readline().strip()
        lock.release()
        if len(ll) == 0: break
        line = ll.split('|')
        protocol= line[3]
        ip      = line[0]
        port    = line[1]
        
        try:
            conn = http.client.HTTPConnection(ip, port, timeout=5.0)
            conn.request(method = 'GET', url = myurl, headers = requestHeader )
            res = conn.getresponse()
            lock.acquire()
            print ("+++Success:" + ip + ":" + port)
            outFile.write(protocol+"://"+ip + ":" + port + "\n")
            lock.release()
        except:
            print ("---Failure:" + ip + ":" + port)
        


getProxyList("https://www.kuaidaili.com/free/inha/")

getProxyList("https://www.kuaidaili.com/free/intr/")


print (u"\n验证代理的有效性：")

all_thread = []
# 文件打开一次，注意不能放到循环里
inFile = open(proxyip_dir+proxyip_file,encoding='utf-8')
outFile = open(proxyip_dir+verify_proxyip_file, 'w', encoding='utf-8')

for i in range(50):
    t = threading.Thread(target=verifyProxyList)
    all_thread.append(t)
    t.start()
    
for t in all_thread:
    t.join()

inFile.close()
outFile.close()
print ("All Done.")