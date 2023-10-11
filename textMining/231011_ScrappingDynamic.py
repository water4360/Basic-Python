# https://www.coffeebeankorea.com/store/store.asp
# storePop2('매장번호')
# 23/10/11 기준 1 ~ 388, 단 중간에 번호누락은 try~catch 쓰는 것으로.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

import time
import pandas as pd

def main():
    #크롬 WebDriver 객체 생성
    wdriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    result_list = []

    for storeNo in range(1, 389):
        #매장번호 1 ~388
        url = 'https://www.coffeebeankorea.com/store/store.asp'
        # 스크립트 실행할 url 열기
        wdriver.get(url)
        time.sleep(1)
        try:
            #스크립트 실행하기
            wdriver.execute_script(f"storePop2('{storeNo}')")
            time.sleep(1)
            html_doc = wdriver.page_source

            # BeautifulSoup으로 스크래핑scrapping
            soup = BeautifulSoup(html_doc, 'html.parser')
            # print(soup.prettify())

            # div클래스의 store_txt를 선택
            store_name = soup.select('div.store_txt > h2')[0].string
            store_info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
            # store_info
            # [0]영업시간 [1]주차 [2]주소 [3]전화
            store_optime = store_info[0].string
            store_address = list(store_info[2])[0].strip()
            store_phone = store_info[3].string
            store_info_list = [store_name, store_phone, store_address, store_optime]
            print(storeNo, store_info_list) # 확인용
            result_list.append(store_info_list)
        except:
            continue

    # DataFrame으로 만들기
    data_df = pd.DataFrame(result_list, columns=['name', 'phone', 'address', 'optime'])

    # csv 파일로 저장하기
    data_df.to_csv('231011_커피빈매장정보.csv', encoding='utf-8')
    return

if __name__ == '__main__':
    main()

