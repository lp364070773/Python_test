import requests
import re
import urllib
import sys
import selenium

url = "http://192.168.200.200:8088/jenkins/j_acegi_security_check"
headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
   }  # get方法其它加个ser-Agent就可以了
d = {"j_username": "lupeng",
 "j_password": "123456",
 "from": "",
 "Submit": u"登录",
 "remember_me": "on"
   }

s = requests.session()
r = s.post(url, headers=headers, data=d)
#print (r.content.decode('utf-8'))

t = re.findall(r'<span>(.+?)</span>', r.content.decode('utf-8'))   # 用python3的这里r.content需要解码
# print (t[0])
# print (t[1])

#新建任务
url1 = "http://192.168.200.200:8088/view/all/createItem"
body = {"name":"哈哈",
         "mode": "hudson.model.FreeStyleProject",
         "Jenkins-Crumb":"6de5a605dbfe0edee2789f24e384bb2d38700bb8247294c03f24605a2a632779",
         "json":{"name": "哈哈", "mode": "hudson.model.FreeStyleProject", "from": "",
          "Jenkins-Crumb": "6de5a605dbfe0edee2789f24e384bb2d38700bb8247294c03f24605a2a632779"}
}
print(type (body))

#获取name的值
name = body['name']
print('name:'+name)
#获取body的值
Jenkins_Crumb = body['Jenkins-Crumb']
print('body的值是：',body['Jenkins-Crumb'])
r2 = s.post(url1, data=body, verify=False)
#print (r2.content.decode('utf-8'))
#删除新建任务
url2 = "http://192.168.200.200:8088/job/%E5%93%88%E5%93%88/doDelete"
body1 = {
            "Jenkins-Crumb": Jenkins_Crumb
}
 
r3 = s.post(url2, data=body1, verify=False)
print (r3.content.decode('utf-8'))
#删除成功重定向到主界面（由于抓包没有看到response的结果，只知道重定向主界面）
print(r3.url)