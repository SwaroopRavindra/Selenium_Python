from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Swaroop\Desktop\Selenium\Drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.youtube.com/")
driver.find_element_by_name("search_query").send_keys("Draggers duke")
driver.find_element_by_id("search-icon-legacy").click()
