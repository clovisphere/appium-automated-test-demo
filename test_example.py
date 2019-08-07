import os
import pytest
from appium import webdriver

# let's define some constants
PLATFORM = 'Android'
PLATFORM_VERSION = '8'
DEVICE = 'Android Emulator'
AUTOMATION_NAME = 'UiAutomator2'
# returns absolute path relative to the file
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
# appium local development host
HOST = 'http://localhost:4723/wd/hub'
WAIT_TIME = 5000


class TestExampleApk:
    @pytest.fixture(scope='function')
    def driver(self, request):
        settings = {
            'platformName': PLATFORM,
            'automationName': AUTOMATION_NAME,
            'platformVersion': PLATFORM_VERSION,
            'deviceName': DEVICE,
            'app': PATH('/sample/ContactManager.apk')
        }
        # initialize webdriver
        app = webdriver.Remote(HOST, settings)
        # to give the splash screen time to load
        app.implicitly_wait(WAIT_TIME)

        def fin():
            """teardown test(s)."""
            app.quit()

        request.addfinalizer(fin)
        return app

    def test_add_contact(self, driver):
        el = driver.find_element_by_accessibility_id('Add Contact')
        el.click()
