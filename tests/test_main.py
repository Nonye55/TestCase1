from page_objects.main import LampTrainees

driver = LampTrainees()
driver.run_page()
driver.login()
driver.invite_employee()

