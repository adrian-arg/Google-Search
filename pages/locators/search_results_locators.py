from selenium.webdriver.common.by import By


class SearchResultsLocators:

    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='q'][title='Search']")
    SEARCH_SUGGESTION_LIST = (By.CSS_SELECTOR, "ul[role='listbox']")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    SEARCH_RESULTS_LIST = (
        By.XPATH,
        "//div[@class='g']/div[@class='rc']/div[@class='yuRUbf']/a[not(ancestor::div[@class='related-question-pair'])]"
    )
