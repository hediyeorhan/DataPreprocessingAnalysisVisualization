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
    yazı_girişi = browser.find_element_by_css_selector(".gLFyf.gsfi")
    yazı_girişi.send_keys("tc sağlık bakanlığı twitter")
    time.sleep(2)
    yazı_girişi.send_keys(Keys.ENTER)

    tıkla = browser.find_element_by_css_selector(".NsiYH")
    tıkla.click()

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
       

        sayfa_kaynağı = browser.page_source
        soup = BeautifulSoup(sayfa_kaynağı, "html.parser")
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

