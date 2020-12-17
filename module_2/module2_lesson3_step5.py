from selenium import webdriver
import time
import math

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
   browser = webdriver.Chrome()
   browser.get(link)
   button = browser.find_element_by_css_selector("[type='submit']")
   button.click()
   new_window = browser.window_handles[1]
   browser.switch_to.window(new_window)
   input = browser.find_element_by_id("input_value").text
   x = calc(input)
   answer = browser.find_element_by_id("answer")
   answer.send_keys(x)
   submit = browser.find_element_by_css_selector("[type='submit']")
   submit.click()

finally:
   time.sleep(10)
   browser.quit()
   