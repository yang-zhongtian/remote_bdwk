from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os

url = r"https://wenku.baidu.com/view/ab397b2c2f3f5727a5e9856a561252d380eb203e.html"
print(os.getcwd())
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd()}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
WebDriverWait(driver, 30).until(lambda x:x.find_element_by_xpath("//div[contains(@class,'reader-download') and contains(@class,'btn-download')]")).click()
WebDriverWait(driver, 30).until(lambda x:x.find_element_by_xpath("//div[contains(@class,'dialog-down-load-btn-center') and contains(@class,'dialog-green')]/a")).click()
