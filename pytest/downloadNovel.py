from selenium import webdriver


### 根据id下载小说
def downloadNovel(driver, id):
    ## 1. 打开小说目录列表页
    ## 打开 https://www.hongxiu.com/book/{id}#Catalog
    driver.get('https://www.hongxiu.com/book/' + id +  '#Catalog')

    ## 2. 获取所有章节链接列表
    ## 用 xpath 或 css 获取

    ## 3. 对章节列表中的每一章，获取它的文字内容
    ## getChapterText(link);

    ## 4. 把所有章节的内容文本合在一起，存盘

## 根据章节链接，获取文字内容
def getChapterText(driver, link):
    ## 1. 打开章节页面
    driver.get(link)

    ## 2. 获取内容文本
    # 获取 div.read-content.j_readContent
    text = ""
    return text


## 下载小说 ：天下苏门 21987824000603002
driver=webdriver.Chrome()
downloadNovel(driver, "21987824000603002")
driver.close()
