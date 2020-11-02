from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from pjct.cm import main
from pjct.test import star_aut
import time
import requests
import re
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pjct.amazon_analyzer import predict_sent
from pjct.visualisation import main_twitter
from pjct.reddit import call_reddit
chromedriver="pjct/chromedriver"
driver=webdriver.Chrome(chromedriver)
def sentiment_cal(sentence):
    # sid_obj = SentimentIntensityAnalyzer()
    # sentiment_dict = sid_obj.polarity_scores(sentence)
    # if sentiment_dict['compound'] >= 0.05:
    #     return("Positive")
    # elif sentiment_dict['compound'] <= - 0.05:
    #     return("Negative")
    # else :
    #     return("Neutral")
    analysis=predict_sent(sentence)
    if analysis <0.35:
        return 'Negative'
    elif analysis >0.45:
        return 'Positive'
    else:
        return 'Neutral'

def plot_pie(p,neg,neu):
    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [p,neg,neu]
    explode = (0.1, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

def ten(lis,k):
    c=''
    for i in range(30):
        ind=lis.index(max(lis))
        c=c+(k[ind].strip())
        lis[ind]=0
    print(c)
    print('/n')
    sum=main(c)
    return sum

def main_part_pjct(n1):
    ret=[]
    p=0
    neg=0
    neu=0
    global sum_len
    sum_len=[]
    global summarize
    summarize=[]
    n=star_aut(n1)
    driver.get(n)
    sp=BeautifulSoup(driver.page_source,'html.parser')
    rev=sp.select('span#acrCustomerReviewText')
    print(rev)
    try:
        no_txt=rev[0].text
        no_t=''
        k=[i for i in no_txt if i.isdigit()]
        for m in k:
            no_t+=m
        no=int(no_t)
        print(no)
        x=int(no*0.04)
    except:
        x=80
    driver.get(n+'#customerReviews')
    but=driver.find_element_by_css_selector('#reviews-medley-footer > div.a-row.a-spacing-medium > a')
    but.send_keys(Keys.ENTER)
    but2=driver.find_element_by_css_selector('#cm_cr-pagination_bar > ul > li.a-last > a')
    but2.send_keys(Keys.ENTER)
    url=driver.current_url
    for i in range(2,x):
        if i>95:
            break
        print(url)
        if(i==10):
            url=url[0:len(url)-1]+str(i)
        elif(i==100):
            url=url[0:len(url)-2]+str(i)
        elif(i==1000):
            url=url[0:len(url)-3]+str(i)
        else:
            url=url[0:len(url)-len(str(i))]+str(i)
        req=requests.get(url)
        cont=req.content
        soup=BeautifulSoup(cont,'html.parser')
        s1=soup.findAll('span',class_='a-size-base review-text review-text-content')
        for i in s1:
            summarize.append(i.text)
            sum_len.append(len(i.text))
            st=sentiment_cal(i.text)
            if(st=='Positive'):
                p+=1
            elif(st=='Negative'):
                neg+=1
            else:
                neu+=1
    #summm=ten(sum_len,summarize)
    twi_l=main_twitter(n1)
    red_l=call_reddit(n1.replace(' ',''))
    #ret.append(summm)
    ret.append(0)
    ret.append(red_l[0])
    ret.append(red_l[1])
    ret.append(red_l[2])
    ret.append(p)
    ret.append(neg)
    ret.append(neu)
    ret.append(twi_l[0])
    ret.append(twi_l[1])
    ret.append(twi_l[2])
    return ret
    # main_twitter(n1)
    # plot_pie(red_l[0],red_l[1],red_l[2])
def summarize_t():
    try:
        summm=ten(sum_len,summarize)
        return summm
    except:
        summm=["you","have","to","analyze first","go back to first page and then come"]
        return summm
