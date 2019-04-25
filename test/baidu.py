import os
import http.client
import hashlib
import json
import urllib
import random
import time
 
def baidu_translate(content):
    appid = '20151113000005349'
    secretKey = 'osubCEzlGjzvw8qdQc41'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'ja' # 源语言
    toLang = 'zh'   # 翻译后的语言
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return dst # 打印结果
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
 
if __name__ == '__main__':
    file_name = "file.txt"
    
    try:
        file = open(file_name)
        lines = file.readlines()
        os.remove('file_result.txt')
        for line in lines:
            if len(line.strip()) != 0:
                # print(baidu_translate(line.strip()))
                time.sleep(1)
                with open("file_result.txt", "a") as f:
                    f.write(line.strip()) 
                    f.write('\n\n')
                    f.write(baidu_translate(line.strip()))
                    f.write('\n\n')
        
        dic = {
'滤波器': '滤镜',
'摄像元件': '图像感应器',
'白飞': '高光溢出',
'镜头交换式照相机': '可换镜头式相机',
'尺寸': '画幅',
'装载':'搭载',
'《':'“',
'》':'”',
'「':'“',
'」':'”',
'胶卷':'胶片',
'(':'（',
')':'）',
'福瑟斯':'4/3（Four Thirds）',
'液晶显示器':'液晶监视器',
'反射镜':'反光镜',
'FORSERS':'4/3',
'·':'・',
'胶卷':'胶片',
'无反光镜机':'微单相机',
'镜头反光相机':'微单相机',
'反光镜相机':'微单相机',
'无反光相机':'微单相机',
'胶片式相机':'胶片相机',
'照相机':'相机',
'模型':'机型',
'抖动补正':'防抖',
'西格玛':'适马',
'模糊':'虚化',
'透镜':'镜头',
'车型':'机型',
'数字':'数码',
'机种':'机型',
'噪声':'噪点',
'噪音':'噪点',
'模糊':'虚化',
'过滤器':'滤镜',
'适配器':'转接环',
'实体':'机身',
'图像处理引擎':'影像处理器',
'挂载':'卡口'
        }       
        with open("file_result.txt") as f:
            newText = f.read()
        for key, value in dic.items():
            newText = newText.replace(key, value)
        with open("out.txt", "w") as f:
            f.write(newText)
        print('終了')
    except Exception as e:
        print(e)
    finally:
        file.close()
        
