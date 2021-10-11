from urllib import request

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import TestData


@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    #global web_driver
    if request.param == "chrome":
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
        })
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, chrome_options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()