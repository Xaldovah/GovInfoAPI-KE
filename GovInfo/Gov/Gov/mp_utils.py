from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from parliament.models import MemberOfParliament
import time


def extract_page_data(driver):
    """
    Function to extract the data from the current page of the pagination
    element.
    Returns a list of dictionaries, each containing the data from one row
    of the table.
    """
    page_output = []
    for _ in range(35):
        try:
            page_elements = driver.find_elements(
                    By.XPATH, '//tr[contains(@class, "mp")]')
            for each_element in page_elements:
                name = each_element.find_element(
                        By.CLASS_NAME, 'views-field-field-name').text.strip()
                constituency = each_element.find_element(
                        By.CLASS_NAME,
                        'views-field-field-constituency').text.strip()
                county = each_element.find_element(
                        By.CLASS_NAME, 'views-field-field-county').text.strip()
                party = each_element.find_element(
                        By.CLASS_NAME, 'views-field-field-party').text.strip()

                if constituency and party:
                    mp_data = {
                            'name': name,
                            'constituency': constituency,
                            'county': county,
                            'party': party
                    }
                    page_output.append(mp_data)
        except StaleElementReferenceException:
            continue

        try:
            next_page = driver.find_element(
                    By.XPATH, '//a[contains(@title, "Go to next page")]')
            if not next_page:
                print("Reached the end of pagination.")
                break

            next_page.click()
            time.sleep(3)
        except NoSuchElementException:
            print("Reached the end of pagination")
            break

    return page_output
