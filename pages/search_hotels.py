from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import allure
from datetime import date, timedelta


class SearchHotelsPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_hotel_field_xpath = '//span[text()="Search by Hotel or City Name"]'
        self.search_hotel_input_xpath = '//div[@id="select2-drop"]//input'
        self.search_hotel_location_match_class = 'select2-match'
        self.check_in_input_name = 'checkin'
        self.check_out_input_name = 'checkout'
        self.calendar_active_day_xpath = '//td[@class="day  active"]'
        self.travellers_input_id = 'travellersInput'
        self.travellers_adult_input_id = 'adultInput'
        self.travellers_child_input_id = 'childInput'
        self.search_button_xpath = '//button[text()=" Search"]'

    @allure.step("Setting city name to '{1}'")
    def set_city(self, city):
        self.driver.find_element(By.XPATH, self.search_hotel_field_xpath).click()
        self.driver.find_element(By.XPATH, self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element(By.CLASS_NAME, 'select2-match').click()
        allure.attach(self.driver.get_screenshot_as_png(), name='Set city', attachment_type=AttachmentType.PNG)

    @allure.step("Setting date range from today to today + 'days'")
    def set_date_range_from_today(self, days):
        today = date.today()
        check_in = today.strftime("%d/%m/%Y")
        self.driver.find_element(By.NAME, self.check_in_input_name).send_keys(check_in)
        future_date = date.today() + timedelta(days)
        check_out = future_date.strftime("%d/%m/%Y")
        self.driver.find_element(By.NAME, self.check_out_input_name).send_keys(check_out)
        allure.attach(self.driver.get_screenshot_as_png(), name='Set check in and acheck out dates',
                      attachment_type=AttachmentType.PNG)

    @allure.step("Setting travellers - adult '{1}', child '{2}'")
    def set_travellers(self, adult, child):
        self.driver.find_element(By.ID, self.travellers_input_id).click()
        self.driver.find_element(By.ID, self.travellers_adult_input_id).clear()
        self.driver.find_element(By.ID, self.travellers_adult_input_id).send_keys(adult)
        self.driver.find_element(By.ID, self.travellers_child_input_id).clear()
        self.driver.find_element(By.ID, self.travellers_child_input_id).send_keys(child)
        allure.attach(self.driver.get_screenshot_as_png(), name='Set travellers', attachment_type=AttachmentType.PNG)

    def click_search(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='View search result', attachment_type=AttachmentType.PNG)

