from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
   browser = webdriver.Chrome()
   browser.get(link)
   num = browser.find_element_by_id("input_value").text
   x = calc(int(num))
   button = browser.find_element_by_tag_name("button")
   browser.execute_script("return arguments[0].scrollIntoView(true);", button)
   answer = browser.find_element_by_id("answer")
   answer.send_keys(str(x))
   checkbox = browser.find_element_by_id("robotCheckbox")
   checkbox.click()
   radio = browser.find_element_by_id("robotsRule")
   browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
   radio.click()
   button = browser.find_element_by_css_selector("button")
   button.click()

finally:
   time.sleep(30)
   browser.quit()