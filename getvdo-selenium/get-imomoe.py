import os
import urllib.request as req

from selenium import webdriver
from selenium.webdriver.common.by import By

base_dir = 'C:\\vdos'

def getvdo(driver, vdoId):
    ## 1. 打开目录列表页
    driver.get('http://www.imomoe.ai/view/' + str(vdoId) + '.html')

    title = str(vdoId) #+ driver.find_element_by_css_selector('span.names')[0].get_attribute('text')

    vdo_dir = base_dir+ '\\' + title
    ## 2. 获取所有视频播放页链接列表
    ## 用 xpath 或 css 获取
    episodes = []
    for link in driver.find_elements(By.CSS_SELECTOR, '#play_0 > ul > li > a'):
        episodes.append({'name': link.get_attribute('text'), 'href': link.get_attribute('href')})

    os.makedirs(vdo_dir)
    for episode in episodes:
        updateVdoLink(driver, episode)
        req.urlretrieve(episode['vdosrc'], vdo_dir+'\\'+episode['name']+'.mp4')


def updateVdoLink(driver, episode):
    driver.get(episode['href'])
    driver.switch_to_frame('play2')
    vdoElement = driver.find_element_by_css_selector('#a1 > div.dplayer-video-wrap > video')
    episode['vdosrc'] = vdoElement.get_attribute('src')


## 下载小说 ：天下苏门 21987824000603002
driver = webdriver.Chrome()
getvdo(driver, "538")
driver.close()
