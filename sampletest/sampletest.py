from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver import Chrome

class View():
    def __init__(self, driver=None):
        # if driver is None:
        #     driver = {}
        # else:
            self.driver = driver
    chromedriver_autoinstaller.install()
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        print(self.driver.title)
        self.driver.close()


if __name__ == '__main__':
    View().setUp()
