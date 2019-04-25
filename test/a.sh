import urllib
import re

import dukpy

# Webページを取得する。
f = urllib.request.urlopen('https://gigaplus.makeshop.jp/letdream/test/index.html')

# HTMLのボディをUnicode文字列にデコードする。
html = f.read().decode('utf-8')

# 正規表現でscript要素の中身を取得する。
# re.DOTALLで正規表現中の.が改行にもマッチするようになる。
m = re.search(r'<script type="text/javascript">(.*?)</script>', html, re.DOTALL)

# 正規表現でキャプチャしたscript要素の中身を取得する。
script = m.group(1)

# dukpyでJavaScriptを実行し、変数__DetailProp__の値を取得する。
js_obj = dukpy.evaljs([script, '__DetailProp__'])

# 取得できた値（タイトル、画像のURL、もっと読むの中身）を表示する。
print(js_obj['title'])  # タイトル
print(js_obj['img'])    # 画像のURL（/news/からの相対URL）
print(js_obj['more'])   # もっと読むの中身