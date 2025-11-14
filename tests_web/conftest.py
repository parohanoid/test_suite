import os
os.environ['WDM_LOCAL'] = '1'  # Cache drivers locally
os.environ['WDM_SKIP_GITHUB_API'] = '1'  # Skip GitHub API version checks
# os.environ['WDM_OFFLINE'] = '1'  # Use cached drivers without checking for updates


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


@pytest.fixture()
def url():
    return "https://bugeater.web.app/app/challenge/"

@pytest.fixture(params=["chrome", "edge", "firefox"])
def setup_browser(request):
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        # Firefox uses the `headless` attribute
        driverPath = "./geckodriver"
        driver = webdriver.Firefox(
            service=FirefoxService(driverPath),
            options=options,
        )
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless=new")

        driverPath = EdgeChromiumDriverManager( url="https://msedgedriver.microsoft.com/", latest_release_url="https://msedgedriver.microsoft.com/LATEST_RELEASE" ).install()
        driver = webdriver.Edge(
            service=EdgeService(driverPath),
            options=options,
        )
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    try:
        yield driver
    finally:
        driver.quit()