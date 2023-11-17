from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


def veri_cek():
    sayfa = int(input("scroll sayısını girin = "))

    driver_path = "C:\Anaconda3\Lib\chromedriver.exe"
    browser = webdriver.Chrome(driver_path)

    browser.get("https://www.google.com.tr/")
    yazi_girisi = browser.find_element_by_css_selector(".gLFyf.gsfi")
    yazi_girisi.send_keys("tc sağlık bakanlığı twitter")
    time.sleep(2)
    yazi_girisi.send_keys(Keys.ENTER)

    tikla = browser.find_element_by_css_selector(".NsiYH")
    tikla.click()

    #
    file = open("tweetler.csv", "w", encoding="utf-8")
    writer = csv.writer(file)

    writer.writerow(["Tweetler", "YorumSayisi", "RetweetSayisi", "BegeniSayisi"])

    #
    a = 0
    while a < sayfa:
      
        lastHeight = browser.execute_script("return document.body.scrollHeight")
        i = 0
        while i < 1:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            newHeight = browser.execute_script("return document.body.scrollHeight")

            if newHeight == lastHeight:
                break
            else:
                lastHeight = newHeight

            i = i + 1
       

        sayfa_kaynagi = browser.page_source
        soup = BeautifulSoup(sayfa_kaynagi, "html.parser")
        tweetler = soup.find_all("div", attrs={"data-testid": "tweet"})

        for i in tweetler:

            try:

                yazi = i.find("div", attrs={
                    "class": "css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-1mi0q7o"}).text
                print(i.find("div", attrs={
                    "class": "css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-1mi0q7o"}).text)

                yorum_sayisi = i.find("div", attrs={"data-testid": "reply"}).text
                retweet_sayisi = i.find("div", attrs={"data-testid": "retweet"}).text
                begeni_sayisi = i.find("div", attrs={"data-testid": "like"}).text

                writer.writerow([yazi, yorum_sayisi, retweet_sayisi, begeni_sayisi])

            except:
                print("**")
        a = a + 1


veri_cek()



###########################################################################################################################################################

import time
import login
from selenium import webdriver

driver_path = "C:\Anaconda3\Lib\chromedriver.exe"

browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://twitter.com/")

time.sleep(3)

giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/a[2]")

giris_yap.click()

time.sleep(5)

username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
password = browser.find_element_by_xpath("//*[@id='react-root'']/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")

time.sleep(3)


login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")

login.click()

time.sleep(5)

searchArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")
searchButton = browser.find_element_by_xpath("//*[@id='global-nav-search']/span/button")



searchArea.send_keys("#ArtificialIntelligence")

searchArea.click()

time.sleep(5)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
tweets = []

elements = browser.find_elements_by_css_selector(".TweetTextSize.js-tweet-text.tweet-text")

for element in elements:
    tweets.append(element.text)

tweetCount = 1

with open("ai.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("**************************\n")
        tweetCount += 1

browser.close()


