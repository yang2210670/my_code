import requests
import json
from pprint import pprint
from tqdm import tqdm


def get_vid(url):
    if 'vid' in url:
        vid = url.split('vid=')[-1].split('&')[0]
    else:
        vid = url.split('/')[-1].split('.')[0]
    return vid


def get_m3u8_url(vid):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'cookie': 'tvfe_boss_uuid=836cef3306ccd369; video_guid=45beb4a7d2a9105c; video_platform=2; pgv_pvid=3593629138; ts_uid=6977471568; bucket_id=9231007; tvfe_search_uid=c660189c-9e80-41f1-acfb-e4dcb15c0c38; login_remember=qq; pgv_pvi=1462210560; ptui_loginuin=2805704997; RK=DZIF5Uam6g; ptcz=b76c0d6dda1d48ef4fda2ccf9f3534499dcc7d7f23d8127122dc70c4c51d013e; webwx_data_ticket=gSdvLVSRYsXLiT/B9GTtNDdC; pgv_info=ssid=s6887315250; o_cookie=2251513837; pgv_si=s8880321536; main_login=qq; vqq_appid=101483052; last_refresh_time=1588689532270; last_refresh_vuserid=698396035; ts_refer=m.v.qq.com/index.html; qv_als=Q2Bi1/E5tZvxtKcmA11588692894Mc0fNA==; ts_last=v.qq.com/biu/u/history/;vqq_vuserid=544077820; vqq_vusession=do600lDKzE0Z0cEG6aOUnw..; vqq_access_token=B40C82130215DFA753F23A50CA784F50; vqq_openid=6E547FB11EE8878ED0A5F3C472D8CEE0; qq_nick=%E5%B0%9A%E5%A4%8F%E4%BD%90%E5%AE%A5; qq_head=http://thirdqq.qlogo.cn/g?b=oidb&k=6icLycw3dD8C2NgRrnwTtHw&s=640&t=1570117330; lw_nick=%E5%B0%9A%E5%A4%8F%E4%BD%90%E5%AE%A5|0|http://thirdqq.qlogo.cn/g?b=oidb&k=6icLycw3dD8C2NgRrnwTtHw&s=640&t=1570117330|0; uid=542486469; ad_play_index=90'
    }
    api = 'http://vv.video.qq.com/getinfo?'
    params = {
        'defn': 'fhd',
        'platform': '10801',  # 101001,10901,10801
        'otype': 'ojson',
        'sdtfrom': 'v4138',
        'appVer': '7',
        'vid': vid,
        'newnettype': '1',
        'fhdswitch': '1',
        'show1080p': '1',
        'dtype': '3',
        'sphls': '2',
    }
    res = requests.get(api, headers=headers, params=params).text
    data = json.loads(res)
    name = data['vl']['vi'][0]['ti']
    m3u8_url = data['vl']['vi'][0]['ul']['ui'][0]['url']

    return name, m3u8_url


def parse_url(m3u8_url):
    m3u8_head = '/'.join(m3u8_url.split('/')[0:-1]) + '/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    res = requests.get(m3u8_url, headers=headers).text
    addr_list = res.replace('\n', '').split(',')[1::]
    m3u8_list = [*map(lambda s: m3u8_head + s.split('#')[0], addr_list)]
    return m3u8_list


def download(name, m3u8_list):
    f = open(name + '.mp4', 'wb+')
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    print('开始下载视频:')
    for url in tqdm(m3u8_list):
        ts = requests.get(url, headers=headers)
        f.write(ts.content)

    f.close()
    print('视频下载完成！')


def main():
    url = input('请输入地址：')
    vid = get_vid(url)
    name = get_m3u8_url(vid)[0]
    m3u8_list = parse_url(get_m3u8_url(vid)[1])
    download(name, m3u8_list)


if __name__ == "__main__":
    main()