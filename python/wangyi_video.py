import requests
from lxml import etree
import re
from mydload import downloadfile


def get_id(url):
    id = id = url.split("=")[-1]
    return id

def get_data(id):
    url = "https://music.163.com/video"
    querystring = {"id": id}
    headers = {
        'authority': "music.163.com",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "nested-navigate",
        'referer': "https://music.163.com/",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': "_iuqxldmzr_=32; _ntes_nnid=0bf429d4bd92f4804fc43683c6f99b26,1573707499825; _ntes_nuid=0bf429d4bd92f4804fc43683c6f99b26; WM_TID=ToHbWaZBN6lAFQEABQN87GiT67kPo1qC; __remember_me=true; ntes_kaola_ad=1; UM_distinctid=16e8ba3a6165a-0f175c16c4a3da-2393f61-144000-16e8ba3a6172cc; vinfo_n_f_l_n3=35a321adffa72f19.1.0.1574300785899.0.1574300793792; mail_psc_fingerprint=a61dccb54cf7a63c1656bc6ad543ebc6; P_INFO=yang2210670^@163.com^|1575185923^|0^|urs^|00^&99^|sxi^&1575185678^&carddav^#sxi^&610100^#10^#0^#0^|^&0^|authcode^&urs^&study_client^&mail163^&note_client^|yang2210670^@163.com; WM_NI=3eMEMqazRCr9iFytfwPPQiuxljTprt0XLMA9^%^2FuYyVdLYVkD6TUP0XGH752ASFmQZ^%^2FC096^%^2FeejUUiG54^%^2BNNPhPViaLSWpdo7YoBjnyV0Vqw8PXXTAhNgyQH6ZDR^%^2BxC^%^2FAdOUU^%^3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8cf333a5b488afc64392968fa6c84e969f8eafbc7ba389ab9af45af5b9f887cc2af0fea7c3b92af1bb83a6d07ba3a69ea4f133ab9ab795e57d94909f8af874b0b69c91f180f48884aec433edab979ad57090879a8cc73e988ba0d1db4d8ce9fbd3c45986b39fbbae49f4e7fad0e86faa8b9b8ac63ff8f582afd364948aa782cf5995b0ac90b653ad9ea68ffc5ef48abf98bb5c9c889ca2eb46a5a79fa9b552888ee599c22583bc81b6d837e2a3; JSESSIONID-WYYY=au7NxUAYsT2fcKXBbi1nZP7HRU71f^%^2BgSEjbF7wE^%^2Byz3jSthtBsqdQwNcBFP^%^2F2sZkbPyhRIqYZro2qy3T9IjhZI6F^%^2FmRxMfomy3Nv2ei9uKpwx3^%^2BU^%^2F^%^2F3ljp9zjD4UQcCtxSGVhT57sWIQIQZhu0Kd4^%^2Fo2FTSCnfAJOrCNtf2PWKB4fOBp^%^3A1575381468751; MUSIC_U=2dd49e0d8c7e0c528b1dd6ab22798a7f0462b6952f7847bf8135d10fbf6ef5d2243db1ed0537be84c280db000ba3463741049cea1c6bb9b6; __csrf=2cbac938c0dda8b83bc80634f4417b29",
        'cache-control': "no-cache",
        'postman-token': "527870be-2a1d-f6ac-340e-db51898ade86"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = etree.HTML(response.text)
    urls = data.xpath('//*[@id="flash_box"]/@data-flashvars')[0]
    urls = urls.split("&autoPlay")[0].split("hurl=")[1].split("murl=")
    vname = data.xpath('//*[@id="flag_title1"]/text()')[0]
    return urls,vname


def url_parse(url):
    s1 = ["%3A","%2F","%3F","%3D","%26"]
    s2 = [":","/","?","=","&"]
    for i in range(len(s1)):
        url = re.sub(s1[i],s2[i],url)
    return url


def main():
    url = input("请输入视频链接:")
    id = get_id(url)
    vname = get_data(id)[1] + ".mp4"
    furl = get_data(id)[0][0]
    vurl = url_parse(furl)
    downloadfile(vurl,vname)

if __name__ == '__main__':
    try:
        main()
    except:
        print("未知错误")