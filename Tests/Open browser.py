from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"D:\selenium_udemy\drivers\chromedriver.exe")
service.start()
browser = webdriver.Chrome(service=service)
browser.get("C:/Users/Karol/AppData/Local/Temp/Test.html")
browser.maximize_window()

first_window = browser.window_handles[0]
browser.find_element(By.ID, 'newPage').click()
second_window = browser.window_handles[1]
browser.switch_to.window(second_window)
print(browser.title)
browser.switch_to.window(first_window)
print(browser.title)
browser.quit()



# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("http://google.com")
#
