import unittest
from selenium import webdriver

class WebdriverTests(unittest.TestCase):

    def setUp(self):
      options = webdriver.ChromeOptions()
      options.add_argument('--headless')
      options.add_argument('--no-sandbox')
      options.add_argument('--disable-gpu')
      options.add_argument('--disable-setuid-sandbox')
      self.browser = webdriver.Remote('http://chrome:4444/wd/hub', options=options)
      self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://app:8000')
        self.assertIn('foo', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
