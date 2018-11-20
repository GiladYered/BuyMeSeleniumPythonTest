from datetime import time
from selenium import webdriver


# *********************************************************************************************************************************************************************************************
# selectors erea

enter_register_button_selector = "//span[contains(text(),\"כניסה\")]"
until_no_regigster_button_selector = "//div[@class=\"lightbox-content\"]/p/span[@class=\"text-btn\"]"
register_name_selector = "//input[@placeholder=\"שם פרטי\"]"
register_email_selector ="//input[@placeholder=\"מייל\"]"
register_pass_selector = "//input[@placeholder=\"סיסמה\"]"
register_pass_again_selector = "//input[@placeholder=\"אימות סיסמה\"]"
radio_button_accept_selector="//div[@class=\"ember-view ui-field ui-checkbox\"][1]/label/i"
button_submit_selector="//button[@type =\"submit\" and contains(text(),\"הרשמה ל-BUYME\")]"

# broken selectors
# enter_register_button_selector = "//div[@class=\"main-container main-padding\"]/header//div[@class=\"wrapper relative\"]/ul[@class=\"top-bar padding\"]/li[@class=\"top-bar-item my-account\"]"
# until_no_regigster_button_selector = "//div[@class=\"modal modal--auth modal--extra-wide\"]//span[@class=\"header-link bold\"]"
# until_no_regigster_button_selector = "//span[contains(text(),\"להרשמה\")]"
# register_name_selector = "//div[@id=\"register-block\"]//form[@id=\"ember900\"]//input[@id=\"ember901\" and @placeholder=\"שם פרטי\"]"
# register_email_selector = "//div[@id=\"register-block\"]//form[@id=\"ember900\"]//input[@id=\"ember902\" and @placeholder=\"מייל\"]"
# register_pass_selector = "//div[@id=\"register-block\"]//form[@id=\"ember900\"]//input[@id=\"valPass\" and @placeholder=\"סיסמה\"]"
# register_pass_again_selector = "//div[@id=\"register-block\"]//form[@id=\"ember900\"]//input[@id=\"ember904\" and @placeholder=\"אימות סיסמה\"]"
# radio_button_accept_selector="(//div[@class=\"form-group\"][5])//label[contains(text(), 'אני מסכים')]"
# button_submit_selector="//div[@id=\"register-block\"]//button[@type =\"submit\"]"

# *********************************************************************************************************************************************************************************************


class RegistrationScreen:

    def __init__(self, driver):
        self.driver = driver

    # Press on button "כניסה| הרשמה"
    def click_on_enter_register(self):

        self.driver.find_element_by_xpath(enter_register_button_selector).click()
        # time.sleep(10)

    def click_on_until_no_regigster(self):

        self.driver.find_element_by_xpath(until_no_regigster_button_selector).click()

    def set_regigster_name(self,name):

        self.driver.find_element_by_xpath(register_name_selector).send_keys(name)


    def set_regigster_email(self,email):

        self.driver.find_element_by_xpath(register_email_selector).send_keys(email)

    def set_regigster_password(self,password):

        self.driver.find_element_by_xpath(register_pass_selector).send_keys(password)

    def set_regigster_password_again(self,password_again):

        self.driver.find_element_by_xpath(register_pass_again_selector).send_keys(password_again)

    def check_accept(self):

        # self.driver.find_elements_by_css_selector("input[type='checkbox'][value='SRF']")[0].click()
        # self.driver.find_element_by_id(radio_button_accept_selector).click()
        self.driver.find_element_by_xpath(radio_button_accept_selector).click()

    def submit_registration(self):

        self.driver.find_element_by_xpath(button_submit_selector).click()




