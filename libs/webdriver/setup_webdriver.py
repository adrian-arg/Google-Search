import os
from libs.utilities import utils
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, DesiredCapabilities


class SetupWebDriver:

    def __init__(self, browser="chrome", driver_path=None):
        """
        :param browser:
        :param driver_path: Use to specify a different versions of chromedriver.exe,
        leaving empty uses the latest as default
        """
        self.driver_path = self.set_absolute_driver_path(driver_path=driver_path, browser=browser)

    # TODO Analyze common behavior for these and other browsers

    def set_up_chrome_driver(
            self, options_arguments=None, page_load_timeout=None, implicit_wait_time=None, page_load_strategy="none"
    ):
        """
        :param options_arguments: ChromeOptions arguments
        :param page_load_timeout:
        :param implicit_wait_time:
        :param page_load_strategy: Available options are "normal", "eager" or "none" (default)
        :return: driver: chromedriver instance
        """

        # Use options and capabilities to customize Chrome Browser
        options = ChromeOptions()
        for argument in options_arguments:
            options.add_argument(argument)
        options.set_capability("pageLoadStrategy", page_load_strategy)
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en_ca'})

        capabilities = DesiredCapabilities().CHROME
        capabilities["pageLoadStrategy"] = page_load_strategy

        driver = webdriver.Chrome(executable_path=self.driver_path, desired_capabilities=capabilities, options=options)

        if page_load_timeout is not None:
            driver.set_page_load_timeout(int(page_load_timeout))

        if implicit_wait_time is not None:
            driver.implicitly_wait(int(implicit_wait_time))

        return driver

    def set_up_firefox_gecko_driver(
            self, options_arguments=None, page_load_timeout=None, implicit_wait_time=None, page_load_strategy="none"
    ):
        """
           :param options_arguments: ChromeOptions arguments
           :param page_load_timeout:
           :param implicit_wait_time:
           :param page_load_strategy: Available options are "normal", "eager" or "none" (default)
           :return: driver: chromedriver instance
       """

        # Use options and capabilities to customize Firefox Browser
        options = FirefoxOptions()
        for argument in options_arguments:
            options.add_argument(argument)
        options.set_capability("pageLoadStrategy", page_load_strategy)

        capabilities = DesiredCapabilities().FIREFOX
        capabilities.keys()
        capabilities["pageLoadStrategy"] = page_load_strategy
        #capabilities["marionette"] = True

        driver = webdriver.Firefox(executable_path=self.driver_path, desired_capabilities=capabilities, options=options)

        if page_load_timeout is not None:
            driver.set_page_load_timeout(int(page_load_timeout))

        if implicit_wait_time is not None:
            driver.implicitly_wait(int(implicit_wait_time))

        return driver

    def set_absolute_driver_path(self, driver_path, browser):

        """
        :return This method resolves the absolute path for relative paths of the webdrivers directory within the
         project. If the driver_path does not match a pattern inside the project it will return the original value.
         If the driver_path is empty it will return the path to the latest version for the browser

        """

        if driver_path is not None:
            # Project Relative Path
            if driver_path.startswith("webdrivers"):
                driver_path = os.path.join(utils.get_project_directory(), driver_path)
        else:
            # Path to latest expected webdriver version by default
            path = os.path.join(utils.get_project_directory(), "webdrivers", utils.get_os(), browser)
            if browser == "chrome":
                driver_path = os.path.join(path, "chromedriver")
            elif browser == "firefox":
                driver_path = os.path.join(path, "geckodriver")

        return driver_path
