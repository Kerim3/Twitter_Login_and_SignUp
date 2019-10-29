from locators import SignInPageLocators
from locators import SignUpPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def clickf(self, by_locator):
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator)).click()

    def assert_elem_text(self, by_locator, elem_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.text == elem_text


class HomePage(BasePage):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver.get("https://twitter.com")


class SignUpPage(BasePage):
    def __init__(self, driver):
        super(SignUpPage, self).__init__(driver)
        self.driver.get("https://twitter.com/i/flow/signup")

    def signup_information_for(self, inf_string1, inf_string2):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SignUpPageLocators.NAME_INPUT)).send_keys(
            inf_string1)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SignUpPageLocators.PHONE_INPUT)).send_keys(inf_string2)


class SignInPage(BasePage):

    def __init__(self, driver):
        super(SignInPage, self).__init__(driver)
        self.driver.get("https://twitter.com/login")

    def signin_information_for(self, inf_string1, inf_string2):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SignInPageLocators.USER_NAME)).send_keys(
            inf_string1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SignInPageLocators.PASSWORD)).send_keys(
            inf_string2)
