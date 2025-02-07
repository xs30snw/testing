from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

def setUpModule():
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=browser-profile')
    # options.add_argument('--proxy-server=xxx.xxx.xxx.xxx')
    TestWithSelenium.driver = webdriver.Chrome(options=options)

def tearDownModule():
    TestWithSelenium.driver.quit()

class TestWithSelenium(unittest.TestCase):
    def test_hello_world(self):
        self.driver.get("http://127.0.0.1:5000")
        p = self.driver.find_element(By.TAG_NAME, "p")
        self.assertEqual(p.text, "Hello, World!")

if __name__ == "__main__":
    unittest.main()