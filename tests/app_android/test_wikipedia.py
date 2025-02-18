from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


# def test_search():
#
#     with step('Type search'):
#         browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
#         browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Apium')
#
#     with step('Verify content found'):
#         results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
#         results.should(have.size_greater_than(0))
#         results.first.should(have.text('Apium'))

def test_search1():

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('2Pac')
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2Pacalypse Now")')).click()