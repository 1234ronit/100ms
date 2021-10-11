from time import sleep
import pyautogui as P
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage


class VCPage(BasePage):

    NAME = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[4]/input")
    JOIN = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div/button")

    MUTE_BUTTON_AT_JOIN_CONF = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[1]/button[1]")

    VIDEO_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/button[1]/*[name()='svg'][1]/*[name()='path'][1]")
    VIDEO_1 = (By.XPATH, "/html/body/div[5]/div[3]/ul/li/div[2]/div/div[2]/div[1]")
    VIDEO_FILE = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/video[1]")

    AUDIO_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/button[1]/*[name()='svg'][1]")
    AUDIO_1 = (By.XPATH, "/html/body/div[5]/div[3]/ul/li/div[2]/div/div[2]/div[1]/div/span[1]")
    AUDIO_FILE = (By.XPATH, "/html/body/div[5]/div[3]/ul/li/div[2]/div/div[3]/div[1]/div[2]")

    PEERLIST_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/div[1]")
    PEER_LINK_1 = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]")

    TEXT_MESSAGE_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/button[2]/*[name()='svg'][1]")
    TEXT_MESSAGE_BOX = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[3]/textarea")
    TEXT_SEND_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[3]/button")

    TEXT_MESSAGE_RECEIVE = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div")

    SCREEN_SHARE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/button[3]")

    SETTINGS_BUTTON_2 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/span[2]/div[2]/div[1]/button")
    CHANGE_ROLL_HOST_TO_GUEST_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/span[2]/div[2]/div[1]/button")
    CONFIRM_BUTTON = (By.XPATH, "/html/body/div[5]/div[3]/div/div/div[5]/button")

    ACCEPT_BUTTON_AT_HOST = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/div/div/div/div/div[3]/div/button")

    SCREEN_SHARE_CONF_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/h1")
    SCREEN_SHARE_CONF_NOTIFICATION = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/span")


    def __init__(self, driver):
        super().__init__(driver)


    def do_join_video_conf(self, username):
        #result = self.is_visible(self.VIDEO)
        #self.do_click(self.JOIN)
        sleep(5)
        self.do_click(self.MUTE_BUTTON_AT_JOIN_CONF)
        self.do_send_keys(self.NAME, username)
        self.do_click(self.JOIN)
        sleep(5)


    def get_video_playback(self):
        self.do_click(self.VIDEO_BUTTON)
        self.do_click(self.VIDEO_1)
        return self.is_visible(self.VIDEO_FILE)

    def get_audio_playback(self):
        self.do_click(self.AUDIO_BUTTON)
        self.do_click(self.AUDIO_1)
        return self.is_visible(self.AUDIO_FILE)
            
    def get_peerlist(self):
        sleep(5)
        self.do_click(self.PEERLIST_BUTTON)
        sleep(5)
        return self.is_visible(self.PEER_LINK_1)

    def send_text_message(self, text_message):
        sleep(5)
        self.do_click(self.TEXT_MESSAGE_BUTTON)
        self.do_send_keys(self.TEXT_MESSAGE_BOX, text_message)
        self.do_click(self.TEXT_SEND_BUTTON)
        sleep(10)

    def get_text_message_confirmation(self):
        sleep(5)
        self.do_click(self.TEXT_MESSAGE_BUTTON)
        if (self.is_visible(self.TEXT_MESSAGE_RECEIVE)):
            return self.get_elements_text(self.TEXT_MESSAGE_RECEIVE)

    def start_screen_share(self):
        self.do_click(self.SCREEN_SHARE_BUTTON)
        P.moveTo(650, 350)
        P.rightClick()
        sleep(5)
        P.moveTo(1200, 710)
        #P.rightClick()
        P.doubleClick()
        sleep(5)
        if (self.is_visible(self.SCREEN_SHARE_CONF_MESSAGE)):
           return self.get_elements_text(self.SCREEN_SHARE_CONF_MESSAGE)

    def change_roll_from_host_to_get(self):
        sleep(5)
        self.do_click(self.PEERLIST_BUTTON)
        self.do_click(self.CHANGE_ROLL_HOST_TO_GUEST_BUTTON)
        sel = Select(self.driver.find_element_by_id("role-change-select-menu"))
        sel.select_by_value('guest')
        sleep(5)
        self.do_click(self.CONFIRM_BUTTON)

    def accept_change_roll_at_host(self):
        self.do_click(self.ACCEPT_BUTTON_AT_HOST)
        if (self.is_visible(self.SCREEN_SHARE_CONF_NOTIFICATION)):
            return self.get_elements_text(self.SCREEN_SHARE_CONF_NOTIFICATION)


