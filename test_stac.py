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
        # to give the splash screen time to load
        app.implicitly_wait(WAIT_TIME)

        def fin():
            """teardown test(s)."""
            app.quit()

        request.addfinalizer(fin)
        return app

    def test_login(self, driver):
        driver.find_element_by_android_uiautomator('text("English")').click()
        driver.find_element_by_id('7c48e2b8-a788-497e-b31c-0b7339d656ff').click()
        driver.find_element_by_android_uiautomator('text("ALLOW")').click()

        el = driver.find_elements_by_class_name('android.widget.TextView')
        assert 'You can get an instant loan on your phone.' == el[1].text
