import typing as t
from functools import partial

import pytest
from pytest_django.live_server_helper import LiveServer
from selenium.webdriver import ChromeOptions, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# The Docker container running Selenium
SELENIUM_CMD_EXECUTOR = "http://selenium:4444/wd/hub"


@pytest.fixture
def base_url(live_server: LiveServer) -> str:
    """
    Return the base URL to the Django live test server.

    By default, this is localhost and a random port, but it can
    be set explicitly by passing the `--liveserver <host(:port)>` argument
    to `pytest`, or by setting the `DJANGO_LIVE_TEST_SERVER_ADDRESS`
    environment variable.
    """
    return live_server.url


@pytest.fixture
def driver() -> t.Iterator[Remote]:
    options = ChromeOptions()
    driver = Remote(command_executor=SELENIUM_CMD_EXECUTOR, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def query_selector(driver: Remote) -> partial[WebElement]:
    """Select DOM element by CSS selector."""
    return partial(driver.find_element, By.CSS_SELECTOR)
