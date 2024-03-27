from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from senate.models import Senators
import time


def extract_senate_data(driver):
    """
    Function to extract the data from the current page of the pagination
    element.
    Returns a list of dictionaries, each containing the data from one row
    of the table.
    """
    page_output = []

    for _ in range(7):
        try:
            page_elements = driver.find_elements(
                    By.XPATH, '//tr[not(@class)]')
            for each_element in page_elements:
                name = each_element.find_element(
                        By.CLASS_NAME, 'views-field-field-senator').text.strip()       
                county = each_element.find_element(
                        By.CLASS_NAME, 'views-field-field-county-senator').text.strip()
                party = each_element.find_element(
                        By.CLASS_NAME, 'views-field-field-party-senator').text.strip() 

                if county != "Nominated" and name != "Senator":
                    senator_data = {
                            'name': name,
                            'county': county,
                            'party': party
                    }
                    page_output.append(senator_data)
        except StaleElementReferenceException:
            continue

        try:
            next_page = driver.find_element(
                    By.XPATH, '//a[contains(@title, "Go to next page")]')
            if not next_page:
                print("Reached the end of pagination.")
                break

            next_page.click()
            time.sleep(2)
        except NoSuchElementException:
            print("Reached the end of pagination")
            break

    return page_output
