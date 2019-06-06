# coding:utf-8
import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains 
import config as conf

def ss_output(outPath, fileName, data):
    with open(outPath + fileName, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    print('-- Start --')
    #driverの場所
    driver = webdriver.Chrome('/usr/local/lib/python3.7/site-packages/chromedriver')

    #ログインページへ遷移
    driver.get(conf.login_url)

    #指定したname属性に一致した箇所に値をセットする
    driver.find_element_by_name('txtUsrId').send_keys(conf.login_id)
    driver.find_element_by_name('pwdPsw').send_keys(conf.login_password)

    time.sleep(1)
    
    #ログイン
    driver.find_element_by_name('ELogin').click()

    time.sleep(2)

    driver.get(conf.attend_url)

    #SSが切れるため最大化
    driver.maximize_window()

    ssData = driver.find_element_by_class_name('scrl').screenshot_as_png

    ss_output(conf.outPath, 'ss1.png', ssData)

    #Div内でスクロールする, tr指定した要素
    actions = ActionChains(driver) 
    actions.move_to_element(driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/table/tbody/tr[16]/th'))
    actions.perform()
   
    ssData = driver.find_element_by_class_name('scrl').screenshot_as_png

    ss_output(conf.outPath, 'ss2.png', ssData)

    #ウィンドウを閉じる
    driver.close()

    print('-- End --')