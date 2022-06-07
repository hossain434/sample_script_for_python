from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver import Chrome

class View():

    def __init__(self, driver=None,options=None):
        chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        #options.set_headless = True
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
    def setUp(self):
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        print(self.driver.title)
        self.driver.close()


if __name__ == '__main__':
    View().setUp()
