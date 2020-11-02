from bs4 import BeautifulSoup
import requests as r
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromedriver="chromedriver"
driver=webdriver.Chrome(chromedriver)
driver.get("https://www.imdb.com/")
box=driver.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div[1]/form/div[2]/div/input')
box.send_keys('Baahubali 2')
button=driver.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div[1]/form/button')
button.click()
time.sleep(2)
but=driver.find_element_by_css_selector('#main > div > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.result_text > a')
but.send_keys(Keys.ENTER)
time.sleep(10)
url=driver.current_url
print(url)
d=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[3]/div[9]/div/a[2]')
d.send_keys(Keys.ENTER)
time.sleep(10)
b=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/section/div[2]/div[4]/div/button')
b.click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
soup=BeautifulSoup(driver.page_source,"html.parser")
s=soup.findAll('div',class_='text show-more__control')
print(s)
# for i in s:
#     print(i.text)
# s=driver.find_element_by_css_selector('#SONG_smoothScroll > li:nth-child(1) > div.railContent.w-100.float-left.pt-2 > a')
# href=s.get_attribute('href')
# print(href)
# driver.get(href)
# button=driver.find_element_by_xpath('/html/body/app-root/app-home/div[2]/div/song-info/div/div[1]/div[3]/div[2]/div[1]/button[1]')
# button.click()
# for i in range(5):
#     driver.execute_script("window.scrollTo(0,2000);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# time.sleep(10)
