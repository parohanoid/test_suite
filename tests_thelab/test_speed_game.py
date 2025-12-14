from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_speed_game(url, setup_browser):
    driver = setup_browser

    driver.get(url)