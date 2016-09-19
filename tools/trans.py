import urllib.request
import urllib.parse
import json

def trans():
    
    while True:
        
        content=input('root!trans!：请翻译：')
        if content=='<<':
            break
        else:
       
            url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'

            head={}
            head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

            data={}
            data['type']='AUTO'
            data['i']=content
            data['doctype']='json'
            data['xmlVersion']='1.8'
            data['keyfrom']='fanyi.web'
            data['ue']='UTF-8'
            data['action']='FY_BY_CLICKBUTTON'
            data['typoResult']='true'
            data=urllib.parse.urlencode(data).encode('utf-8')

            req=urllib.request.Request(url,data,head)
            response=urllib.request.urlopen(req)
            html=response.read().decode('utf-8')

            target=json.loads(html)
            print('翻译结果：%s' %(target['translateResult'][0][0]['tgt']))

if __name__ == '__main__':
    trans()
    
