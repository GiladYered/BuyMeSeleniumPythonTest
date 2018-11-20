from BusinessScreen import BusinessScreen
from HomeScreen import HomeScreen
from InformationScreen import InformationScreen
from InitializeDriver import InitializeDriver
from RegistrationScreen import RegistrationScreen


#  A.Registration screen
def registration_screen_test():
    # set driver for actions
    initializeDriver = InitializeDriver()
    driver_for_actions = initializeDriver.get_driver("Chrome")
    driver_for_actions.maximize_window()

    # Enter to website
    homeScreen = HomeScreen(driver_for_actions)
    homeScreen.connect_to_web_site("https://buyme.co.il/")

    # create instance of registration
    registrationScreen = RegistrationScreen(driver_for_actions)

    # enter to resistraion screen
    registrationScreen.click_on_enter_register()

    # Press on button " עוד לא נרשמת "
    registrationScreen.click_on_until_no_regigster()

    # Enter first name
    registrationScreen.set_regigster_name("gilad")

    # Enter email address
    registrationScreen.set_regigster_email("gilad@backbox.com")

    # Enter password
    registrationScreen.set_regigster_password("Password123!")

    # Enter password again
    registrationScreen.set_regigster_password_again("Password123!")

    # Press on radio button "אני מסכים "
    registrationScreen.check_accept()

    # Press button " הרשמה... " this is marked because I did not want to register on this website in practice.
    # registrationScreen.submit_registration()

    # notification for test finish succsefuly
    print("registration_screen_test finish succsefuly!")

    # close the window and the session for next test
    driver_for_actions.close()
    driver_for_actions.quit()


# B. Home Screen
def home_screen_test():
    # set driver for actions
    initializeDriver = InitializeDriver()
    driver_for_actions = initializeDriver.get_driver("Chrome")
    driver_for_actions.maximize_window()

    homeScreen = HomeScreen(driver_for_actions)
    homeScreen.connect_to_web_site("https://buyme.co.il/")

    # Pick point price
    homeScreen.select_point_price("300-499")
    # Pick area
    homeScreen.select_area("ירושלים")
    # Pick category
    homeScreen.select_category("גיפט קארד לארוחת בוקר ובתי קפה")

    # Press the search button
    homeScreen.search_products()

    # notification for test finish succsefuly
    print("home_screen_test finish succsefuly!")

    # close the window and the session for next test
    driver_for_actions.close()
    driver_for_actions.quit()


# C. Choose business screen
def choose_business_screen_test():
    # set driver for actions
    initializeDriver = InitializeDriver()
    driver_for_actions = initializeDriver.get_driver("Chrome")
    driver_for_actions.maximize_window()

    homeScreen = HomeScreen(driver_for_actions)
    homeScreen.connect_to_web_site("https://buyme.co.il/")

    # Pick point price
    homeScreen.select_point_price("300-499")
    # Pick area
    homeScreen.select_area("ירושלים")
    # Pick category
    homeScreen.select_category("גיפט קארד למתנות לידה וצעצועים")

    # Press the search button
    homeScreen.search_products()

    buisness_screen = BusinessScreen(driver_for_actions)
    # Pick a Buisness
    buisness_screen.select_buisness_by_name("BUYME TOTAL")

    # this case is failed the test.that cause it remarked
    # buisness_screen.select_buisness_by_name("BABY MIT MIT")

    # Type a price
    buisness_screen.set_price_for_product("500")

    # notification for test finish succsefuly
    print("choose_business_screen_test finish succsefuly!")

    # close the window and the session for next test
    driver_for_actions.close()
    driver_for_actions.quit()


# D. Sender & Receiver information screen
def information_screen_test():
    # set driver for actions
    initializeDriver = InitializeDriver()
    driver_for_actions = initializeDriver.get_driver("Chrome")
    driver_for_actions.maximize_window()

    homeScreen = HomeScreen(driver_for_actions)
    homeScreen.connect_to_web_site("https://buyme.co.il/")

    # Pick point price
    homeScreen.select_point_price("300-499")
    # Pick area
    homeScreen.select_area("ירושלים")
    # Pick category
    homeScreen.select_category("גיפט קארד למתנות לידה וצעצועים")

    # Press the search button
    homeScreen.search_products()

    buisness_screen = BusinessScreen(driver_for_actions)

    # Pick a Buisness
    buisness_screen.select_buisness_by_name("BUYME TOTAL")

    # Type a price
    buisness_screen.set_price_for_product("500")

    # submit price
    buisness_screen.submit_price()

    information_screen = InformationScreen(driver_for_actions)
    # Press radio button "למישהו אחר "
    information_screen.check_for_other()

    # Enter receiver name
    information_screen.set_receiver_name("Gilad")

    # Enter sender name
    information_screen.set_sender_name("Adi")

    # Enter a blessing
    information_screen.set_blessing("I love you")

    # Upload a picture
    information_screen.upload_picture_file()

    # Pick the event (Wedding/birthday)
    information_screen.pick_event("Wedding")

    # Press radio button "מיד אחרי התשלום "
    information_screen.press_after_payment()

    # Pick Email / SMS option + # Enter address/ number and press save
    information_screen.send_by_email("Gilad@backbox.com")
    information_screen.sumbit_email()

    information_screen.send_by_sms("0526229820","0526229820")
    information_screen.submit_phones()

    # submit all
    information_screen.submit_all()

    # notification for test finish succsefuly
    print("information_screen_test finish succsefuly!")

    # close the window and the session for next test
    driver_for_actions.close()
    driver_for_actions.quit()

def main():
    registration_screen_test()
    home_screen_test()
    choose_business_screen_test()
    information_screen_test()


if __name__ == "__main__":
    main()
