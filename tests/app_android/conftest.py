import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import pytest
from appium.options.android import UiAutomator2Options
from selene import browser, support
import allure_commons
import os
import config
import utils.attach
from utils import attach

@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # "platformName": "android",
        "platformVersion": "10.0",
        "deviceName": "Google Pixel 4",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Python_project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack_test",

            # Set your access credentials
            'userName': config.bstack_userName,
            'accessKey': config.bstack_accessKey,
        }
    })

    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield
    allure.attach(
        browser.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG
    )
    allure.attach(
        browser.driver.page_source, name='xml_dump', attachment_type=AttachmentType.XML
    )

    session_id = browser.driver.session_id

    with step('Tear down app session'):
         browser.quit()

    utils.attach.attach_bstack_video(session_id)