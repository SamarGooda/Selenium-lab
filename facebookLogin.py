import unittest
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class TestPythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")

    def test_facebook_login(self):
        driver = self.driver
        driver.get('http://www.facebook.org')
        self.assertIn('Facebook', driver.title)
        email = driver.find_element_by_id("email")
        password = driver.find_element_by_id("pass")
        password.send_keys(Keys.RETURN)

        assert 'samar' in driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



email="enter your mail"
password="enter your password"
