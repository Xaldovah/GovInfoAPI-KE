from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from parliament.models import MemberOfParliament

def extract_page_data(driver):
    """
    Function to extract the data from the current page of the pagination element. 
    Returns a list of dictionaries, each containing the data from one row of the table.
    """
    page_output = []

    page_elements = driver.find_elements(By.XPATH, '//tr[contains(@class, "mp")]')
    for each_element in page_elements:
        name = each_element.find_element(By.CLASS_NAME, 'views-field-field-name').text.strip()
        constituency = each_element.find_element(By.CLASS_NAME, 'views-field-field-constituency').text.strip()
        county = each_element.find_element(By.CLASS_NAME, 'views-field-field-county').text.strip()
        party = each_element.find_element(By.CLASS_NAME, 'views-field-field-party').text.strip()

        mp_data = {
                'name': name,
                'constituency': constituency,
                'county': county,
                'party': party
        }

        page_output.append(mp_data)
    return page_output

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
driver.get('http://www.parliament.go.ke/the-national-assembly/mps')
driver.maximize_window()

# Loop through each page
while True:
    # Extract data from the current page
    page_data = extract_page_data(driver)

    # Save data to the SQLite database
    for mp_data in page_data:
        existing_mp = MemberOfParliament.objects.filter(name=mp_data['name'], constituency=mp_data['constituency'], county=mp_data['county'], party=mp_data['party']).first()
        if not existing_mp:
            mp_object = MemberOfParliament(**mp_data)
            mp_object.save()

    # Check if there's a next page
    try:
        next_page = driver.find_element(By.XPATH, '//a[contains(@title, "Go to next page")]')   
        next_page.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Reached the end of pagination.")
        break

# Close the browser
driver.quit()
