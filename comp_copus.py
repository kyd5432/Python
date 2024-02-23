import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
import random
from selenium.webdriver.common.keys import Keys
import time
import os
import csv
import threading
import schedule
import requests

from bs4 import BeautifulSoup

fileinfo = (os.path.join(os.path.abspath('') , 'file_info.txt'))

f = open('file_info.txt', 'w')
f.write("0")
f.close()

id = "kyd54312@gmail.com"
pw = "~12tjalrud"



headless = 0
option = Options()

paynow = "on"
timestamps = {}
timeok = False
date_rev = True  #처음으로 예약 시도 할때 True

startime = "23:59" #"23:59"
resetime = "00:00" #"00:00"
formatted_time = []


option = Options()

if headless == 1:
    option.add_argument('--headless')
option.add_argument("--window-size=500,800")
option.add_argument("--user-data-dir=C:\\temp\\camp_uak_refactory_test")

option.add_experimental_option("excludeSwitches", ["enable-logging"])  # 불필요한 메세지 제거
option.add_experimental_option("excludeSwitches", ["enable-automation"])  # 자동화 메세지 제거

option.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=option)

# chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
# try:
#     driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
# except:
#     chromedriver_autoinstaller.install('./')
#     driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

driver.implicitly_wait(2)



timerandom = [9, 3, 5, 10, 12]
chilist = [2, 1]  #[2, 1]
chilist_b = [13, 11, 12]
urllist = {"c":"ContentMain_rptOptionZone_rptOption_2_lblSiteStatus_"}


# urllist = {"c":"ContentMain_rptOptionZone_rptOption_2_lblSiteStatus_",
#            "d":"ContentMain_rptOptionZone_rptOption_1_lblSiteStatus_"}


date_fin_reserv = open('C:/Python/camp_unak/camp_unak_date_reserv.txt', mode='r', encoding='UTF8')
date_fin = open('C:/Python/camp_unak/camp_unak_date.txt', mode='r', encoding='UTF8')

if date_rev == True:

    with date_fin_reserv as f:
        for line in f:
            pass
        last_line = line

    cardNo_1 = last_line[0:2]
    cardNo_2 = last_line[2:4]
else:

    with date_fin as f:
        for line in f:
            pass
        last_line = line

    cardNo_1 = last_line[0:2]
    cardNo_2 = last_line[2:4]


filepath = r"C:/Python/camp_unak/camp_unak_date.txt"
timestamp = os.path.getmtime(filepath)



dateday = [cardNo_1, cardNo_2] #[12, 2]
url = "https://www.campunak.co.kr/Reservation2/Reservation_Site.aspx"
driver.get(url)


#로그인
try:
    driver.find_element(By.ID, "ContentMain_txtUserID").send_keys(id)
    time.sleep(0.5)
    driver.find_element(By.ID, "ContentMain_txtUserPW").send_keys(pw)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'next_btn').click()
    time.sleep(0.5)

except:
    pass

time.sleep(0.3)
driver.find_element(By.NAME, "ctl00$ContentMain$txtSdate").send_keys(Keys.ARROW_RIGHT)
driver.find_element(By.NAME, "ctl00$ContentMain$txtSdate").send_keys(Keys.ARROW_RIGHT)
driver.find_element(By.NAME, "ctl00$ContentMain$txtSdate").send_keys(dateday[1])
time.sleep(0.3)

driver.find_element(By.NAME, "ctl00$ContentMain$txtSdate").send_keys(Keys.ARROW_RIGHT)
driver.find_element(By.NAME, "ctl00$ContentMain$txtSdate").send_keys(dateday[0])
time.sleep(0.3)

driver.find_element(By.NAME, "ctl00$ContentMain$txtEdate").send_keys(Keys.ARROW_RIGHT)
driver.find_element(By.NAME, "ctl00$ContentMain$txtEdate").send_keys(dateday[0])

time.sleep(0.3)
driver.find_element(By.NAME, "ctl00$ContentMain$txtEdate").send_keys(Keys.ARROW_RIGHT)
driver.find_element(By.NAME, "ctl00$ContentMain$txtEdate").send_keys(Keys.ARROW_RIGHT)
driver.find_element(By.NAME, "ctl00$ContentMain$txtEdate").send_keys(int(dateday[1]) + 2)





if timeok == True:     #정해진시간에 예약을 할것인가 확인
    chaktime = False

    timechspslow = False


    def my_function():

        global timechspslow
        timechspslow = True


    def my_function1():
        global chaktime, timeok

        chaktime = True


    # schedule.every().day.at(startime).do(my_function)

    schedule.every().day.at(startime).do(my_function)
    schedule.every().day.at(resetime).do(my_function1)

    while True:
        schedule.run_pending()
        if timechspslow == False:
            time.sleep(5)
        else:
            time.sleep(0.2)

        if chaktime == True:
            timeok = False
            break

#
# ###제거 해야할 부분



# driver.find_element(By.NAME, "ctl00$ContentMain$txtEdate").send_keys(Keys.ARROW_RIGHT)
# driver.find_element(By.NAME, "ctl00$ContentMain$txtEdate").send_keys('05')
# time.sleep(0.3)
# driver.find_element(By.NAME, "ctl00$ContentMain$txtEdate").send_keys(Keys.ARROW_RIGHT)
# driver.find_element(By.NAME, "ctl00$ContentMain$txtEdate").send_keys(Keys.ARROW_RIGHT)
# driver.find_element(By.NAME, "ctl00$ContentMain$txtEdate").send_keys('01')







finy = None  #예약이 최종 완료 될때 True 일경우 최종 탈출을 위한 변수
onsite= False
timechake = False


onetime = False

onestartime = ["12:59:50","13:01:05"]

# onestartime = "12:59" #"23:59"
# oneresetime = "13:01" #"00:00"


def mesg(content, msg):
    DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1100003376202252359/KPl7wFjVfB0D8Q6yob6xo6W7Nbu1PAejU5CKNCtsHQ5GpFSaTdiV8et1zRuR30i1Nvl7'
    message = {content: msg}
    requests.post(DISCORD_WEBHOOK_URL, data=message)

def my_function2():
    global onetime
    onetime = True

def my_function3():
    global onetime
    onetime = False

schedule.every().day.at(onestartime[0]).do(my_function2)  #오후 1시
schedule.every().day.at(onestartime[1]).do(my_function3)  #오후 1시


driver.find_element(By.CLASS_NAME, 'btntext').click()


elements  = driver.find_elements(By.XPATH, ("//*[contains(@id, 'ContentMain_rptOptionZone_rptOption')]"))


# 결과 출력
for element in elements:
    if '선택가능' in element.text.strip():
        if 'B12' in element.text.strip():
            print("B15자리발생")

        # print(element.get_attribute('option'))
    # print('ID:', element.get_attribute('option'))
    # print('ID:', element.get_attribute('text'))
    # print(element.text.strip())

# for site in site_list:
#
#     option_value = site.get_attribute('option')
#     print(option_value)
# soup = BeautifulSoup(html, 'html.parser')

# # '선택가능' 상태인 사이트를 찾습니다.
# available_sites = soup.find_all('span', string='선택가능')
#
# for site in available_sites:
#     # 상위 요소(<li>)를 찾아서 사이트 코드를 출력합니다.
#     site_code = site.find_previous_sibling('span', class_='payamount').text
#     print(site_code)
#
# time.sleep(10000)


#
# while True:
#       # 랜덤하게 타임 슬립을 만듬
#
#     try:
#
#         driver.find_element(By.CLASS_NAME, 'btntext').click()
#
#         if onetime:
#             time.sleep(1)
#             print("1초타임")
#
#
#         else:
#             rtime = random.choice(timerandom)
#             time.sleep(rtime)
#             print("랜덤타임")
#         schedule.run_pending()
#
#         text00 = driver.find_element(By.ID, 'ContentMain_lblReserCnt').text
#
#
#         if "없음" in text00:
#             timechake = False
#             pass
#
#         else:
#             if timechake == False:
#                 current_time = time.localtime()
#                 formatted_time = time.strftime("%m.%d %H:%M", current_time)
#                 f = open('C:/Python/camp_unak/camp_history.txt', 'a')
#                 f.write(formatted_time + '\n')
#                 f.close()
#
#
#                 timechake = True
#
#             for urltitle in urllist.keys(): #urllist
#                 def abcd(urltitle, chilists):
#                     global finy, onsite
#                     scurl1 = str(urllist[urltitle]) + str(chilists)  # urllist urltitle 값 + 사이트 변수 항목을 스트링으로 더함
#                     si = driver.find_element(By.ID, scurl1).text
#
#                     if "선택가능" in si and onsite == False:  #onsite  빈자리가 선택되면 멈춤을 확인하기 위함
#
#                         driver.find_element(By.ID, scurl1).click()
#                         time.sleep(0.2)
#                         driver.find_element(By.XPATH, '//*[@id="ContentMain_divRsrv"]/div[4]/label').click()
#                         time.sleep(0.2)
#                         driver.find_element(By.XPATH, '//*[@id="ContentMain_divRsrv"]/div[5]/label').click()
#                         time.sleep(0.2)
#
#                         if paynow == "on":
#                             driver.find_element(By.CLASS_NAME, 'next_btn').click()  # 예약 최종
#
#                             onsite = True
#                             finy = True  # finy는  while 문을 멈추기 위함
#
#                         msg = "캠프운악"+urltitle + "싸이트" + "_" + str(chilists + 1) +" "+"예약됨"
#                         print(msg)
#                         # if telegram_option == 1:
#                         #     bot.send_message(chat_id=chat_id, text=msg)
#
#                     else:
#                         # print(urltitle+"싸이트없음")
#                         pass
#                     return finy
#
#                 if finy == True:
#                     break
#
#                 if "c" == urltitle:  # c 싸이트 검색
#                     for chilists in chilist:  # 싸이트 검색횟수만큼 반복
#                         abcd(urltitle, chilists)  # 1번째 항목 c 싸이트, 2번째 항목 싸이트 자리를 abcd 변수에 던저 call
#
#                 if "d" == urltitle:  # b 싸이트 검색
#                     for chilists in chilist_b:
#                         abcd(urltitle, chilists)
#
#
#     except:
#         msg = "캠프운악 코드에러 중지합니다."
#         mesg('content', msg)
#         print(msg)
#         break
#
#
#     if finy == True:
#         break

driver.quit()


#
# def thread_fnc12(a):
#     f = open('file_info.txt', 'w')
#     f.write(a)
#     f.close()


