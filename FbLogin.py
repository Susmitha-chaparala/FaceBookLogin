from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='C:\\Users\\CH.SUSMITHA\\Anaconda3\\chromedriver.exe')
browser.get('https://www.facebook.com/')

user_id = input("Enter the user_id or phone_number:")
password = input("Enter password:")

print(user_id)
print(password)


ep = browser.find_element_by_id("email")
ep.send_keys(user_id)

pw = browser.find_element_by_id("pass")
pw.send_keys(password)

login = browser.find_element_by_id("u_0_b")
login.click()
