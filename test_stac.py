import os
import pytest
from appium import webdriver

# let's define some constants
PLATFORM = 'Android'
PLATFORM_VERSION = '8'
DEVICE = 'Android Emulator'
AUTOMATION_NAME = 'UiAutomator2'
# get apk path
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
# appium local development host
HOST = 'http://localhost:4723/wd/hub'
WAIT_TIME = 5000

class TestJumoStacApp:
    @pytest.fixture(scope='function')
    def driver(self, request):
        settings = {
            # 'appPackage': 'world.jumo.now',
            # 'appActivity': '.MainApplication',
            'platformName': PLATFORM,
            'automationName': AUTOMATION_NAME,
            'platformVersion': PLATFORM_VERSION,
            'deviceName': DEVICE,
            # TODO: find a better way to load/find the apk
            'app': PATH('../../../work/eng-jumo-now-app/packages/jumo-now.apk')
        }
        # initialize webdriver
        app = webdriver.Remote(HOST, settings)
        # to deal with the fact that the splash screen takes some time
        app.implicitly_wait(WAIT_TIME)

        def fin():
            """teardown test(s)."""
            app.quit()

        request.addfinalizer(fin)
        return app

    def test_login(self, driver):
        el = driver.find_element_by_class_name('android.widget.TextView')
        el.click()
