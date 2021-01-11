from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageBase(object):
    """
    Use set_explicit_wait during derived Page Object __init__ method

    Example:
        def __init__(self, driver):
            super().__init__(driver)
            self.set_explicit_wait(timeout=30, poll_frequency=1)

    """

    def __init__(self, driver):
        self.driver = driver

    def set_explicit_wait(self, timeout=30, poll_frequency=1, ignored_exceptions={}):
        """
        This methods sets up a global explicit wait to be used in each derived Page Object
        :param timeout: timeout in seconds
        :param poll_frequency: poll frequency in seconds
        :param ignored_exceptions: list of exceptions to be ignored while polling
        :return: void
        """

        self.explicit_wait = WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=poll_frequency,
            ignored_exceptions=ignored_exceptions,
        )

    def find_element(self, locator, explicit_wait=True):
        if explicit_wait:
            return self.explicit_wait.until(EC.visibility_of_element_located(locator))
        else:
            return self.driver.find_element(*locator)

    def find_elements(self, locator, explicit_wait=True):
        if explicit_wait:
            return self.explicit_wait.until(EC.visibility_of_all_elements_located(locator))
        else:
            return self.driver.find_elements(*locator)

    def find_clickable_element(self, locator):
        return self.explicit_wait.until(EC.element_to_be_clickable(locator))

    def click_on(self, locator=None):
        element = self.find_clickable_element(locator=locator)
        element.click()

    def click_on_element(self, element):
        element.click()

    def enter_text_via_send_keys(self, locator, string):
        element = self.find_clickable_element(locator=locator)
        element.clear()
        element.send_keys(string)

    def is_displayed(self, locator=None, explicit_wait=True):
        if explicit_wait is True:
            return self.find_element(locator=locator, explicit_wait=explicit_wait).is_displayed()
        else:
            elements = self.find_elements(locator=locator, explicit_wait_enabled=explicit_wait)
            if len(elements) > 0:
                return elements[0].is_displayed()
            else:
                return False

    def wait_for_url_to_change_to(self, expected_url):
        return self.explicit_wait.until(EC.url_to_be(url=expected_url))
