import requests
from bs4 import BeautifulSoup

# 上糗事百科爬取热门内容,按回车键刷新 2016.03.27




def read_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        print('成功登录')
    else:
        print(response)
    soup = BeautifulSoup(response.content, 'lxml')
    # print(soup.prettify())
    jokes = soup.select('div.article')

    for each in jokes:
        if str(each).find('thumb') != -1:
            # print("找到一个带图的,跳过")
            pass
        else:
            print(each.select('div.content')[0].get_text().strip())



pageNum = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(pageNum)
print(url)
read_one_page(url)
while 1:
    print('_______________分割线_________________')
    char = input("输入Q退出程序")
    if char == 'Q':
        break
    pageNum += 1
    url = 'http://www.qiushibaike.com/hot/page/' + str(pageNum)
    read_one_page(url)





