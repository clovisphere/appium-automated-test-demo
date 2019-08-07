import pytest
from appium import webdriver

# let's define some constants // change them accordingly
PLATFORM = 'Android'
PLATFORM_VERSION = '8'
DEVICE = 'Android Emulator'
AUTOMATION_NAME = 'UiAutomator2'
# absolute path to the apk, or the URL (if hosted somewhere on the internet)
APK_ABSOLUTE_PATH = ''
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

    def test_view_educational_screen(self, driver):
        driver.find_element_by_android_uiautomator('text("English")').click()
        driver.find_element_by_android_uiautomator('text("Continue")').click()
        driver.find_element_by_android_uiautomator('text("ALLOW")').click()

        el = driver.find_elements_by_class_name('android.widget.TextView')
        assert 'You can get an instant loan on your phone.' == el[0].text
