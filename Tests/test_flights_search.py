import allure
import pytest
from pages.search_flights import SearchFlightsPage
from utils.read_excel import ReadExcel


@pytest.mark.usefixtures("setup")
class TestFlightsSearch:

    @allure.title("Test flights search")
    @allure.description("Test verify flights search engine")
    @pytest.mark.parametrize("data", ReadExcel.get_flights_data())
    def test_flights_search(self, data):
        search_flights_page = SearchFlightsPage(self.driver)
        search_flights_page.click_search_flights_tab()
        search_flights_page.click_round_trip_checkbox()
        search_flights_page.set_from_airport(data.from_airport)
        search_flights_page.set_to_airport(data.to_airport)
        search_flights_page.set_date_range_from_today(7)
        search_flights_page.set_passengers_number('3', '1', '1')


