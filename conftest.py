import pytest
from selenium import webdriver

SERVER_TEMPLATE = "http://{api}/"
UI_TEMPLATE = "http://{ui}/"


def pytest_addoption(parser):
    parser.addoption(
        "--api",
        action="store",
        required=True,
    )
    parser.addoption(
        "--ui",
        action="store",
        required=True,
    )


@pytest.fixture(scope='session')
def url(request):
    # create template for ui
    ui = request.config.getoption('--ui')
    return UI_TEMPLATE.format(ui=ui)


@pytest.fixture(scope='session')
def api(request):
    # create template for api
    api = request.config.getoption('--api')
    return SERVER_TEMPLATE.format(api=api)


@pytest.fixture(scope='session')
def driver(url, pytestconfig):
    # default driver is assumed to be chromedriver
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.get(url)
    yield driver
    driver.close()
    driver.quit()
