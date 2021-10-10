from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Home(BaseTest):

    def test_home_page_video_conf(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        self.homePage.do_start_video_conf()





    """
    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_account(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        account = homePage.get_account_name_value()
        assert account == TestData.HOME_PAGE_ACCOUNT

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homePage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER
    """

