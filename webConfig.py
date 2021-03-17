from selenium import webdriver


class WebDrivers:
    def __init__(self, driver):
        self.driver = driver
        if driver == "SM":
            self.driver = webdriver.Chrome()
        elif driver == "fire":
            self.driver = webdriver.Firefox()
        elif driver == "edge":
            self.driver = webdriver.Edge()
        else:
            print(f"{driver} Not Found!!")

    def run_page(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
