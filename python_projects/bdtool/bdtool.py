
import importlib, sys, urllib
importlib.reload(sys)
import urllib.request
import json  # 导入json模块
import hashlib
import urllib
import random
import time
'''
通过调用百度api，实现实时翻译以及存储已翻译的词汇。
api使用说明：http://api.fanyi.baidu.com/api/trans/product/apidoc#joinFile
'''
if __name__ == '__main__':
    flag = input('输入1：查看词汇本\n输入2：翻译\n输入3：离开\n请输入你的选择(1/2/3)：')
    while flag!='1' and flag!='2' and flag!='3':
        flag = input('命令错误，请按照要求重新输入: ')
    if flag=='1':
        with open('words.txt', 'r') as rd:
            for line in rd.readlines():
                print(line, end='')
        flag = input('输入任意键,按enter退出程序!')
    elif flag=='2':
        appid = '20171120000098005'  # 自己在百度翻译开放平台注册的账号的开发者信息
        secretKey = 's1op5ShDU8HOqNAht1Yj'  # 自己在百度翻译开放平台注册的账号的开发者信息
        api_http = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        q = 'apple'
        fromLang = 'en'  # 翻译源语言, 具体查看百度翻译api
        toLang = 'zh'  # 译文语言
        salt = random.randint(32768, 65536)
        while True:
            word = input('请输入您要翻译的内容(输入\'*\'表示退出程序): ')
            if word == '*':
                break
            sign = appid + word + str(salt) + secretKey
            sign = hashlib.md5(sign.encode()).hexdigest()
            # print(sign)
            api_http = api_http + '?appid=' + appid + '&q=' + urllib.parse.quote(
                word) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
            resultPage = urllib.request.urlopen(api_http)  # 调用百度翻译API进行批量翻译

            # print(api_http)
            resultJason = resultPage.read().decode('utf-8')  # 取得翻译的结果，翻译的结果是json格式
            resultJasons = resultPage.read()
            # print(resultJason)
            try:
                js = json.loads(resultJason)  # 将json格式的结果转换成Python的字典结构
                translate_res = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
                print(translate_res)
                try:
                    with open('words.txt', 'a') as wordfile:
                        wordfile.write(word + '\n')
                        wordfile.write(translate_res + '\n')
                        wordfile.write('-' * 60 + '\n')
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
