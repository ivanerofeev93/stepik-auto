from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    y_element = browser.find_element_by_xpath('//input[@id="answer"]')
    y_element.send_keys(y)
    #print(x, y)

    a_element = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    b_element = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    c_element = browser.find_element_by_xpath('//button[@class="btn btn-default"]')

    a_element.click()
    b_element.click()
    c_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

