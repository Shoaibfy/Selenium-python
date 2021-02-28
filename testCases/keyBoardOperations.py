from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


path = "C:\\selenium\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")

driver.find_element_by_name("fld_username").send_keys("hello")

act = ActionChains(driver)
# act.send_keys(Keys.TAB).perform()

# select data cntl + a

act.send_keys(Keys.CONTROL).send_keys("a").perform()
# act.send_keys(Keys.CONTROL).send_keys("c").perform()
# driver.find_element_by_name("fld_email").send_keys(
#     act.send_keys(Keys.CONTROL).send_keys("v").perform())
