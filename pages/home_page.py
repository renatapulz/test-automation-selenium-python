from selenium.webdriver.common.by import By
from urllib.parse import urlparse

class HomePage:
    URL = "https://practice.qabrains.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def click_menu(self, label):
        self.driver.find_element(By.LINK_TEXT, label).click()

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def url_matches(self, expected_url):
        current_parsed = urlparse(self.get_current_url())
        expected_parsed = urlparse(expected_url)
        return (
            current_parsed.netloc == expected_parsed.netloc and
            current_parsed.path.rstrip('/') == expected_parsed.path.rstrip('/')
        )

    def go_to_menu(self, label):
        self.click_menu(label)
        if len(self.driver.window_handles) > 1:
            self.switch_to_last_tab()