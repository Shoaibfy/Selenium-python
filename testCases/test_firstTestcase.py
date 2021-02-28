from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()  # this method runs before test case
def environment_setup():
    global driver
    path = "C:\\selenium\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()

    yield driver.close()   # this yield will execute after test case


def test_verify_registration(environment_setup):

    # maximizing window
    # driver.maximize_window()

    # # enter text in input field
    # driver.find_element_by_name("fld_username").send_keys("hello")
    # driver.find_element_by_name("fld_email").send_keys("abc@gmail.com")
    # driver.find_element_by_name("fld_password").send_keys("Abc123")
    # driver.find_element_by_name("fld_cpassword").send_keys("Abc123")
    # driver.find_element_by_name("fld_username").clear()
    # driver.find_element_by_name("fld_username").send_keys("hello")
    # driver.find_element_by_name("dob").send_keys("")

    # Working on Radio button
    # driver.find_element_by_xpath("//input[@value='office']").click()

    # checkbox click
    # driver.find_element_by_name("terms").click()
    # Seleck dropdoen
    obj = Select(driver.find_element_by_name("sex"))
    # select using visible text
    # obj.select_by_visible_text("Female")
    # select using index number
    obj.select_by_index(1)
    # select using value string
    # obj.select_by_value("2")

    # click button
    # driver.find_element_by_xpath("//input[@type='submit']").click()
    # Link text
    # driver.find_element_by_link_text("Read Detail").click()
    # Close Browser
    # driver.close()

    assert driver.current_url == "http:\\theTestingtutor.com"
