import allure
import pytest
from pages.search_hotels import SearchHotelsPage
from pages.search_hotels_results import SearchResultsPage
from utils.read_excel import ReadExcel


@pytest.mark.usefixtures("setup")
class TestHotelsSearch:

    @allure.title("Test hotels search")
    @allure.description("Test verify hotels search engine")
    @pytest.mark.parametrize("data", ReadExcel.get_hotels_data())
    def test_hotels_search(self, data):
        search_hotels_page = SearchHotelsPage(self.driver)
        search_hotels_page.set_city(data.city)
        search_hotels_page.set_date_range_from_today(7)
        search_hotels_page.set_travellers(data.adult_travellers, data.child_travellers)
        search_hotels_page.click_search()
        search_results_page = SearchResultsPage(self.driver)
        hotels_names = search_results_page.get_hotel_names()
        hotels_prices = search_results_page.get_hotel_prices()
        assert hotels_names[0] == data.hotel_1
        assert hotels_prices[0] == data.price_1

