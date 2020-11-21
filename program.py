from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.wikipedia.org/")
search = driver.find_element_by_id("searchInput")
search.send_keys("medes")
time.sleep(1)
for element in driver.find_elements_by_xpath("//*[@id='typeahead-suggestions']/div/a/div[1]/h3"):
    if element.text.lower() == "medes islands":
        element.click()
        break
time.sleep(2)
spain = driver.find_element_by_xpath("//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[6]/td/a")
print(spain.get_attribute("href"))
driver.close()