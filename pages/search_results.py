from selenium.webdriver.common.by import By


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_xpath = '//a[contains(@href, "://")]/b'
        self.hotel_prices_xpath = '//div[contains(@class, "fs26 text-center")]/b'

    def get_hotel_names(self):
        hotels = self.driver.find_elements(By.XPATH, self.hotel_names_xpath)
        return [hotel.get_attribute("textContent") for hotel in hotels]

    def get_hotel_prices(self):
        prices = self.driver.find_elements(By.XPATH, self.hotel_prices_xpath)
        return [price.get_attribute("textContent") for price in prices]

