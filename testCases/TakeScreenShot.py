def take_Screen_shot(driver, name):
    driver.get_screenshot_as_file(
        "C:/Users/WINDOWS/OneDrive/Desktop/Selenium_Python/testCases/" + name + ".png")
