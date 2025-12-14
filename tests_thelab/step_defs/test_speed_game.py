from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, when, then


@scenario("../features/speed_game.feature", "Verify message shown on end game")
def test_verify_message_shown_on_end_game(setup_browser):
    """Test scenario from feature file."""
    pass


@given("I have started the speed game")
def start_speed_game(url, setup_browser):
    setup_browser.get(url + "speedGame")
    setup_browser.find_element(By.XPATH, "//button[@data-testid='startBtn']").click()


@when("I end the game")
def end_speed_game(setup_browser):
    wait = WebDriverWait(setup_browser, 30)
    end_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form_btn.delete")))
    end_button.click()

@then("a success message should be shown")
def verify_success_message(setup_browser):
    wait = WebDriverWait(setup_browser, 30)
    success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-testid='message']")))
    assert success_message.is_displayed()