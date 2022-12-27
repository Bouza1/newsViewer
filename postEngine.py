import pickle
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome('chromedriver.exe')


def firstTime(usernamePlaceHolder, passwordPlaceHolder):
    cookieBtn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]")
    cookieBtn.click()
    firstLoginButton = driver.find_element(By.XPATH,
                                           "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a")
    firstLoginButton.click()
    time.sleep(10)
    usernameInput = driver.find_element(By.NAME, "text")
    usernameInput.click()
    usernameInput.send_keys(usernamePlaceHolder)
    time.sleep(3)
    nextBtn = driver.find_element(By.XPATH, "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                            "2]/div[2]/div/div/div/div[6]/div/span/span")
    nextBtn.click()
    time.sleep(5)

    verifyBox = driver.find_element(By.NAME, "text")
    twitterUsername = "Were_Autonomous"
    verifyBox.send_keys(twitterUsername)
    verifyBtn = driver.find_element(By.XPATH,
                                    "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div")
    verifyBtn.click()

    time.sleep(5)
    passwordInput = driver.find_element(By.NAME, "password")
    passwordInput.send_keys(passwordPlaceHolder)
    passwordBtn = driver.find_element(By.XPATH,
                                      "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div["
                                      "2]/div[2]/div/div[1]/div/div/div")
    passwordBtn.click()
    time.sleep(6)
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    driver.get("https://www.twitter.com")


def cookieLoadIn():
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        print(cookie)
        driver.add_cookie(cookie)
    driver.get("https://www.twitter.com")


def post4Me(newsUrl, title, hastags):
    # for image scirpt as in to add an image and post copy it from bota.java postrEnginge works perfectly
    # addPhotoBtn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div["
    #                                             "3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[1]")
    # addPhotoBtn.click()
    # time.sleep(2)
    # os.startfile("C:\\Users\\User\\PyProjects\\newsViewer\\Tools\\imgSelector4Twitter.exe")
    time.sleep(4)
    tweetBtnSideBar = driver.find_element(By.XPATH,
                                          "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
    tweetBtnSideBar.click();
    time.sleep(4)
    print("tweetBtnSideBar sucess")
    textInp = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div["
                                            "2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div["
                                            "1]/div/div/div/div/div/div[2]/div/div/div/div/label/div["
                                            "1]/div/div/div/div/div/div[2]/div/div/div/div/span")
    textInp.send_keys(title)
    textInp.send_keys(Keys.RETURN)
    textInp.send_keys(newsUrl)
    textInp.send_keys(Keys.RETURN)
    textInp.send_keys(hastags)

    finalPostBtn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div["
                                                 "2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div["
                                                 "3]/div/div/div[2]/div[4]")
    finalPostBtn.click()


username = "ENTER USERNAME"
password = "ENTER PASSWORD"


def start2Finish(newsUrl, Title, hashtags):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.twitter.com")
    cookieLoadIn()
    time.sleep(6)
    post4Me(newsUrl, Title, hashtags)


def firstTimeOR():
    file_exists = os.path.exists('cookies.pkl')
    if file_exists:
        cookieLoadIn()
        time.sleep(6)
    # post4Me(newsUrl, Title, hashtags)
    else:
        time.sleep(5)
        firstTime(username, password)


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
        driver.get("https://www.twitter.com")
        time.sleep(5)
        tweetBtnSideBar = driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        tweetBtnSideBar.click();
        time.sleep(4)
        print("tweetBtnSideBar sucess")
        textInp = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div["
                                      "2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div["
                                      "1]/div/div/div/div/div/div[2]/div/div/div/div/label/div["
                                      "1]/div/div/div/div/div/div[2]/div/div/div/div/span")
        textInp.send_keys(title)
        textInp.send_keys(Keys.RETURN)
        textInp.send_keys(newsUrl)
        textInp.send_keys(Keys.RETURN)
        textInp.send_keys(hashtags)

        finalPostBtn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div["
                                                     "2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div["
                                                     "3]/div/div/div[2]/div[4]")
        finalPostBtn.click()
