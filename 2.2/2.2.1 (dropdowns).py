from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element_by_xpath('//span[@id="num1"]')
    a = int(a_element.text)
    b_element = browser.find_element_by_xpath('//span[@id="num2"]')
    b = int(b_element.text)
    c = a + b

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(c))

    submit = browser.find_element_by_xpath('//button[@class="btn btn-default"]')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()