import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def test_assignment(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 30)


    # 1.
    driver.get("http://www.uitestingplayground.com/")

    page_title = driver.find_element(By.ID, "title").text
    assert page_title == "UI Test Automation\nPlayground"

    feature_link = driver.find_element(By.XPATH, "//a[@href='/dynamicid']")
    assert feature_link.text == "Dynamic ID"

    # 2.
    feature_link.click()

    dynamic_id_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
    assert dynamic_id_button.is_displayed()

    # 3.
    # Click on Home nav
    driver.get("http://www.uitestingplayground.com/")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/textinput']")))
    # Click on Text Input link
    driver.find_element(By.XPATH, "//a[@href='/textinput']").click()

    text_to_input = "Selenium Test"

    driver.find_element(By.ID, "newButtonName").send_keys(text_to_input)

    driver.find_element(By.ID, "updatingButton").click()

    # Verify the button text is what we entered
    assert driver.find_element(By.ID, "updatingButton").text == text_to_input

    # 4.
    # Click on Home nav
    driver.get("http://www.uitestingplayground.com/")

    # Click on client side delay link
    driver.find_element(By.XPATH, "//a[@href='/clientdelay']").click()

    driver.find_element(By.ID, "ajaxButton").click()

    # wait.until(EC.invisibility_of_element((By.ID, "spinner")))

    # driver.set_page_load_timeout(driver, 30)

    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), "Data calculated on the client side."))

    displayed_message = driver.find_element(By.ID, "content").text
    assert displayed_message == "Data calculated on the client side."
