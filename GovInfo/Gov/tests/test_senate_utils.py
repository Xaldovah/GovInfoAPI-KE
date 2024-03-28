import unittest
from unittest.mock import Mock
from selenium.common.exceptions import StaleElementReferenceException
from Gov.senate_utils import extract_senate_data

class TestExtractSenateData(unittest.TestCase):
    def setUp(self):
        self.driver = Mock()

    def test_extract_senate_data(self):
        """Mock page elements"""
        mock_element = Mock()
        mock_element.text = "John Doe"
        self.driver.find_elements.return_value = [mock_element]

        # Call the function
        data = extract_senate_data(self.driver)

        # Assert that data is extracted correctly
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "John Doe")

    def test_pagination_handling(self):
        """Mock next page link"""
        next_page_link = Mock()
        self.driver.find_element.return_value = next_page_link

        # Call the function for 2 pages
        extract_senate_data(self.driver)

        # Assert that the next page link is clicked twice
        self.assertEqual(next_page_link.click.call_count, 2)

    def test_exception_handling(self):
        """Mock StaleElementReferenceException"""
        self.driver.find_elements.side_effect = StaleElementReferenceException

        # Call the function
        data = extract_senate_data(self.driver)

        # Assert that an empty list is returned
        self.assertEqual(data, [])

if __name__ == '__main__':
    unittest.main()
