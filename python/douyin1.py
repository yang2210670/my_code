import requests
from pprint import pprint
import json
from mydload import downloadfile


api = 'https://aweme-hl.snssdk.com/aweme/v1/aweme/detail/?aweme_id={}&device_platform=ios&app_name=aweme&aid=1128'
headers = {'user-agent': 'Mozilla/5.0'}


def get_data(surl):
    url = surl.split(' ')[-2]
    res = requests.get(url, allow_redirects=False)
    wurl = res.headers['location']
    id = wurl.split('/')[5]
    rel_url = api.format(id)
    data = requests.get(rel_url, headers=headers)
    res_code = data.status_code
    # pprint(json.loads(data.text))
    return data.text, res_code


def download(data):
    video_data_list = {}
    js_data = json.loads(data)
    name = js_data['aweme_detail']['desc']
    try:
        url_list = js_data['aweme_detail']['long_video'][0]['video']['play_addr']['url_list']
    except:
        url_list = js_data['aweme_detail']['video']["play_addr"]['url_list']
    author = js_data['aweme_detail']['author']['nickname']
    introduce = js_data['aweme_detail']['author']['signature']
    Head = js_data['aweme_detail']['author']['avatar_thumb']['url_list'][0]
    music = js_data['aweme_detail']['music']['title']
    owner_nickname = js_data['aweme_detail']['music']['owner_nickname']
    play_url = js_data['aweme_detail']['music']['play_url']['url_list'][0]
    video_data_list["视频名称"] = name
    video_data_list["视频作者"] = author
    video_data_list["视频地址"] = "有点长，拒绝输出"
    video_data_list["作者签名"] = introduce
    video_data_list["作者头像"] = Head
    video_data_list["音乐名称"] = music
    video_data_list["音乐作者"] = owner_nickname
    video_data_list["音乐地址"] = play_url
    return video_data_list, name, url_list[0]


def get_durl(url):
    headers = {'user-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    durl = res.headers['Location'] + ".mp4"
    return durl


def main():
    share_url = input('请输入抖音分享链接:')
    s = get_data(share_url)
    if s[1] == 200:
        print("欢迎使用本程序下载抖音视频，下面是视频信息：" + '\n')
        data = download(s[0])[0]
        for item in list(data.items()):
            print(item[0] + ":" + item[1].replace("\n",""))
        print('\n需要下载视频吗？ y/n')
        fo = input()
        if fo == 'y':
            url = get_durl(download(s[0])[2])
            name = download(s[0])[1].strip()
            downloadfile(url, name)
        else:
            pass

    else:
        print('对不起，视频信息提取错误')


if __name__ == '__main__':
    main()

# #在抖音，记录美好生活#@剪辑手过往~好男人就要志在四方，顶天立地，成就春秋霸业#楚汉传奇 #剪辑 http://v.douyin.com/apY1Gj/ 复制此链接，打开【抖音短视频】，直接观看视频！
#在抖音，记录美好生活#向往的生活，就是儿时的小巷，时间，暖阳，还有那份难得的宁静 #大连  http://v.douyin.com/avwLfE/ 复制此链接，打开【抖音短视频】，直接观看视频！