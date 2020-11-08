import unittest
from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        input1 = browser.find_element_by_xpath('//input[contains(@class, "first") and contains(@placeholder, "name")]')
        input1.send_keys("Ivanov")

    def test_abs2(self):
        #self.assertEqual(abs(-42), 5, "Should be absolute value of a number")
        input2 = browser.find_element_by_xpath('//input[contains(@class, "second") and contains(@placeholder, "name")]')
        input2.send_keys("Ivan")

    def test_abs3(self):
        input3 = browser.find_element_by_xpath('//input[contains(@class, "third") and contains(@placeholder, "email")]')
        input3.send_keys("Smolensk")

if __name__ == "__main__":
    unittest.main()

time.sleep(3)
browser.quit()