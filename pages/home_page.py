from libs.base_classes.page_base import PageBase
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from pages.locators.home_page_locators import HomePageLocators


class HomePage(PageBase):

    def __init__(self, driver):

        super().__init__(driver=driver)

        self.set_explicit_wait(
            timeout=30,
            poll_frequency=1,
            ignored_exceptions={
                NoSuchElementException,
                ElementNotVisibleException,
            }
        )

    def is_page_displayed(self):
        return self.is_displayed(locator=HomePageLocators.HOME_PAGE_LOCATOR)

    def enter_search_string(self, string):
        self.enter_text_via_send_keys(locator=HomePageLocators.SEARCH_INPUT, string=string)

    def click_on_search_button(self):
        self.click_on(locator=HomePageLocators.SEARCH_BTN)

    def get_suggestions_list(self):
        suggestions_list = self.find_elements(locator=HomePageLocators.SEARCH_SUGGESTION_LIST)
        suggestions_elements = []
        for suggestion in suggestions_list:
            suggestions_elements.append({
                "text": suggestion.text,
                "element": suggestion
            })
        return suggestions_elements

    def click_on_suggestion_by_position(self, position):
        suggestions_list = self.get_suggestions_list()
        self.click_on_element(element=suggestions_list[position - 1]['element'])

