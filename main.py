import webbrowser
from tkinter import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from newsScraper import news2Array
import pickle
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os


def wholeScript(title, newsUrl, hashtags):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.twitter.com")
    time.sleep(5)
    file_exists = os.path.exists('cookies.pkl')
    if file_exists:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            print(cookie)
            driver.add_cookie(cookie)
        driver.get("https://twitter.com/compose/tweet")

        # time.sleep(5)
        # tweetBtnSideBar = driver.find_element(By.XPATH,
        #                                       "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        # tweetBtnSideBar.click();
        # time.sleep(4)
        # print("tweetBtnSideBar sucess")
        time.sleep(5)
        textInp = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div["
                                                "2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div["
                                                "1]/div/div/div/div/div/div[2]/div/div/div/div/label/div["
                                                "1]/div/div/div/div/div/div[2]/div/div/div/div/span")
        textInp.send_keys(title)
        time.sleep(1)
        textInp.send_keys(Keys.RETURN)
        print("return 1 passed")
        time.sleep(1)
        textInp.send_keys(newsUrl)
        textInp.send_keys(Keys.RETURN)
        print("return2 passed")
        time.sleep(1)
        textInp.send_keys(hashtags)
        time.sleep(4)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='react-root']/div/div/div[@id='layers']/div/div/div/div[@role='dialog']/div/div/div[@role='group']/div[@role='dialog']/div/div/div/div/div/div/div/div/div/div/div/div/div/div[@data-testid='toolBar']/div[2]/div[1]"))).click()
        # finalPostBtn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]")
        # finalPostBtn.click()

scrappedData = news2Array("technews", "week", 1000)

root = Tk()
root.title("Get(News) & Post(News)")
root.geometry('900x450')
root.configure(bg="black")

global i
i = 0


def nextStory():
    global i
    i = i + 1
    if i >= len(scrappedData):
        pass
    else:
        storyTitleLbl.configure(text=scrappedData[i][0])
        upvotesLbl.configure(text=scrappedData[i][2])


def prevStory():
    global i
    i = i - 1
    if i <= 0:
        pass
    else:
        storyTitleLbl.configure(text=scrappedData[i][0])
        upvotesLbl.configure(text=scrappedData[i][2])


def openStory():
    webbrowser.open(scrappedData[i][1])


def postArticle():
    wholeScript((storyTitleLbl['text']), (scrappedData[i][1]), "#WeAreAutonomous")


title = Label(root, text="Twitter News Bot")
title.grid()

prevBtn = Button(root, text="Back", command=prevStory)
prevBtn.grid(column=0, row=1)

todaysNewsLbl = Label(root, text="Todays Tech News")
todaysNewsLbl.grid(column=1, row=1)

nextBtn = Button(root, text="Next", command=nextStory)
nextBtn.grid(column=2, row=1)

upvotesLbl = Label(root, text="")
upvotesLbl.grid(column=0, row=2)

storyTitleLbl = Button(root, text="", command=openStory)
storyTitleLbl.grid(column=1, row=2)

urlLbl = Label(root, text="")
urlLbl.grid(column=1, row=3)

openArticleBtn = Button(root, text="Post", command=postArticle)
openArticleBtn.grid(column=1, row=4)

root.mainloop()
