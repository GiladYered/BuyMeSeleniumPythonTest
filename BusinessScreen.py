from selenium import webdriver

# *********************************************************************************************************************************************************************************************
# selectors erea
select_gif_card_product_selector = "//div[@class=\"cash-input-wrapper dib\"]/div[@class=\"money\"]/input"
what_is_the_price_of_gift_card_selector = "//h4[contains(text(),'מה סכום ה-Gift Card?')]"
submit_amount_to_pay = "//div[@class=\"card-info relative\"]//button[contains(text(),'בחירה')]"



# *********************************************************************************************************************************************************************************************


class BusinessScreen:

    def __init__(self, driver):
        self.driver = driver

    def select_buisness_by_name(self, buisness_name):
        #broken selector = select_buisness_selector = "//span[contains(text(), '" + buisness_name + "')]/parent::*"
        select_buisness_selector = "//div[@class=\"label\" and contains(text(), '" + buisness_name + "')]"

        self.driver.find_element_by_xpath(select_buisness_selector).click()

    def set_price_for_product(self, amount_to_pay):

        try:
            self.driver.find_element_by_xpath(what_is_the_price_of_gift_card_selector).is_displayed()
            self.driver.find_element_by_xpath(select_gif_card_product_selector).send_keys(amount_to_pay)

        except:
            print(
                "you can't set price to gift card. please choose another product.\nchoose_business_screen_test failed! :(")

    def submit_price(self):
        self.driver.find_element_by_xpath(submit_amount_to_pay).click()

