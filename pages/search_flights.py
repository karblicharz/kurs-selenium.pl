from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import date, timedelta
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
        self.done_button_id = 'sumManualPassenger'
        self.search_button_xpath = '//button[@type="submit"][not(contains(@class, "loader"))][contains(text(), "Search")]'
        self.dates_availability_panel_depart_date_xpath = '//div[1][@class="row"]//li[@class="active"]/a[@class="enable"]'
        self.dates_availability_panel_return_date_xpath = '//div[2][@class="row"]//li[@class="active"]/a[@class="enable"]'

    def click_search_flights_tab(self):
        self.driver.find_element(By.XPATH, self.search_flights_tab_xpath).click()

    def click_round_trip_checkbox(self):
        self.driver.find_element(By.XPATH, self.round_trip_checkbox_xpath).click()

    def click_done_button(self):
        self.driver.find_element(By.ID, self.done_button_id).click()

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def set_to_airport(self, airport):
        self.driver.find_element(By.ID, self.to_airport_field_id).click()
        self.driver.find_element(By.XPATH, self.airport_input_xpath).send_keys(airport)
        self.driver.find_element(By.CLASS_NAME, 'select2-match').click()

    def set_from_airport(self, airport):
        self.driver.find_element(By.ID, self.from_airport_field_id).click()
        self.driver.find_element(By.XPATH, self.airport_input_xpath).send_keys(airport)
        self.driver.find_element(By.CLASS_NAME, 'select2-match').click()

    def set_departure_date_at_today(self):
        today = date.today()
        departure = today.strftime("%Y-%m-%d")
        self.driver.find_element(By.XPATH, self.departure_input_xpath).send_keys(departure)

    def set_arrival_date(self, days):
        future_date = date.today() + timedelta(days)
        arrival = future_date.strftime("%Y-%m-%d")
        self.driver.find_element(By.XPATH, self.arrival_input_xpath).send_keys(arrival)

    def set_passengers_number(self, adult, child, infant):
        self.driver.find_element(By.XPATH, self.passenger_input_xpath).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.passenger_adults_xpath)))
        adults = Select(self.driver.find_element(By.XPATH, self.passenger_adults_xpath))
        adults.select_by_value(adult)
        children = Select(self.driver.find_element(By.XPATH, self.passenger_child_xpath))
        children.select_by_value(child)
        infants = Select(self.driver.find_element(By.XPATH, self.passenger_infant_xpath))
        infants.select_by_value(infant)

    def get_depart_date(self):
        text = self.driver.find_element(By.XPATH, self.dates_availability_panel_depart_date_xpath).text
        depart_date = text.replace("\n", " ")
        return depart_date

    def get_return_date(self):
        text = self.driver.find_element(By.XPATH, self.dates_availability_panel_return_date_xpath).text
        return_date = text.replace("\n", " ")
        return return_date

    def get_today_date_a_b_d(self):
        today = date.today()
        date_in_a_b_d_format = today.strftime("%a %b %d")
        return date_in_a_b_d_format

    def get_future_date_a_b_d(self, days):
        future_date = date.today() + timedelta(days)
        date_in_a_b_d_format = future_date.strftime("%a %b %d")
        return date_in_a_b_d_format
