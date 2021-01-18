from libs.base_classes.page_base import PageBase
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from pages.locators.search_results_locators import SearchResultsLocators


class SearchResultsPage(PageBase):

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

    def enter_search_string(self, string):
        self.enter_text_via_send_keys(locator=SearchResultsLocators.SEARCH_INPUT, string=string)

    def click_on_search_button(self):
        self.click_on(locator=SearchResultsLocators.SEARCH_BTN)

    def get_results_list(self):
        results_list = self.find_elements(locator=SearchResultsLocators.SEARCH_RESULTS_LIST)
        results_elements = []
        for result in results_list:
            results_elements.append({
                "title": result.find_element_by_css_selector("span").text,
                "element": result
            })
        return results_elements

    def click_on_result_by_position(self, position):
        result = self.get_results_list()[position - 1]['element']
        destination_url = result.get_attribute("href")
        self.click_on_element(element=result)
        self.wait_for_url_to_change_to(expected_url=destination_url)

