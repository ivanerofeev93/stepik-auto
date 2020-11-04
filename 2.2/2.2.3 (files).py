import os
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("ivan@mail.ru")

    file_button = browser.find_element_by_xpath('//input[@type="file"]')
    submit_button = browser.find_element_by_xpath('//button[@type="submit"]')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла

    file_button.send_keys(file_path)
    submit_button.click()

finally:
    time.sleep(7)
    browser.quit()

