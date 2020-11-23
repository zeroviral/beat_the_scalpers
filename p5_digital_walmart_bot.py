from selenium import webdriver
from configparser import ConfigParser
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time


class P5Bot():

    def __init__(self):

        # VARIABLES
        self.add_to_cart = '//button[@data-tl-id="ProductPrimaryCTA-cta_add_to_cart_button"]'
        self.check_out = '//span[contains(text(), "Check out")]'
        self.continue_without_account = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button/span'
        self.continue_to_delivery = '//button[@aria-label="Continue to Delivery Address"]'
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
        self.review_order = '//span[contains(text(), "Review your order")]'
        self.confirm_order = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button'
        self.not_available_message = '//div[@class="prod-blitz-copy-message"]'

    def order(self):

        # KEYS
        # Add your information here
        config = ConfigParser()
        config.read('config.ini')

        print_list = []
        first_name = config.get('main', 'firstName')
        last_name = config.get('main', 'lastName')
        email = config.get('main', 'email')
        address = config.get('main', 'address')
        phone = config.get('main', 'phone')
        cc_num = config.get('main', 'creditCardNum')
        cc_expiry_month = config.get('main', 'creditExpireMonth')
        cc_expiry_year = config.get('main', 'creditExpireYear')
        cvv = config.get('main', 'cvv')

        print_list.append(first_name)
        print_list.append(last_name)
        print_list.append(email)
        print_list.append(address)
        print_list.append(phone)
        print_list.append(cc_num)
        print_list.append(cc_expiry_month)
        print_list.append(cc_expiry_year)
        print_list.append(cvv)

        print("Current values: " + str(print_list))

        if not self.verify_if_available(self.not_available_message):
            driver.quit()
            return

        # ADDS PS5 TO CART AND GOES TO CHECKOUT
        self.click_button(self.add_to_cart)
        self.click_button(self.check_out)
        self.click_button(self.continue_without_account)

        # FILLS OUT SHIPPING INFO
        self.click_button(self.continue_to_delivery)
        self.enter_data(self.first_name, first_name)
        self.enter_data(self.last_name, last_name)
        self.enter_data(phone, phone)
        self.enter_data(email, email)
        self.enter_data(address, address)
        self.click_button(self.confirm_info)

        # FILLS OUT PAYMENT
        self.enter_data(self.credit_card_num, cc_num)
        self.enter_data(self.credit_expire_month, cc_expiry_month)
        self.enter_data(self.credit_expire_year, cc_expiry_year)
        self.enter_data(self.credit_cvv, cvv)

        # ORDER
        self.click_button(self.reviewOrder)
        self.clickButton(self.confirmOrder)

    @staticmethod
    def verify_if_available(xpath):
        if len(driver.find_elements_by_xpath(xpath)):
            print("Seems like it's not available currently, exiting program")
            return False
        else:
            return True

    @staticmethod
    def click_button(xpath):
        try:
            # time.sleep(1.5)
            driver.find_element_by_xpath(xpath).click()
        except NoSuchElementException:
            print("Element not found: " + xpath)
            print("\nExiting program...")
            driver.quit()
            exit(1)

    def enter_data(self, field, data):
        try:
            driver.find_element_by_xpath(field).send_keys(data)
            self.enter_data(field, data)
        except NoSuchElementException:
            print("Field not found for text entry: " + field)
            print("\nExiting Program...")
            driver.quit()
            exit(1)


if __name__ == "__main__":
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)

        # Digital edition
        # driver.get('https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815')

        # Physical edition
        driver.get('https://www.walmart.com/ip/PlayStation-5-Console/363472942')

        # Test URL
        # driver.get('https://www.walmart.com/ip/Apple-AirPods-Pro/520468661')
        time.sleep(3)

        ps5bot = P5Bot()
        ps5bot.order()

    except Exception as e:
        print("Exception occured: " + str(e))
        print("\n Quitting chromeDriver...")
        driver.quit()
