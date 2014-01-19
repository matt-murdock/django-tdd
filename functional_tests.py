from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_Wait(3)
    self.browser.get('http://localhost:8000')

  def tearDown(self):
    self.browser.quit()

  def test_title_is_todo(self):
    self.assertIn('To-Do', self.browser.title)

if __name__ == '__main__':
  unittest.main(warnings='ignore')