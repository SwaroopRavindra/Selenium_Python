from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver= webdriver.Chrome(r"C:\Users\Swaroop\Desktop\Selenium\Drivers\chromedriver.exe")

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin= driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
um= driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users= driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions= ActionChains(driver)
actions.move_to_element(admin).move_to_element(um).move_to_element(users).click().perform()      #Mouse Hover action

driver.find_element_by_name("btnAdd").click()

driver.find_element_by_id("systemUser_employeeName_empName").send_keys("Ar Lee")
driver.find_element_by_id("systemUser_userName").send_keys("Swaroop")
role_selection = Select(driver.find_element_by_id("systemUser_userType"))
role_selection.select_by_index(0)

driver.find_element_by_name("btnSave").click()
driver.close()

