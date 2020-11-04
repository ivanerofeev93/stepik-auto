from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath('//button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    a_value = browser.find_element_by_id("input_value")
    a = int(a_value.text)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(a))

    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()