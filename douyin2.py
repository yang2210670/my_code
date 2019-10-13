# -*- coding: utf-8 -*-
import requests
import json
import re
from mydload import downloadfile


def url_parse(first_url):
    url = first_url.split(' ')[-2]
    return url


def get_mid(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    id = res.text.split('/')[5]
    mid = re.findall("mid=(.*?)&amp", res.text)[0]
    return mid,id


def get_parameter(mid,id):
    api = "https://www.iesdouyin.com/share/video/{}/".format(id)
    querystring = {"region": "CN", "mid": mid, "u_code": "14kfd7jc6", "titleType": "title",
                   "utm_source": "copy_link", "utm_campaign": "client_share", "utm_medium": "android", "app": "aweme"}
    headers = {
        'authority': "www.iesdouyin.com",
        'cache-control': "no-cache",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Mobile Safari/537.36",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'sec-fetch-site': "none",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en,zh;q=0.9,en-US;q=0.8,zh-CN;q=0.7",
        'cookie': "tt_webid=6747241470506255879; _ba=BA0.2-20191013-5199e-uzYNzhltjMjicGHspBtV; _ga=GA1.2.1498799453.1570964585; _gid=GA1.2.1193785399.1570964585",
        'postman-token': "4c084325-2f57-37cb-3ad5-536607dc81b6"
    }

    response = requests.request("GET", api, headers=headers, params=querystring)
    item_ids = re.findall('itemId: "(.*?)",', response.text)[0]
    dytk = re.findall('dytk: "(.*?)" }', response.text)[0]
    return item_ids, dytk


def get_data(item_ids, dytk):
    api = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/"
    querystring = {"item_ids": item_ids,
                   "dytk": dytk}
    headers = {
        'sec-fetch-mode': "cors",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en,zh;q=0.9,en-US;q=0.8,zh-CN;q=0.7",
        'user-agent': "ttplayer(2.9.5.362)",
        'accept': "*/*",
        'referer': "https://www.iesdouyin.com/share/video/6737411526405262599/?region=CN&mid=6737369819445742347&u_code=14kfd7jc6&titleType=title&utm_source=copy_link&utm_campaign=client_share&utm_medium=android&app=aweme",
        'authority': "www.iesdouyin.com",
        'x-requested-with': "XMLHttpRequest",
        'sec-fetch-site': "same-origin",
        'cache-control': "no-cache",
        'postman-token': "7fca3381-daca-17d9-86dd-ee623328a8cb"
    }

    response = requests.request("GET", api, headers=headers, params=querystring)
    name = json.loads(response.text)['item_list'][0]['desc'].strip()
    addr = json.loads(response.text)['item_list'][0]['video']['play_addr']['url_list'][0]
    return name, addr


def main():
    first_url = input("请输入分享连接：")
    url = url_parse(first_url)
    mid_data = get_mid(url)
    parameter = get_parameter(mid_data[0],mid_data[1])
    data = get_data(parameter[0],parameter[1])
    downloadfile(data[1], data[0].split(" ")[0] + ".mp4")


if __name__ == '__main__':
    try:
        main()
    except:
        print("不好意思，接口又挂了，呜呜呜！")