from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.VCPage import VCPage


class HomePage(BasePage):

    HEADER = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/h3[1]")
    ACCOUNT_NAME = (By.XPATH, "/html/body/div/div[2]/div[1]/div[1]/div/p")
    VIDEO_CONF = (By.CSS_SELECTOR, "div[class='text-gray-cool3 font-semibold text-base']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def get_header_value(self):
        if(self.is_visible(self.HEADER)):
            return self.get_elements_text(self.HEADER)

    def get_account_name_value(self):
        if(self.is_visible(self.ACCOUNT_NAME)):
            return self.get_elements_text(self.ACCOUNT_NAME)

    def is_video_conf_link_exist(self):
        return self.is_visible(self.VIDEO_CONF)

    def do_start_video_conf(self):
        self.do_click(self.VIDEO_CONF)
        return VCPage(self.driver)