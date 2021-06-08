from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.base_actions import BaseAction
from helpers.listener import DriverListener

class Browser(BaseAction):

    def __init__(self, mode=None, name_browser='chrome'):
        """Драйвер браузера Хром имеет листенер для отслеживания действия"""
        self.mode = mode
        self.name_browser = name_browser
        # выбор режима
        if self.mode is None:
            # выбор браузера
            if self.name_browser == 'chrome':
                chromer = ChromeDriverManager().install()
                self.driver = EventFiringWebDriver(driver=WebDriver(chromer), event_listener=DriverListener())
        elif self.mode == 'headless':
            pass

    def open(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    def close(self):
        self.driver.quit()