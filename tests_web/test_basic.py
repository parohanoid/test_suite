import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


def test_textbox():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless-new")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://demoqa.com/text-box")

    input = "Hello, HAHA"

    wait = WebDriverWait(driver, 10)
    full_name = wait.until(EC.element_to_be_clickable((By.ID, 'userName')))
    full_name.send_keys(input)

    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
    submit_button.click()

    output = wait.until(EC.visibility_of_element_located((By.ID, 'name')))

    assert output.text == "Name:" + input
