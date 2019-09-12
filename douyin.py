import requests
from pprint import pprint
import json

api = 'https://aweme-hl.snssdk.com/aweme/v1/aweme/detail/?aweme_id={}&device_platform=ios&app_name=aweme&aid=1128'
headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

def get_data(surl):
    url = surl.split(' ')[-2]
    res = requests.get(url,allow_redirects=False)
    wurl = res.headers['location']
    id = wurl.split('/')[5]
    rel_url = api.format(id)
    data = requests.get(rel_url,headers = headers)
    res_code = data.status_code
    return data.text,res_code


def dowload(data):
    js_data = json.loads(data)
    name = js_data['aweme_detail']['desc']
    url_list = js_data['aweme_detail']['video']['play_addr']['url_list']
    author = js_data['aweme_detail']['author']['nickname']
    introduce = js_data['aweme_detail']['author']['signature']
    Head = js_data['aweme_detail']['author']['avatar_thumb']['url_list'][0]
    music = js_data['aweme_detail']['music']['title']
    owner_nickname = js_data['aweme_detail']['music']['owner_nickname']
    play_url = js_data['aweme_detail']['music']['play_url']['url_list'][0]
    video_data_list = {"name":name,"video_url":url_list,"author":author,"introduce":introduce,"Head":Head,
                        "music_name":music,"music_author":owner_nickname,"music_url":play_url}
    js = json.dumps(video_data_list, ensure_ascii=False)
    return js

def main():
    share_url = input('请输入抖音分享链接:')
    s = get_data(share_url)
    if s[1] == 200:
        print('\n\n'+"欢迎使用本程序下载抖音视频，下面是视频信息："+'\n')
        data = dowload(s[0])
        pprint(json.loads(data))
    else:
        print('对不起，视频信息提取错误')



if __name__ == '__main__':
    main()

