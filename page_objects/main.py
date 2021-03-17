from webConfig import WebDrivers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from variables import var


class LampTrainees:
    def __init__(self):
        self.driver = WebDrivers("SM")
        self.wait = WebDriverWait(self.driver.driver, 30)

    def run_page(self):
        self.driver.driver.maximize_window()
        self.driver.run_page(var.lamp_page)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, var.landing_login)))
        self.driver.driver.find_element_by_xpath(var.landing_login).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, var.login_button)))

    def login(self):
        self.driver.driver.find_element_by_xpath(var.email_field).send_keys(var.login_email)
        self.driver.driver.find_element_by_xpath(var.password_field).send_keys(var.Login_password)
        self.driver.driver.find_element_by_xpath(var.login_button).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, var.trainees_button)))

    def invite_employee(self):
        self.driver.driver.find_element_by_xpath(var.trainees_button).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, var.invite_button)))
        self.driver.driver.find_element_by_xpath(var.invite_button).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, var.add_employees_button)))
        self.driver.driver.find_element_by_xpath(var.add_employees_button).send_keys(var.employees_email)
        sleep
         
        self.wait.until(ec.visibility_of_element_located((By.XPATH, var.send_invite_button)))
        self.driver.driver.find_element_by_xpath(var.send_invite_button).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, var.close_button)))
        self.driver.driver.find_element_by_xpath(var.close_button).click()
        sleep(3)

    def close_page(self):
        self.driver.driver.quit()


