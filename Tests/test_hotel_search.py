import allure
import pytest
from pages.search_hotel import SearchHotelPage
from pages.search_results import SearchResultsPage
from utils.read_excel import ReadExcel


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("Test hotel search")
    @allure.description("Test verify hotel search engine")
    @pytest.mark.parametrize("data", ReadExcel.get_data())
    def test_hotel_search(self, data):
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city(data.city)
        search_hotel_page.set_date_range(data.check_in, data.check_out)
        search_hotel_page.set_travellers(data.adult_travellers, data.child_travellers)
        search_hotel_page.click_search()
        search_results_page = SearchResultsPage(self.driver)
        hotel_names = search_results_page.get_hotel_names()
        hotel_prices = search_results_page.get_hotel_prices()
        assert hotel_names[0] == data.hotel_1
        assert hotel_prices[0] == data.price_1

