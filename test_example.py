import pytest
from appium import webdriver

# let's define some constants
PLATFORM = 'Android'
PLATFORM_VERSION = '8'
DEVICE = 'Android Emulator'
AUTOMATION_NAME = 'UiAutomator2'
# absolute path to the apk, or the URL (if hosted somewhere on the internet)
APK_ABSOLUTE_PATH = ''
# appium local development host
HOST = 'http://localhost:4723/wd/hub'
WAIT_TIME = 5000


class TestExampleApk:
    @pytest.fixture(scope='function')
    def driver(self, request):
        settings = {
            # 'appPackage': 'world.jumo.now',
            # 'appActivity': '.MainApplication',
            'platformName': PLATFORM,
            'automationName': AUTOMATION_NAME,
            'platformVersion': PLATFORM_VERSION,
            'deviceName': DEVICE,
            'app': APK_ABSOLUTE_PATH
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

    def test_(self, driver):
        pass
