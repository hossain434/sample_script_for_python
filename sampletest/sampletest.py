from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import chromedriver_autoinstaller
from selenium.webdriver import Chrome

class View():

    def __init__(self, driver=None,options=None):
        self.driver = webdriver.Remote(command_executor='http://172.17.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        #chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
    def setUp(self):
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        print(self.driver.title)
        self.driver.close()


if __name__ == '__main__':
    View().setUp()
