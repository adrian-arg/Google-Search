import pytest
import datetime


def pytest_addoption(parser):

    # Reports
    parser.addini(name="reports_folder", type="string", default="reports", help="Reports folder")

    parser.addoption(
        "--open-report", action="store_true", dest="open_report", help="Open report automatically once test run ends"
    )

    # Browser
    parser.addoption(
        "--browser", action="store", dest="browser", default="chrome",
        help="Select browser for test run. Valid options: chrome, firefox"
    )

    # WebDriver config
    parser.addoption("--driver_path", action="store", type=str, default=None,
                     help="WebDriver path: webdrivers/linux/chrome/chromedriver")
    parser.addini(name="implicit_wait_time", type="string", default=None, help="WebDriver Implicit Wait Time")
    parser.addini(name="page_load_timeout", type="string", default=None, help="WebDriver Page Load Timeout")
    parser.addini(name="headless", type="bool", default=True, help="Run tests in headless mode")
    parser.addini(name="page_load_strategy", type="string", default="none", help="WebDriver page load strategy")
    parser.addini(name="options_arguments", type="linelist", default=None, help="WebDriver arguments")
    parser.addini(name="explicit_wait", type="args", default=None, help="WebDriver arguments")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):

    #request.node.own_markers[0].args[0]

    import os
    from libs.utilities import utils
    from configparser import NoOptionError

    if not config.option.htmlpath:
        try:
            reports_path = os.path.join(utils.get_project_directory(), config.getini("reports_folder"))
            now = datetime.datetime.now().__format__("%Y-%m-%d_%H-%M-%S")
            html_path = os.path.join(reports_path, "Automation_Report_" + now + ".html")
        except NoOptionError:
            html_path = 'my_report.html'

        config.option.htmlpath = html_path


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):

    import webbrowser

    if session.config.getoption("open_report"):
        report_file = session.config._html.logfile
        new = 2
        webbrowser.open(report_file, new=new)


@pytest.fixture
def driver(request):

    from libs.webdriver.setup_webdriver import SetupWebDriver

    driver = False
    try:
        # Global implicit wait timeout
        implicit_wait_time = request.config.getini("implicit_wait_time")
        browser = request.config.getoption("browser")

        set_up_webdriver = SetupWebDriver(driver_path=request.config.getoption("driver_path"), browser=browser)

        if browser == "chrome":
            driver = set_up_webdriver.set_up_chrome_driver(
                implicit_wait_time=implicit_wait_time,
                options_arguments=request.config.getini("options_arguments")
            )
        elif browser == "firefox":
            driver = set_up_webdriver.set_up_firefox_gecko_driver(
                options_arguments=request.config.getini("options_arguments"),
                implicit_wait_time=implicit_wait_time
            )

    except Exception:
        if driver:
            driver.quit()
        raise

    yield driver

    driver.quit()


@pytest.fixture
def home_page(driver):
    from pages.home_page import HomePage
    home_page = HomePage(driver=driver)
    return home_page


@pytest.fixture
def search_results_page(driver):
    from pages.search_results_page import SearchResultsPage
    search_results_page = SearchResultsPage(driver=driver)
    return search_results_page


@pytest.fixture
def user_is_at_home_page(driver, home_page):
    driver.get("https://www.google.com/")
    home_page.is_page_displayed()
