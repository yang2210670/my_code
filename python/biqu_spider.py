import requests
import time
from lxml import etree

url = input("请输入笔趣阁(52bqg.com)小说主页URL:")
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}

def get_data(url):
    res = requests.get(url,headers = headers)
    res.encoding = 'gbk'
    html = etree.HTML(res.text)
    title_list = html.xpath('//*[@id="list"]/dl/dd/a/text()')
    url_list = html.xpath('//*[@id="list"]/dl/dd/a/@href')
    name = html.xpath('//*[@id="info"]/h1/text()')[0]
    data = dict(zip(title_list,url_list))
    return data,name

def get_content(url):
    res1 = requests.get(url,headers = headers)
    res1.encoding = 'gbk'
    cha_html = etree.HTML(res1.text)
    content = cha_html.xpath('//*[@id="content"]/text()')
    return content

def download(f,cha_name,content):
    f.write('\n' + cha_name + '\n')
    for item in content:
        f.write(item)

def main():
    data = get_data(url)
    data_dict = data[0]
    name = data[1]
    print(name)
    f = open(name + '.txt','w',encoding='utf-8')
    for kv in data_dict.items():
        time.sleep(3)
        try:
            content = get_content(url + kv[1])
            download(f,kv[0],content)
            print('下载成功:' + kv[0])
        except:
            print('下载失败:' + kv[0])
    f.close()    
if __name__ == '__main__':
    main()
