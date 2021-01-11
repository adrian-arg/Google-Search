import pytest


@pytest.mark.regression
@pytest.mark.search
@pytest.mark.usefixtures(
    "driver", "user_is_at_home_page", "home_page", "search_results_page"
)
class TestGoogleSearch:

    @pytest.mark.parametrize(
        "search_parameter, expected_result_position, expected_result_text",
        [
            ("The name of the wind", 1, "The Name of the Wind - Patrick Rothfuss")
        ]
    )
    def test_c000002_search_using_the_google_search_button(
        self, search_parameter, expected_result_position, expected_result_text, home_page, search_results_page
    ):
        home_page.enter_search_string(string=search_parameter)
        home_page.click_on_search_button()
        results_list = search_results_page.get_results_list()

        assert results_list[expected_result_position - 1]['title'] == expected_result_text,\
            "\"" + expected_result_text + "\"" + " is not the first result"

    @pytest.mark.parametrize(
        "search_parameter, expected_suggestion_position, expected_suggestion_text",
        [
            ("The name of the w", 1, "The Name of the Wind - Patrick Rothfuss")
        ]
    )
    def test_c000003_display_auto_complete_suggestions(
        self, search_parameter, expected_suggestion_position, expected_suggestion_text, home_page
    ):
        home_page.enter_search_string(string=search_parameter)
        suggestions_list = home_page.get_suggestions_list()
        assert suggestions_list[expected_suggestion_position - 1]['text'] == expected_suggestion_text, \
            "\"" + expected_suggestion_text + "\"" + " is not the first suggestion"

    @pytest.mark.parametrize(
        "search_parameter, suggestion_position, expected_result_position, expected_result_text",
        [
            ("The name of the w", 1, 1, "The Name of the Wind - Patrick Rothfuss")
        ]
    )
    def test_c000004_search_using_the_suggestions_list(
        self, search_parameter, suggestion_position, expected_result_position, expected_result_text,
            home_page, search_results_page
    ):
        home_page.enter_search_string(string=search_parameter)
        home_page.click_on_suggestion_by_position(position=suggestion_position)
        results_list = search_results_page.get_results_list()
        assert results_list[expected_result_position - 1]['title'] == expected_result_text,\
            "\"" + expected_result_text + "\"" + " is not the first result"

    @pytest.mark.parametrize(
        "search_parameter, expected_result_position, destination_page_title",
        [
            ("The name of the wind", 1, "The Name of the Wind - Patrick Rothfuss")
        ]
    )
    def test_c000005_click_on_first_result_link(
        self, search_parameter, expected_result_position, destination_page_title,
        home_page, search_results_page, driver
    ):
        home_page.enter_search_string(string=search_parameter)
        home_page.click_on_search_button()
        search_results_page.click_on_result_by_position(position=expected_result_position)
        assert driver.title == destination_page_title, \
            "The destination page title does not match the expected: " + "\"" + destination_page_title + "\""
