import os
import urllib.request as req

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

base_dir = 'C:\\vdos'

def getvdo(driver, vdoId):
    ## 1. 打开目录列表页
    driver.get('http://www.imomoe.ai/view/' + str(vdoId) + '.html')

    title = str(vdoId) + "_" + driver.find_element_by_css_selector('span.names').text
    vdo_dir = base_dir+ '\\' + title
    ## 2. 获取所有视频播放页链接列表
    ## 用 xpath 或 css 获取
    episodes = []
    for link in driver.find_elements(By.CSS_SELECTOR, '#play_0 > ul > li > a'):
        episodes.append({'name': link.get_attribute('text'), 'href': link.get_attribute('href')})

    if not os.path.exists(vdo_dir):
        os.makedirs(vdo_dir)
    try:
        for episode in episodes:
            updateVdoLink(driver, episode)
            f = vdo_dir + '\\' + title + episode['name'] + '.mp4'
            if not os.path.exists(f):
                print("downloading " + f + "/n")
                req.urlretrieve(episode['vdosrc'], f)
                print("finished    " + f + "/n")
    except:
        return

def updateVdoLink(driver, episode):
    driver.get(episode['href'])
    driver.switch_to.frame('play2')
    vdoElement = driver.find_element_by_css_selector('#a1 > div.dplayer-video-wrap > video')
    episode['vdosrc'] = vdoElement.get_attribute('src')


## 下载小说 ：天下苏门 21987824000603002
opts = Options()
opts.add_argument('--headless')
opts.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=opts)
# getvdo(driver, "1361")
# getvdo(driver, "1707")
getvdo(driver, "391")
getvdo(driver, "6746")
getvdo(driver, "5101")

getvdo(driver, "390")
getvdo(driver, "2444")
getvdo(driver, "6705")
getvdo(driver, "980")
driver.close()
