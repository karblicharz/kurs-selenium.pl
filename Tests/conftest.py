import pytest
import allure
from allure_commons.types import AttachmentType
from utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("chrome")
    driver.get("http://www.kurs-selenium.pl/demo/")
    driver.implicitly_wait(5)
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    driver.quit()

