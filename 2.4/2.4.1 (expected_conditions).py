from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button.click()

    a_value = browser.find_element_by_id("input_value")
    a = int(a_value.text)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(a))

    submit = browser.find_element_by_id("solve")
    submit.click()

finally:

    time.sleep(5)
    browser.quit()