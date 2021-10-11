from time import sleep

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.VCPage import VCPage
from Tests.test_base import BaseTest

class Test_VC(BaseTest):

    def test_vc_page_video_conf(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        self.homePage.do_start_video_conf()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.vcPage = VCPage(self.driver)
        self.vcPage.do_join_video_conf(TestData.HOST)
        #self.driver.switch_to.window(self.driver.window_handles[0])


    def test_video_playback(self):
        self.test_vc_page_video_conf()
        flag = self.vcPage.get_video_playback()
        assert flag

    def test_audio_playback(self):
        self.test_vc_page_video_conf()
        flag = self.vcPage.get_audio_playback()
        assert flag

    def test_peer_list(self):
        self.test_vc_page_video_conf()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(5)
        self.homePage.do_start_video_conf()
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.vcPage.do_join_video_conf(TestData.GUEST_1)
        flag = self.vcPage.get_peerlist()
        assert flag

    def test_text_message(self):
        self.test_vc_page_video_conf()

        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(5)
        self.homePage.do_start_video_conf()

        self.driver.switch_to.window(self.driver.window_handles[2])
        self.vcPage.do_join_video_conf(TestData.GUEST_1)
        self.vcPage.send_text_message(TestData.TEXT_MESSAGE)

        self.driver.switch_to.window(self.driver.window_handles[1])
        receiver = self.vcPage.get_text_message_confirmation()
        assert receiver == TestData.TEXT_MESSAGE


    def test_role_change(self):
        self.test_vc_page_video_conf()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(5)
        self.homePage.do_start_video_conf()
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.vcPage.do_join_video_conf(TestData.GUEST_1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.vcPage.change_roll_from_host_to_get()

        self.driver.switch_to.window(self.driver.window_handles[2])
        receiver = self.vcPage.accept_change_roll_at_host()
        assert receiver == TestData.SCREEN_SHARE_CONF_NOTIFICATION


    def test_screen_share(self):
        self.test_vc_page_video_conf()
        receiver = self.vcPage.start_screen_share()
        assert receiver == TestData.SCREEN_SHARE_CONF_MESSAGE




    """
    def test_messaging(self):
        self.test_vc_page_video_conf()
        self.vcPage.send_text_message(TestData.TEXT_MESSAGE)
        receiver = self.vcPage.get_text_message_confirmation()
        assert receiver == TestData.TEXT_MESSAGE
    """


