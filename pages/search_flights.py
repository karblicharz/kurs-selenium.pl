from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure


class SearchFlightsPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_flights_tab_xpath = '//li[@data-title="flights"]'
        self.round_trip_checkbox_xpath = '//div[input[@id="round"]]'
        self.from_airport_field_id = 's2id_location_from'
        self.to_airport_field_id = 's2id_location_to'
        self.airport_input_xpath = '//div[@id="select2-drop"]//input'
        self.departure_input_xpath = '//input[@name="departure"]'
        self.arrival_input_xpath = '//input[@name="arrival"]'
        self.passenger_input_xpath = '//input[@name="totalManualPassenger"]'
        self.passenger_adults_xpath = '//select[@name="madult"]'
        self.passenger_child_xpath = '//select[@name="mchildren"]'
        self.passenger_infant_xpath = '//select[@name="minfant"]'

    def click_search_flights_tab(self):
        self.driver.find_element(By.XPATH, self.search_flights_tab_xpath).click()

    def click_round_trip_checkbox(self):
        self.driver.find_element(By.XPATH, self.round_trip_checkbox_xpath).click()

    def set_to_airport(self, airport):
        self.driver.find_element(By.ID, self.to_airport_field_id).click()
        self.driver.find_element(By.XPATH, self.airport_input_xpath).send_keys(airport)
        self.driver.find_element(By.CLASS_NAME, 'select2-match').click()

    def set_from_airport(self, airport):
        self.driver.find_element(By.ID, self.from_airport_field_id).click()
        self.driver.find_element(By.XPATH, self.airport_input_xpath).send_keys(airport)
        self.driver.find_element(By.CLASS_NAME, 'select2-match').click()

    def set_departure_date(self, departure_date):
        self.driver.find_element(By.XPATH, self.departure_input_xpath).send_keys(departure_date)

    def set_arrival_date(self, arrival_date):
        self.driver.find_element(By.XPATH, self.arrival_input_xpath).send_keys(arrival_date)

    def set_passengers_number(self, adult, child, infant):
        self.driver.find_element(By.XPATH, self.passenger_input_xpath).click()
        adults = Select(self.driver.find_element(By.XPATH, self.passenger_adults_xpath))
        adults.select_by_value(adult)
        children = Select(self.driver.find_element(By.XPATH, self.passenger_child_xpath))
        children.select_by_value(child)
        infants = Select(self.driver.find_element(By.XPATH, self.passenger_infant_xpath))
        infants.select_by_value(infant)
