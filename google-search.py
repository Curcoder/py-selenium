import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import HtmlTestRunner

chrome_options = Options()
chrome_options.add_argument("--headless")


# Use the unittest.TestCase to turn the class into a Test Case
class GoogleSearch(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://www.google.com')
        print('Setup executed')

    def test_verify_customer_search(self):
        self.assertTrue(self.driver.find_element_by_class_name('gLFyf ').is_displayed(),
                        msg='Search field not displayed')
        print('Test 1 executed')

    def test_verify_search_btn(self):
        self.assertTrue(self.driver.find_element_by_xpath(
            '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').is_displayed(),
                        msg='Search field not displayed')
        print('Test 2 executed')

    def test_verify_lucky_btn(self):
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="gbqfbb"]').is_displayed(),
                        msg='Search field not displayed')
        print('Test 3 executed')

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.close()
        print('Teardown executed')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports',
        combine_reports=True,
        add_timestamp=False,
        report_name="TestReport"))

