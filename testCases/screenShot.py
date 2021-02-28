from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import TakeScreenShot as TakeScreenShot

path = "C:\\selenium\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.maximize_window()
driver.get("http://www.theTestingWorld.com/testings")
TakeScreenShot.take_Screen_shot(driver, 'screenShot2')
