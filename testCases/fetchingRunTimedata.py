from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select


path = "C:\\selenium\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")
driver.maximize_window()
print(driver.title + "this is page title")

print(driver.current_url + "this is current url")

print(driver.page_source)  # fetch & displaying complete source HTML
