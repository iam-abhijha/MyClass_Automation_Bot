# import webdriver
from selenium import webdriver
import time
driver = webdriver.Firefox()

driver.get("https://myclass.lpu.in/")

user_id = driver.find_element_by_name("i")
user_pass = driver.find_element_by_name("p")

user_id.send_keys("Reg_no")
user_pass.send_keys("Password")
user_pass.submit()

driver.implicitly_wait(10)
view_class = driver.find_element_by_xpath("//a[contains(text(),'View Classes/Meetings')]")
view_class.click()
time.sleep(20)

driver.implicitly_wait(5)
try:
    join = driver.find_element_by_xpath("//a[@class='btn btn-primary btn-block btn-sm']")
    time.sleep(100)
    print("Class Started")


except:
    print("Class not started, try after some time")
