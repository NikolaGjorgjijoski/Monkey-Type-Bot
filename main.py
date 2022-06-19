from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import *
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
browser = webdriver.Chrome("PATH_TO_YOUR_CHROME_DRIVER")


url = 'https://monkeytype.com'

delay = 0.00075

browser.get(url)
button = browser.find_element_by_xpath('//*[@id="cookiePopup"]/div[2]/div[2]/div[1]').click()

def GetWord():
    try:
        words = browser.find_element_by_id("words")
        words = words.find_elements(by=By.TAG_NAME, value="div")
        for word in words:
            if "active" in word.get_attribute("class"):
                return word.text
        return False
    except:
        return False

time.sleep(10)

while True:
    time.sleep(delay)
    Word = GetWord()
    if not Word:
        time.sleep(delay)
    else:
        for letter in list(Word):
            keyboard.press(letter)
            time.sleep(delay)
        keyboard.press(Key.space)
        keyboard.release(Key.space)


