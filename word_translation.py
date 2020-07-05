import urllib.request
import urllib.parse
import json
import time
import easygui

while True:
    content = easygui.enterbox(msg='请输入需要翻译的内容（输入“0”退出程序）：',title='翻译程序')#获取用户输入内容
    if content == '0':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'#爬取翻译结果的网址

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'#设置访问机器的名称

    data = {}
    data['i'] = content
    data['doctype'] = 'json'
    data = urllib.parse.urlencode(data).encode('utf-8')#编码成网站的编码形式

    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)#访问，返回文件对象
    html = response.read().decode('utf-8')#译码

    target = json.loads(html)#解码
    easygui.msgbox('%s' % (target['translateResult'][0][0]['tgt']),'翻译结果' )

    time.sleep(2)

#直接运行exe文件，则运行打包完成的应用程序
