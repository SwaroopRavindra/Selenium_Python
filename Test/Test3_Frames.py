from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver= webdriver.Chrome(r"C:\Users\Swaroop\Desktop\Selenium\Drivers\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(2)

driver.switch_to_default_content()

driver.switch_to_frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()

driver.close()


