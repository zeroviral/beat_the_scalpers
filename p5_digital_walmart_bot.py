from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def order():
    # VARIABLES
    addToCart = '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span'
    checkOut = '//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/button[1]'
    continueWithoutAccount = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button/span'
    firstContinue = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button/span'
    firstName ='//*[@id="firstName"]'
    lastName = '//*[@id="lastName"]'
    email = '//*[@id="email"]'
    address = '//*[@id="addressLineOne"]'
    phone = '//*[@id="phone"]'
    confirmInfo = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[2]/div[2]/button/span'
    creditCardNum = '//*[@id="creditCard"]'
    creditExpireMonth = '//*[@id="month-chooser"]'
    creditExpireYear = '//*[@id="year-chooser"]'
    creditCVV = '//*[@id="cvv"]'
    reviewOrder = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div/button/span/span/span'
    confirmOrder = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button'
    notAvailableMessage = '//div[@class="prod-blitz-copy-message"]'

    # KEYS
    # Add your information here
    myFirstName = 'John'
    myLastName = 'Smith'
    myEmail = 'mail@gmail.com'
    myAddress = '1234 Apple Lane'
    myPhone = '1234567890'
    myCreditCardNum = '123456789'
    myCreditExpireMonth = '00'
    myCreditExpireYear = '25'
    myCVV = '123'

    if not verify_if_available(notAvailableMessage):
        driver.quit()
        return

    # ADDS PS5 TO CART AND GOES TO CHECKOUT
    click_button(addToCart)
    click_button(checkOut)
    click_button(continueWithoutAccount)

    # FILLS OUT SHIPPING INFO
    click_button(firstContinue)
    enter_data(firstName, myFirstName)
    enter_data(lastName, myLastName)
    enter_data(phone, myPhone)
    enter_data(email, myEmail)
    enter_data(address, myAddress)
    click_button(confirmInfo)

    # FILLS OUT PAYMENT
    enter_data(creditCardNum, myCreditCardNum)
    enter_data(creditExpireMonth, myCreditExpireMonth)
    enter_data(creditExpireYear, myCreditExpireYear)
    enter_data(creditCVV, myCVV)


    # ORDER
    click_button(reviewOrder)
    # clickButton(confirmOrder)


def verify_if_available(xpath):
    if len(driver.find_elements_by_xpath(xpath)):
        print("Seems like it's not available currently, exiting program")
        return False
    else:
        return True


def click_button(xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
        pass
    except Exception:
        time.sleep(1)
        click_button(xpath)


def enter_data(field, data):
    try:
        driver.find_element_by_xpath(field).send_keys(data)
        pass
    except Exception:
        time.sleep(1)
        enter_data(field, data)


if __name__ == "__main__":
    # driver = webdriver.Chrome("./chromedriver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # Replace this link with a new value for the link to the version you want
    driver.get('https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815')
    time.sleep(3)
    order()