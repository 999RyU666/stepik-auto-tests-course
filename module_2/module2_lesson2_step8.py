from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))    
file_path = os.path.join(current_dir, 'file.txt')

try:
   browser = webdriver.Chrome()
   browser.get(link)
   Fname = browser.find_element_by_css_selector("[name = 'firstname']")
   Fname.send_keys("First name")
   Lname = browser.find_element_by_css_selector("[name = 'lastname']")
   Lname.send_keys("Last name")
   Email = browser.find_element_by_css_selector("[name = 'email']")
   Email.send_keys("Email")
   File = browser.find_element_by_id("file")
   File.send_keys(file_path)
   Submit = browser.find_element_by_css_selector("[type = 'submit']")
   Submit.click()

finally:
   time.sleep(15)
   browser.quit()