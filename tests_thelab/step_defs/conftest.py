import os
os.environ['WDM_LOCAL'] = '1'
os.environ['WDM_SKIP_GITHUB_API'] = '1'

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="cef", 
                     help="Browsers: c=chrome, e=edge, f=firefox (e.g., 'cef', 'c')")


def pytest_generate_tests(metafunc):
    if "setup_browser" in metafunc.fixturenames:
        browsers = list(metafunc.config.getoption("--browser"))
        metafunc.parametrize("setup_browser", browsers, indirect=True)


@pytest.fixture(scope='function')
def url():
    return "https://thelab.boozang.com/"


@pytest.fixture(scope='function')
def setup_browser(request):
    browser = request.param
    options_map = {
        'c': (ChromeOptions, ChromeService, ChromeDriverManager().install, webdriver.Chrome),
        'f': (FirefoxOptions, FirefoxService, lambda: "./geckodriver", webdriver.Firefox),
        'e': (EdgeOptions, EdgeService, 
              lambda: EdgeChromiumDriverManager(
                  url="https://msedgedriver.microsoft.com/",
                  latest_release_url="https://msedgedriver.microsoft.com/LATEST_RELEASE"
              ).install(), webdriver.Edge)
    }
    
    if browser not in options_map:
        raise ValueError(f"Unsupported browser: {browser}")
    
    OptionsClass, ServiceClass, driver_path_fn, DriverClass = options_map[browser]
    options = OptionsClass()
    options.add_argument("--start-maximized")
    
    driver = DriverClass(service=ServiceClass(driver_path_fn()), options=options)
    
    try:
        yield driver
    finally:
        driver.quit()