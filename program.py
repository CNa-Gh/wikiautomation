from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")


english = driver.find_element_by_id("js-link-box-en")
english.click()
search = driver.find_element_by_id("searchInput")
search.send_keys("medes")
search.send_keys(Keys.DOWN)
search.send_keys(Keys.RETURN)



time.sleep(100)
driver.close()