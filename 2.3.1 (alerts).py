from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath('//button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    a_value = browser.find_element_by_id("input_value")
    a = int(a_value.text)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(a))

    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
    print(a)