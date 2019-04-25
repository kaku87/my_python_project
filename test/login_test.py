from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import CookieJar
from loginform import fill_login_form
import requests
import pprint
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
login_url = 'http://www.musasi.jp/ichikawa-chuo/login'
r = requests.get(login_url)
login_user = '44644'
login_password = '03759'
values, action, method = fill_login_form(login_url, r.text, login_user, login_password)
print(u'url: {0}\nmethod: {1}\npayload:'.format(action, method))
for k, v in values:
    print(u'- {0}: {1}'.format(k, v))
    
opener = build_opener(HTTPCookieProcessor(CookieJar()))

values = urlencode(values).encode('utf-8')
# はてなサービスにログインします
res = opener.open(action, values)

# HTTPResponseヘッダーを表示しています
# 中にSet-Cookieのヘッダーがあることがわかります
pprint.pprint(res.getheaders())

res.close()
res = opener.open("http://www.musasi.jp/")
pprint.pprint(res.read())
res = opener.open("http://www.musasi.jp/digital")
pprint.pprint(res.read())
#session = requests.Session();
#s = session.post(action,values, headers=headers)
#print(s.status_code)
##headers["Cookie"]=s.headers["Set-Cookie"]
#print("Cookie is set to:")
#print(s.cookies.get_dict())
#a = session.get("http://www.musasi.jp/digital")
#print(a.status_code)