from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("/Users/rojina/Desktop/software-engineering/raw selenium/chromedriver")
driver.get("https://www.google.com/maps")
sleep(2)


def searchPlace():
  place = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/form/input[1]")
  place.send_keys("University of Oxford")
  submit = driver.find_element(By.XPATH,'//*[@id="searchbox-searchbutton"]')
  submit.click()

searchPlace()
sleep(30)








def directions():
  sleep(30)

directions()
