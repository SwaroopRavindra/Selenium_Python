from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path=r"C:\Users\Swaroop\Desktop\Selenium\Drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

print("Title:",driver.title)                     #Welcome: Mercury Tours
print("Current url:",driver.current_url)         #http://newtours.demoaut.com/
print(driver.page_source)                        #HTML code for the page

#LINKS:
links=driver.find_elements(By.TAG_NAME,"a")
print("Number of links present : ", len(links))
print("The links are :" )
for link in links:
    print(links.text)

#Clicking on the link:
driver.find_element(By.LINK_TEXT,"REGISTER").click()
driver.back()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()
driver.back()

#CONDITIONAL COMMANDS:
user=driver.find_element_by_name("userName")
print(user.is_displayed())                      #TRUE
print(user.is_enabled())                        #TRUE

pwd=driver.find_element_by_name("password")
user.send_keys("mercury")
pwd.send_keys("mercury")
driver.find_element_by_name("login").click()

print("Roundtrip radiobutton selected? :",driver.find_element_by_css_selector("input[value=roundtrip]").is_selected())     #TRUE
print("Oneway radiobutton selected? :",driver.find_element_by_css_selector("input[value=oneway]").is_selected())           #FALSE

#SELECTING RADIO BUTTON AND DROPDOWN:
driver.find_element_by_css_selector("input[value=oneway]").click()      #radiobutton selected

passengers= driver.find_element_by_css_selector("select[name=passCount]")
drp= Select(passengers)
drp.select_by_index(1)                                                  #3 ways of seleccting dropdown
#drp.select_by_value("1")
#drp.select_by_visible_text(1)

print(len(drp.options))                                                 #Count number of options

all_options=drp.options                                                 #Display all options of dropdown

for option in all_options:
    print(option.text)

driver.find_element_by_name("findFlights").click()

#driver.close()                  #closes currently focused tab
#driver.quit()                   #quits entire window(all tabs)