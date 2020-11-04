from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value = browser.find_element_by_id("input_value")
    x = value.text

    text_field = browser.find_element_by_xpath('//input[@id="answer"]')
    checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    radiobutton = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    submit_button = browser.find_element_by_xpath('//button[@type="submit"]')

    browser.execute_script("return arguments[0].scrollIntoView(true);", text_field)

    text_field.send_keys(calc(x))
    checkbox.click()
    radiobutton.click()
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()