import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
import re
import csv
import xlsxwriter
import sys

# driver = webdriver.PhantomJS(executable_path='/Users/ryan/Documents/pythonscraping/code/headless/phantomjs-1.9.8-macosx/bin/phantomjs')
#driver = webdriver.Firefox()

# driver = webdriver.Chrome("/home/ubuntu/workspace/bin/chromedriver")

# options = Options()
# options.binary_location = '/home/ubuntu/workspace/bin/chromedriver'
# options.add_argument('--headless')
# options.add_argument('--window-size=1280,1024')

# driver = webdriver.Chrome('chromedriver', chrome_options=options)

def main():
    args = sys.argv
    csv_file = open("201809202.csv", "r", encoding="ms932", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    header = next(f)

    workbook = xlsxwriter.Workbook('result.xlsx')
    worksheet = workbook.add_worksheet()
    # 自動改行
    text_format = workbook.add_format({'text_wrap': True})
    # 行高
    worksheet.set_default_row(320)
    # 設定列の長さ
    worksheet.set_column('C:C', 200)
    # 設定列の長さ
    worksheet.set_column('D:D', 100)

    i = 0
    for row in f:
        i = i + 1
        row[80]=re.sub(r'\n',"",row[80])

        settingsList = [re.sub(r'(.*:)',"",str) for str in row[80].split(',')]

        colorDict = {"ダークブラウン":"bg01",
                     "墨":"bg02",
                     "ワインレッド":"bg03",
                     "ブラウン":"bg04",
                     "チョコ":"bg05",
                     "ブラック":"bg06",
                     "グリーン":"bg07",
                     "ネイビー":"bg08",
                     "レッド":"bg09"}

        settingsList = [colorDict.get(item, item) for item in settingsList]

        getImage(settingsList)

        # 番号
        worksheet.write('A' + str(i), row[0])
        # 名前
        worksheet.write('B' + str(i), row[40]+row[41])
        # 設定
        worksheet.write('C' + str(i), row[80], text_format)
        # 画像
        # worksheet.insert_image('D' + str(i), 'page.jpg', {'x_scale': 0.4, 'y_scale': 0.4})

    workbook.close()


def getImage(settingsList):
    # driver = webdriver.Chrome('chromedriver', chrome_options=options)
    driver = webdriver.PhantomJS()
    driver.get("https://gigaplus.makeshop.jp/letdream/test/index.html")

    driver.implicitly_wait(10)
    # 内側を選択する
    driver.find_elements_by_xpath("//*[@id='app']/div[1]/div[1]/ul/li[1]")[0].click()

    # 可変エリア１を設定
    driver.find_elements_by_xpath("//*[@id='inside']/div[1]/p[1]")[0].click()
    driver.find_element_by_css_selector("li.selectcl." + settingsList[1]).click()

    # 可変エリア２を設定
    driver.find_elements_by_xpath("//*[@id='inside']/div[1]/p[2]")[0].click()
    driver.find_element_by_css_selector("li.selectcl." + settingsList[2]).click()

    # 可変エリア３を設定
    driver.find_elements_by_xpath("//*[@id='inside']/div[1]/p[3]")[0].click()
    driver.find_element_by_css_selector("li.selectcl." + settingsList[3]).click()

    # 可変エリア４を設定
    driver.find_elements_by_xpath("//*[@id='inside']/div[1]/p[4]")[0].click()
    driver.find_element_by_css_selector("li.selectcl." + settingsList[4]).click()

    # 可変エリア５を設定
    driver.find_elements_by_xpath("//*[@id='inside']/div[1]/p[5]")[0].click()
    driver.find_element_by_css_selector("li.selectcl." + settingsList[5]).click()

    # 可変エリア６を設定
    driver.find_elements_by_xpath("//*[@id='inside']/div[1]/p[6]")[0].click()
    driver.find_element_by_css_selector("li.selectcl." + settingsList[6]).click()

    # 可変エリア７を設定
    driver.find_elements_by_xpath("//*[@id='inside']/div[1]/p[7]")[0].click()
    driver.find_element_by_css_selector("li.selectcl." + settingsList[7]).click()

    # 外側を選択する
    driver.find_elements_by_xpath("//*[@id='app']/div[1]/div[1]/ul/li[2]")[0].click()

    # 可変エリアを設定
    driver.find_elements_by_xpath("//*[@id='outside']/div[1]/p")[0].click()
    driver.find_element_by_css_selector("li.selectcl." + settingsList[0]).click()

    # logo形式
    for logoType in driver.find_elements_by_name('logo_type'):
        if settingsList[9] in logoType.get_attribute("value"):
            logoType.click()

    # 名入れ形式
    for nameType in driver.find_elements_by_name('name_type'):
        if settingsList[10] in nameType.get_attribute("value"):
            nameType.click()

    # 名入れを設定する
    textinfo = driver.find_element_by_id("textinfo2")
    textinfo.send_keys(settingsList[8])
    
    print(driver.page_source)

    # プレビューを見るボタンをクリックする
    element=driver.find_element_by_id("btn-Preview-Image")
    element.click()
    
    

    # 画像を保存する
    image=driver.find_element_by_id("btn-Convert-Html2Image").get_attribute("href")
    print(image)
    # urlretrieve(image, "page.jpg")

if __name__ == '__main__':
    main()