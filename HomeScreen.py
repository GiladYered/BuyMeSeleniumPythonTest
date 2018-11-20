import os
import time
from selenium import webdriver


# *********************************************************************************************************************************************************************************************
# selectors erea
point_price_dropdownlist_selector ="(//div[@class=\"ember-view header-search-bar home\"]/div[@class=\"inner\"]//div)[1]"
area_dropdownlist_selector ="(//div[@class=\"ember-view header-search-bar home\"]/div[@class=\"inner\"]//div)[5]"
category_dropdownlist_selector ="(//div[@class=\"ember-view header-search-bar home\"]/div[@class=\"inner\"]//div)[9]"
# search_button = "//a[contains(text(),\"תמצאו לי מתנה\")]"
search_button = "//a[@class=\"ui-btn search ember-view\"]"

#broken selector
# point_price_dropdownlist_selector ="(//div[@class=\"row row--sm row--with-minimal-gutter\"]//div[@class=\"header-col col col-1-5\"])[1]/div/div"
#point_price_dropdownlist_option_selector = "(//div[@class=\"row row--sm row--with-minimal-gutter\"]//div[@class=\"header-col col col-1-5\"])[1]//div[@class=\"chosen-drop\"]/ul/li[text()='" + choosing + "']"
# area_dropdownlist_selector ="(//div[@class=\"row row--sm row--with-minimal-gutter\"]//div[@class=\"header-col col col-1-5\"])[2]/div/div"
# category_dropdownlist_selector ="(//div[@class=\"row row--sm row--with-minimal-gutter\"]//div[@class=\"header-col col col-1-5\"])[3]/div/div"
# search_button = "//div[@class=\"col col-1-3 btn-wrapper header-col\"]//button[@type=\"submit\"]"

# *********************************************************************************************************************************************************************************************

class HomeScreen:
    def __init__(self, driver):
        self.driver = driver

    def connect_to_web_site(self,  urlAddress):
        self.driver.get(urlAddress)

        # write the url to Url text file
        dirname = os.path.dirname(__file__)
        url_file = open(dirname + "/util/urlFile.txt",'w')
        url_file.write(urlAddress)


    def select_point_price(self,choosing):

        point_price_dropdownlist_option_selector = point_price_dropdownlist_selector + "/div[@class=\"chosen-drop\"]/ul[@class=\"chosen-results\"]//li[contains(text(),'" + choosing + "')]"

        self.driver.find_element_by_xpath(point_price_dropdownlist_selector).click()

        self.driver.find_element_by_xpath(point_price_dropdownlist_option_selector).click()

    def select_area(self,choosing):
        area_dropdownlist_option_selector = area_dropdownlist_selector + "/div[@class=\"chosen-drop\"]/ul[@class=\"chosen-results\"]//li[contains(text(),'" + choosing + "')]"

        self.driver.find_element_by_xpath(area_dropdownlist_selector).click()

        self.driver.find_element_by_xpath(area_dropdownlist_option_selector).click()

    def select_category(self,choosing):
        category_dropdownlist_option_selector = category_dropdownlist_selector + "/div[@class=\"chosen-drop\"]/ul[@class=\"chosen-results\"]//li[contains(text(),'" + choosing + "')]"

        self.driver.find_element_by_xpath(category_dropdownlist_selector).click()

        self.driver.find_element_by_xpath(category_dropdownlist_option_selector).click()

    def search_products(self):

        self.driver.find_element_by_xpath(search_button).click()




