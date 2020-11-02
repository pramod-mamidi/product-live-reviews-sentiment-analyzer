from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
import re
def star_aut(n):
    chromedriver="pjct/chromedriver"
    driver=webdriver.Chrome(chromedriver)
    driver.get('https://www.amazon.in/')
    inp=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
    inp.send_keys(n)
    but=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
    but.click()
    soup=BeautifulSoup(driver.page_source,'html.parser')
    sel=soup.findAll('span',class_='a-size-medium a-color-base a-text-normal')
    for i in range(len(sel)):
        if n.lower() in (sel[i].text).lower():
            break
    sel1=soup.findAll('a',class_='a-link-normal a-text-normal')
    href=sel1[i].get('href')
    link='https://www.amazon.in'+href
    return link
