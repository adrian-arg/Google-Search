import pytest


@pytest.mark.regression
@pytest.mark.home
@pytest.mark.usefixtures(
    "driver", "home_page"
)
class TestHomePage:

    @pytest.mark.parametrize(
        "url, expected_page_title",
        [
            ("https://www.google.com/", "Google")
        ]
    )
    def test_c000001_navigate_to_google_home_page(self, url, expected_page_title, driver, home_page):
        driver.get(url)
        is_page_displayed = home_page.is_page_displayed()
        page_title_ok = (driver.title == expected_page_title)
        assert is_page_displayed and page_title_ok, "Google Home Page is not displayed"
