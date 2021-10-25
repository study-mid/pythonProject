#step1.selenium 패키지와 time 모듈 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

#step2.검색할 키워드 입력
#query = input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://www.daangn.com/articles/297117247'
driver = webdriver.Chrome('C:/Users/chromedriver')
driver.get(url)
time.sleep(3)

#step4.검색창에 키워드 입력 후 엔터(X)
'''
search_box = driver.find_element_by_css_selector("input#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)
'''

#step5.개별 판매상품 클릭(보류)
#driver.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
#time.sleep(2)

#step6.뉴스 제목 텍스트 추출
item_titles = driver.find_element_by_id("article-title").text
item_details = driver.find_elements_by_id("article-detail")


#예) table item_data (item_title varchar2, item_detail long)
#data = pd.DataFrame(columns=[item_titles])
data = []

for i in item_details:
    i = i.text
detail = "".join(i)

list1 = [item_titles, detail]
data.append(list1)

print(data)

data = pd.DataFrame(data) #데이터 프레임으로 전환
data.to_excel('C:/Users/wranb/OneDrive/문서/Python&Algoritym Study/라라야.xlsx', index=False, header=False)


# 결과 출력
'''
print(item_titles)
for i in item_details:
    detail = i.text
print(detail)
'''

#step7.개별 판매상품 하이퍼링크 추출(보류)
'''for i in news_titles:
    href = i.get_attribute('href')
    print(href)'''