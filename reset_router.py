from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def reset_router():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service("driver/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://192.168.1.1")
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "el-input__inner"))).send_keys("admin" + Keys.ENTER)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/ul/li[5]/span'))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sideMenu"]/ul/div[2]/li/span'))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="reboot"]/form/button/span'))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="no-ie-9"]/body/div[2]/div/div[3]/button[2]/span'))).click()
    sleep(1)
    driver.quit()
