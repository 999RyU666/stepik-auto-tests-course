from selenium import webdriver
import time 
import math

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
   browser = webdriver.Chrome()
   browser.get(link)
   chest = browser.find_element_by_id("treasure")
   x = chest.get_attribute("valuex")
   y = calc(x)
   answer = browser.find_element_by_id("answer")
   answer.send_keys(y)
   checkbox = browser.find_element_by_id("robotCheckbox")
   checkbox.click()
   radio = browser.find_element_by_id("robotsRule")
   radio.click()
   button = browser.find_element_by_css_selector("[type='submit']")
   button.click()
   print(x)

finally:
   time.sleep(10)
   browser.quit()