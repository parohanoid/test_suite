import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("filter", ["No Filter", "7 Stars", "9 Stars", "Hotel", "House", "Camping"])
@pytest.mark.parametrize("sort", ["Recommended", "Price Asc", "Price Des", "Distance Min"])
def test_all_filters(setup_browser, url, sort, filter):

    driver = setup_browser
    
    wait = WebDriverWait(driver, 10)
    driver.get(url+"functional/bookHotel")

    driver.find_element(By.CSS_SELECTOR, ".modal-dialog button").click()
    wait.until(EC.invisibility_of_element((By.CLASS_NAME, "spinner-border")))

    filter_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(@class,'bookHotelForm')]//button)[1]")))
    filter_button.click()

    option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(@class,'dropdown-item') and contains(text(), '{filter}')]")))

    option.click()

    sort_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(@class,'bookHotelForm')]//button)[2]")))
    sort_button.click()

    option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(@class,'dropdown-item') and contains(text(), '{sort}')]")))
    option.click()

    wait.until(EC.invisibility_of_element((By.CLASS_NAME, "spinner-border")))