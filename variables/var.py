"""
this  fill will be responsible for the strorage of urls,
passwords,username,element locators,and all string literals.
"""
# ++++++++++++++++++++++++++++++++++++#
#  For All urls
# ++++++++++++++++++++++++++++++++++++#

lamp_page = "https://lamp-frontend.herokuapp.com/"

# +++++++++++++++++++++++++++++++++++++#
# Landing page and login#
# +++++++++++++++++++++++++++++++++++++#

landing_login = "//button[@class='action-text btn-scroll mr-3 v-btn v-btn--outlined theme--dark v-size--default']//span[@class='v-btn__content'][normalize-space()='LOGIN']"
email_field = "//input[@placeholder='Email Address']"
login_email = "uka29c@gmail.com"
password_field = "//input[@placeholder='Password']"
Login_password = "123pass321"
login_button = "//span[normalize-space()='Login']"

# +++++++++++++++++++++++++++++++++++++++#
# Invite Employee
# ++++++++++++++++++++++++++++++++++++++++#

trainees_button = "//a[@href='/corporate/employee']"
invite_button = "//span[contains(.,'+ Invite')]"
add_employees_button = "/html//div[@id='app']/div[@role='document']/div/div/div/div/div[2]/div//input[@type='text']"
employees_email = "tennie@yopmail.com"
send_invite_button = "/html//div[@id='app']/div[@role='document']/div/div/div/div[@class='row']/div[2]/div/div[1]/div[2]/button[@type='button']/span[@class='v-btn__content']"
close_button = "//div[@id='app']/div[@role='document']/div/div/div/div[@class='row']/div[2]/div/div[3]/button[2]/span[@class='v-btn__content']"