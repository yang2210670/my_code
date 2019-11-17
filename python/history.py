import requests
# from pprint import pprint as print
import re
import time
import json

def get_time():
    mon = int(input('请输入月份:'))
    day = int(input('请输入号数:'))
    print("")
    return mon,day

def get_data(url):
    res = requests.get(url)
    js = json.loads(res.text)
    result = js['result']
    for s in result:
        t = re.findall('\d+',str(s['_id']))[0]
        print('时间:'+t[0:-4]+'年'+t[-4:-2]+'月'+t[-2:]+'日'+'  '+s['lunar'])
        print('事件:'+s['title'])
        print('内容:'+s['des'])
        print(" ")

def select():
    print('欢迎使用 [历史今日] 查询工具!')
    print('1 查询当日')
    print('2 自定义查询时间')
    m = int(input('请输入您所需服务序号:'))
    print('\n')
    return m

def main():
    m = select()
    if m == 1:
        url = 'http://zhouxunwang.cn/data/?id=36&key=A7vDqtNvQtr+iJyA94o0T2jBOATgsJeZ/pxx6w&v=1.0&month={}&day={}'.format(int(time.gmtime().tm_mon),int(time.gmtime().tm_mday))
        get_data(url)
    elif m == 2:
        t = get_time()
        url = 'http://zhouxunwang.cn/data/?id=36&key=A7vDqtNvQtr+iJyA94o0T2jBOATgsJeZ/pxx6w&v=1.0&month={}&day={}'.format(int(t[0]),int(t[1]))
        get_data(url)

    else:
        print('未知错误!')

if __name__ == '__main__':
    main()
    

