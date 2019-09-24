# coding=gbk
import requests
from lxml import etree
import time



def get_url(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    url_list = html.xpath('/html/body/div[3]/div/div/img/@src')
    return url_list

def download(s):
    list = []
    for i in range(s):
        url = "https://bing.ioliu.cn/?p={}".format(i+1)
        list += get_url(url)
    for i in range(len(list)):
        time.sleep(1)
        print("正在下载第{}张图片".format(i+1),end = ",")
        res = requests.get(list[i])
        f = open("{}.jpg".format(i+1),"wb")
        f.write(res.content)
        f.close()
        print("下载成功。",end="\n")

if __name__ == '__main__':
    s = eval(input("每页有照片12张，请输入下载照片页数："))
    download(s)



