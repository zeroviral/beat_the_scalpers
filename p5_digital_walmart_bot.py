from selenium import webdriver
from configparser import ConfigParser
from webdriver_manager.chrome import ChromeDriverManager
import time


class P5Bot():

    def __init__(self):

        # VARIABLES
        self.add_to_cart = '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span'
        self.check_out = '//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/button[1]'
        self.continue_without_account = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button/span'
        self.first_continue = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button/span'
        self.first_name = '//*[@id="firstName"]'
        self.last_name = '//*[@id="lastName"]'
        self.email = '//*[@id="email"]'
        self.address = '//*[@id="addressLineOne"]'
        self.phone = '//*[@id="phone"]'
        self.confirm_info = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[2]/div[2]/button/span'
        self.credit_card_num = '//*[@id="creditCard"]'
        self.credit_expire_month = '//*[@id="month-chooser"]'
        self.credit_expire_year = '//*[@id="year-chooser"]'
        self.credit_cvv = '//*[@id="cvv"]'
        self.review_order = '/html/body/div[1]/div/div[1]/div/div[1]/div[' \
                        '3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div/button/span/span/span'
        self.confirm_order = '/html/body/div[1]/div/div[1]/div/div[1]/div[' \
                         '3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button'
        self.not_available_message = '//div[@class="prod-blitz-copy-message"]'

    def order(self):

        # KEYS
        # Add your information here
        config = ConfigParser()
        config.read('config.ini')

        first_name = config.get('main', 'firstName')
        last_name = config.get('main', 'lastName')
        email = config.get('main', 'email')
        address = config.get('main', 'address')
        phone = config.get('main', 'phone')
        cc_num = config.get('main', 'creditCardNum')
        cc_expiry_month = config.get('main', 'creditExpireMonth')
        cc_expiry_year = config.get('main', 'creditExpireYear')
        cvv = config.get('main', 'cvv')

        if not self.verify_if_available(self.not_available_message):
            driver.quit()
            return

        # ADDS PS5 TO CART AND GOES TO CHECKOUT
        self.click_button(self.addToCart)
        self.click_button(self.checkOut)
        self.click_button(self.continueWithoutAccount)

        # FILLS OUT SHIPPING INFO
        self.click_button(self.firstContinue)
        self.enter_data(self.firstName, first_name)
        self.enter_data(self.lastName, last_name)
        self.enter_data(phone, phone)
        self.enter_data(email, email)
        self.enter_data(address, address)
        self.click_button(self.confirmInfo)

        # FILLS OUT PAYMENT
        self.enter_data(self.creditCardNum, cc_num)
        self.enter_data(self.creditExpireMonth, cc_expiry_month)
        self.enter_data(self.creditExpireYear, cc_expiry_year)
        self.enter_data(self.creditCVV, cvv)

        # ORDER
        self.click_button(self.reviewOrder)
        # clickButton(confirmOrder)

    @staticmethod
    def verify_if_available(xpath):
        if len(driver.find_elements_by_xpath(xpath)):
            print("Seems like it's not available currently, exiting program")
            return False
        else:
            return True

    def click_button(self, xpath):
        try:
            driver.find_element_by_xpath(xpath).click()
            pass
        except Exception:
            time.sleep(1)
            self.click_button(xpath)

    def enter_data(self, field, data):
        try:
            driver.find_element_by_xpath(field).send_keys(data)
        except Exception:
            time.sleep(1)
            self.enter_data(field, data)


if __name__ == "__main__":
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # Replace this link with a new value for the link to the version you want

        # Digital edition
        # driver.get('https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815')

        # Physical edition
        driver.get('https://www.walmart.com/ip/PlayStation-5-Console/363472942')
        time.sleep(3)

        ps5bot = P5Bot()
        ps5bot.order()
    except Exception as e:
        print("Exception occured: " + str(e))
        print("\n Quitting chromeDriver...")
        driver.quit()
