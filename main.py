import time
from selenium import webdriver
from gameclass import aigamebot
from selenium.webdriver.common.by import By
import random


numlist = []
driver = webdriver.Chrome()

aigame = aigamebot()
driver.get("https://nebin007.github.io/JavascriptNumbergame/")

choicebuttons = [driver.find_element(By.XPATH,"//div[@class='d-flex flex-column']//button[@class='btn btn-outline-danger btn-lg']"),
                    driver.find_element(By.XPATH,"//div[@class='d-flex flex-column']//button[@class='btn btn-outline-primary btn-lg']")]
time.sleep(2)
random.choice(choicebuttons).click()
time.sleep(3)

while(driver.find_elements(By.XPATH,"//div[@class='d-flex flex-row justify-content-center']//button[@type = 'button']")):
    numlist.clear()
    numberbnts = driver.find_elements(By.XPATH,"//div[@class='d-flex flex-row justify-content-center']//button[@type = 'button']")
    for x in numberbnts:
        numlist.append(int(x.get_attribute("innerText")))
    aiscr = driver.find_element(By.XPATH,"//div[@class='d-flex flex-row justify-content-center']//p[@id='aiscore']").get_attribute("innerText")
    hscr = driver.find_element(By.XPATH,"//div[@class='d-flex flex-row justify-content-center']//p[@id='humanscore']").get_attribute("innerText")
    aigame.setvals(numlist,hscr,aiscr)
    bestnum = aigame.comp_act()
    for x in numberbnts:
        if bestnum == int(x.get_attribute("innerText")):
            x.click()
            break
    print(aigame)
    time.sleep(5)
