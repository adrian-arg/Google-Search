from selenium.webdriver.common.by import By


class HomePageLocators:
    HOME_PAGE_LOCATOR = (By.CSS_SELECTOR, "[id*='homepage']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='q']")
    SEARCH_SUGGESTION_LIST = (By.CSS_SELECTOR, "ul[role='listbox'] li")
    SEARCH_BTN = (By.CSS_SELECTOR, "input[name='btnK'][type='submit']")
    IM_FEELING_LUCKY_BTN = (By.CSS_SELECTOR, "[class='FPdoLc tfB0Bf'] input[name='btnI'][type='submit']")
