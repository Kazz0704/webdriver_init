from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from twilio.rest import Client
import time
import datetime


# -----------------開啟官網--------------------------------------------------------

accountSid = ""
authToken = ""
driver = webdriver.Chrome("./chromedriver")
url = ('https://sschool.tp.edu.tw/Login.action?schNo=353301')
driver.get(url)
driver.maximize_window()
time.sleep(1)

# -----------------登入--------------------------------------------------------
entrance = driver.find_element_by_xpath(
    "/html/body/div[1]/section[1]/div/div[2]/div[1]/div/div[1]/a")
entrance.click()

time.sleep(1)
account = driver.find_element_by_xpath(
    "/html/body/div/div/div[2]/div/form/div/div/div[4]/div[1]/div/div/input")
account.send_keys("")

password = driver.find_element_by_xpath(
    "/html/body/div/div/div[2]/div/form/div/div/div[4]/div[2]/div/div/input")
password.send_keys("")

enter = driver.find_element_by_xpath(
    "/html/body/div/div/div[2]/div/form/div/div/div[6]/div[1]/button")
enter.click()

time.sleep(2)
ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# -----------------找尋目標資訊--------------------------------------------------------

toggle_down = driver.find_element_by_xpath(
    "/html/body/div[1]/nav/div[1]/div/ul/li[2]/a")
toggle_down.click()

grade_entrance = driver.find_element_by_xpath(
    "/html/body/div[1]/nav/div[1]/div/ul/li[2]/div/div/li[1]/a")
grade_entrance.click()

time.sleep(2)
tr_3_down = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table/tbody/tr[2]/td[2]")
tr_3_down.click()

time.sleep(2)

td_3_down_1 = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[1]/td[1]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[5]")
td_3_down_1.click()

time.sleep(2)
# -----------------擷取資訊--------------------------------------------------------

atitle = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[2]/td/div/div[3]/div[3]/div/table/tbody/tr[2]/td[5]").text

btitle = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[2]/td/div/div[3]/div[3]/div/table/tbody/tr[3]/td[5]").text

ctitle = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[2]/td/div/div[3]/div[3]/div/table/tbody/tr[4]/td[5]").text
dtitle = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[2]/td/div/div[3]/div[3]/div/table/tbody/tr[5]/td[5]").text

td_3_down_1_ch = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[2]/td/div/div[3]/div[3]/div/table/tbody/tr[2]/td[6]").text

td_3_down_1_en = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[2]/td/div/div[3]/div[3]/div/table/tbody/tr[3]/td[6]").text

td_3_down_1_math = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[2]/td/div/div[3]/div[3]/div/table/tbody/tr[4]/td[6]").text
td_3_down_1_his = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[2]/td/div/div[3]/div[3]/div/table/tbody/tr[5]/td[6]").text
# -----------------發送簡訊--------------------------------------------------------

content = "段考成績通知:"+"\n"+atitle+td_3_down_1_ch+"\n"+btitle + \
    td_3_down_1_en+"\n"+ctitle+td_3_down_1_math + \
    "\n"+dtitle+td_3_down_1_his+"\n"+"成績以成績通知單為準"
print(content)

if td_3_down_1_ch == " " or td_3_down_1_en == " " or td_3_down_1_math == " " or td_3_down_1_his == " ":
    pass
else:
    client = Client(accountSid, authToken)
    message = client.messages.create(
        from_="+13868547807",
        to="+886909627368",
        body=content
    )
driver.close()
