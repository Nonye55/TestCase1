from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from variables import var

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(var.lamp_page)
wait = WebDriverWait(driver, 30)
wait.until(ec.visibility_of_element_located((By.XPATH,var.landing_login)))
driver.find_element_by_xpath(var.landing_login).click()
# driver.implicitly_wait(10)
driver.find_element_by_xpath(var.email_field).send_keys(var.login_email)
driver.find_element_by_xpath(var.password_field).send_keys(var.Login_password)
driver.find_element_by_xpath(var.login_button).click()
driver.implicitly_wait(15)
driver.find_element_by_xpath(var.trainees_button).click()
driver.implicitly_wait(10)
driver.find_element_by_xpath(var.invite_button).click()
driver.implicitly_wait(10)
driver.find_element_by_xpath(var.add_employees_button).send_keys(var.employees_email)
driver.implicitly_wait(10)
driver.find_element_by_xpath(var.send_invite_button).click()
driver.implicitly_wait(10)
driver.find_element_by_xpath(var.close_button).click()
sleep(3)
driver.quit()
