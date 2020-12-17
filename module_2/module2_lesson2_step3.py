from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects2.html"

try:
   browser = webdriver.Chrome()
   browser.get(link)
   num1 = browser.find_element_by_id("num1").text
   x = int(num1)
   num2 = browser.find_element_by_id("num2").text
   y = int(num2)
   z = str(x+y)
   select = Select(browser.find_element_by_id("dropdown"))
   select.select_by_visible_text(z)
   button = browser.find_element_by_css_selector("button.btn")
   button.click()

finally:
   time.sleep(10)
   browser.quit()