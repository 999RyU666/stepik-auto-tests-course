from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
   browser.get(link)
   button = browser.find_element_by_id("book")
   price = browser.find_element_by_id("price")
   WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
   button.click()
   input_value = browser.find_element_by_id("input_value").text
   y = calc(input_value)
   answer = browser.find_element_by_id("answer")
   answer.send_keys(y)
   button = browser.find_element_by_id("solve")
   button.click()

finally:
   time.sleep(10)
   browser.quit()