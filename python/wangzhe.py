import requests
import json
# from pprint import pprint as print
from lxml import etree
import re

herodetail_sort = {"herodetail-sort-3": "坦克",
                   "herodetail-sort-4": "刺客",
                   "herodetail-sort-1": "战士",
                   "herodetail-sort-2": "法师",
                   "herodetail-sort-5": "射手",
                   "herodetail-sort-6": "辅助",
                   }
def get_dict1():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    url = "http://pvp.qq.com/web201605/js/herolist.json"
    res = requests.get(url, headers=header)
    hero_data = json.loads(res.text)
    ename_list = []
    cname_list = []
    for data in hero_data:
        ename_list.append(str(data['ename']))
        cname_list.append(data['cname'])
    hero_dict1 = dict(zip(cname_list, ename_list))
    return hero_dict1


def get_dict2():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    url = "http://pvp.qq.com/web201605/js/herolist.json"
    res = requests.get(url, headers=header)
    hero_data = json.loads(res.text)
    ename_list = []
    cname_list = []
    for data in hero_data:
        ename_list.append(str(data['ename']))
        cname_list.append(data['cname'])
    hero_dict2 = dict(zip(ename_list, cname_list))
    return hero_dict2





def get_coverlist(hero_data):
    name = hero_data.xpath('//h2[@class="cover-name"]/text()')[0]
    type = herodetail_sort[hero_data.xpath('//span[@class="herodetail-sort"]/i/@class')[0]]
    canshu = hero_data.xpath('//ul[@class="cover-list"]/li/span/i/@style')
    life = int(re.findall('\d', canshu[0])[0]) * '★'
    attack = int(re.findall('\d', canshu[1])[0]) * '★'
    ability = int(re.findall('\d', canshu[2])[0]) * '★'
    cmp = int(re.findall('\d', canshu[3])[0]) * '★'
    print('\n'*3)
    print("英雄:" + name)
    print("定位:"+type)
    print('生存能力:'+life)
    print('攻击伤害:'+attack)
    print('技能效果:'+ability)
    print('上手难度:'+cmp)
    print()


def get_skills(hero_data):
    skill_names = hero_data.xpath('//p[@class="skill-name"]/b/text()')
    wait_time = hero_data.xpath('//p[@class="skill-name"]/span[1]/text()')
    consume = hero_data.xpath('//p[@class="skill-name"]/span[2]/text()')
    skill_tips = hero_data.xpath('//div[@class="skill-tips"]/text()')
    skill_desc = hero_data.xpath('//p[@class="skill-desc"]/text()')
    refuse_list = hero_data.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0].split('|')
    print('\n'*2)
    print("技能介绍：")
    for i in range(len(skill_names)):
        print(str(i+1)+ '  '+skill_names[i]+":"+"\n"+'    '+wait_time[i]+'\n'+'    '+consume[i]+'\n'+'    '+skill_tips[i]+'\n'+'    '+skill_desc[i])
    print('\n'*2)
    print('英雄皮肤:')
    for i in range(len(refuse_list)):
        print(str(i+1)+' '+refuse_list[i])
    print('\n'*2)


def get_guanxi(hero_data):
    hero_dict = get_dict2()
    p = hero_data.xpath('//div[@class="hero-list-desc"]/p/text()')
    hero_hd =  hero_data.xpath('//div[@class="hero-list hero-relate-list fl"]/ul/li/a/@href')
    hero_f11 =p[0]
    hero_f12 = p[1]
    hero_f21 = p[2]
    hero_f22 = p[3]
    hero_f31 = hero_dict[re.findall('\d+', hero_hd[4])[0]] + ":" + p[4]
    hero_f32 = hero_dict[re.findall('\d+', hero_hd[5])[0]] + ":" + p[5]
    print('最佳搭档英雄:')
    print('1 '+hero_f11)
    print('2 '+hero_f12)
    print()
    print('压制英雄:')
    print('1 '+hero_f21)
    print('2 '+hero_f22)
    print()
    print('被压制英雄:')
    print('1 '+hero_f31)
    print('2 '+hero_f32)
    print('\n'*2)


def get_story(hero_data):
    story = "     "+"".join(hero_data.xpath('//div[@class="pop-bd"]/p/text()'))
    print('英雄故事:')
    print(story)


def main():
    hero_name = input("请输入英雄名字：")
    dict1 = get_dict1()
    dict2 = get_dict2()
    url = "https://pvp.qq.com/web201605/herodetail/{}.shtml".format(dict1[hero_name])
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    res = requests.get(url, headers=header)
    res.encoding = "gbk"
    hero_data = etree.HTML(res.text)
    get_coverlist(hero_data)
    get_skills(hero_data)
    get_guanxi(hero_data)
    get_story(hero_data)


if __name__ == '__main__':
    try:
        main()
    except:
        print("对不起，没找到这个英雄！")
