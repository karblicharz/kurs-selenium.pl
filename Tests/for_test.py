# import datetime
#
#
# def cat_sound():
#    print("miauuuu")
#
#
# def simple_current_time_wrapper(function):
#    def wrapper():
#        print(datetime.datetime.now())
#        function()
#    return wrapper
#
# cat_with_date = simple_current_time_wrapper(cat_sound)
# cat_with_date()

# ----------------------------------------------
# import pytest
# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
#
# @pytest.fixture()
# def test_setup():
#     global browser
#     service = Service(r"D:\selenium_udemy\drivers\chromedriver.exe")
#     service.start()
#     browser = webdriver.Chrome(service=service)
#     browser.get("https://google.pl")
#     yield
#     browser.quit()
#
#
# def test_method(test_setup):
#     assert browser.title == "Google", "Tytuł " + browser.title + " jest nieprawidłowy"

# ---------------------------------------------------
import pytest


@pytest.mark.parametrize("skladnik, suma", [(5,8),(2,6)])
def test_dodawania(skladnik,suma):
    assert suma == skladnik + skladnik, "Suma dwóch takich samych składników powinna być równa " + str(skladnik+skladnik)
