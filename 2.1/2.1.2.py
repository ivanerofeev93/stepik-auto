from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")

    text_field = browser.find_element_by_xpath('//input[@id="answer"]')
    checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    radiobutton = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    submit_button = browser.find_element_by_xpath('//button[@type="submit"]')

    text_field.send_keys(calc(x))
    checkbox.click()
    radiobutton.click()
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()