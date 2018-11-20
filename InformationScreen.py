from selenium import webdriver
import os

# *********************************************************************************************************************************************************************************************
# selectors erea

radio_button_for_other_selected_selector = "(//div[@class=\"ui-card\"])[2]//label[@data=\"forSomeone\" and @class=\"selected\"]"
radio_button_for_other_selector = "(//div[@class=\"ui-card\"])[2]//label[@data=\"forSomeone\"]"

reciver_name_selector = "//div[@class=\"ui-card\"]//span[contains(text(),'למי המתנה')]/parent::*/input"
sender_name_selector = "//div[@class=\"ui-card\"]//span[contains(text(),'ממי המתנה')]/parent::*/input"

blessing_selector = "(//div[@class=\"mx2 md1\"][2])//label[@class=\"ember-view ui-field ui-textarea\"]/textarea"
event_dropdownlist_selector = "(//div[@class=\"mx2 md1\"][2])//label[@class=\"ember-view ui-field ui-select\"]/div"

upload_picture_button_selector = "//div[@class=\"media-fields\"]//input[@class=\"ember-view ember-text-field\"]"
# when_to_pay_selector = "//div[@class=\"section  send-later-wrapper error-newline \"]//input[@id=\"step-2-now\"]"
when_to_pay_selector = "//div[@class=\"section  send-later-wrapper error-newline \"]//label[@class=\"send-now\"]"

send_giftcard_by_email_selector = "(//button[@class=\"btn btn-clean btn-send-option fluid \"])[2]"
send_giftcard_by_sms_selector = "//div[@class=\"row row--with-less-gutter row--sm\"]/div[1]//button[@class=\"btn btn-clean btn-send-option fluid \"]"

email_address_to_send_selector = "//div[@class=\"improved-overlay visible mail\"]//input"
email_address_to_sender_submit_button = "//div[@class=\"improved-overlay visible mail\"]//button[@type=\"submit\"]"

your_phone_input_selector = "//h3[@class=\"section-title\" and contains(text(),'לאיזה טלפון לשלוח?')]/parent::*//label[contains(text(),\"הטלפון שלך\")]/parent::*/input"
reciver_phone_input_selector = "//h3[@class=\"section-title\" and contains(text(),'לאיזה טלפון לשלוח?')]/parent::*//label[contains(text(),\"טלפון המקבל/ת\")]/parent::*/input"
phone_to_sender_submit_button_selector = "//div[@class=\"improved-overlay visible\"]//button[@type=\"submit\"]"

submit_all_button_selector = "//div[@class=\"submit-wrapper\"]/button[@type=\"submit\"]"


# *********************************************************************************************************************************************************************************************


class InformationScreen:

    def __init__(self, driver):
        self.driver = driver

    def check_for_other(self):

        if self.driver.find_element_by_xpath(radio_button_for_other_selected_selector).is_displayed():
            pass
        else:
            self.driver.find_element_by_xpath(radio_button_for_other_selector).click()

    def set_receiver_name(self, receiver_name):
        self.driver.find_element_by_xpath(reciver_name_selector).send_keys(receiver_name)

    def set_sender_name(self, sender_name):
        self.driver.find_element_by_xpath(sender_name_selector).send_keys(sender_name)

    def set_blessing(self, blessing_text):
        self.driver.find_element_by_xpath(blessing_selector).send_keys(blessing_text)

    def pick_event(self, event_name):

        self.driver.find_element_by_xpath(event_dropdownlist_selector).click()

        event_option_selector = ""

        if event_name == "Wedding":
            event_option_selector = "(//div[@class=\"mx2 md1\"][2])//label[@class=\"ember-view ui-field ui-select\"]/div//div[@class=\"chosen-drop\"]/ul[@class=\"chosen-results\"]/li[contains(text(),'חתונה וחינה')]"

        elif event_name == "birthday":
            event_option_selector = "(//div[@class=\"mx2 md1\"][2])//label[@class=\"ember-view ui-field ui-select\"]/div//div[@class=\"chosen-drop\"]/ul[@class=\"chosen-results\"]/li[contains(text(),'יום הולדת')]"

        else:
            print("pleace choose another choise")

        try:
            self.driver.find_element_by_xpath(event_option_selector).click()

        except:
            print("this option is not enable. pleace choose another choise")

    def upload_picture_file(self):
        try:

            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname, 'util/DevOps_icon.PNG')
            file_input = self.driver.find_element_by_xpath(upload_picture_button_selector)
            file_input.send_keys(filename)

        except:
            print("upload file does not succsses")

    def press_after_payment(self):
        self.driver.find_element_by_xpath(when_to_pay_selector).click()

    def send_by_email(self, email_address):
        self.driver.find_element_by_xpath(send_giftcard_by_email_selector).click()

        self.driver.find_element_by_xpath(email_address_to_send_selector).send_keys(email_address)

    def sumbit_email(self):
        try:
            self.driver.find_element_by_xpath(email_address_to_sender_submit_button).click()
        except:
            print("click does not enable. maybe you forget something or you type invalid values")

    def send_by_sms(self, your_phone_number, reciver_phone_number):
        self.driver.find_element_by_xpath(send_giftcard_by_sms_selector).click()

        self.driver.find_element_by_xpath(your_phone_input_selector).send_keys(your_phone_number)
        self.driver.find_element_by_xpath(reciver_phone_input_selector).send_keys(reciver_phone_number)

    def submit_phones(self):
        try:
            self.driver.find_element_by_xpath(phone_to_sender_submit_button_selector).click()
        except:
            print("click does not enable. maybe you forget something or you type invalid values")

    def submit_all(self):
        try:
            self.driver.find_element_by_xpath(submit_all_button_selector).click()
        except:
            print("click does not enable. maybe you forget something or you type invalid values")
