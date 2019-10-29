import unittest
from selenium import webdriver
from page import HomePage
from page import SignUpPage
from page import SignInPage
from locators import SignInPageLocators
from locators import CommonPageLocators
from locators import SignUpPageLocators
import time


class TestPyOrgBase(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('headless')
        chrome_options.add_argument('--start-maximized')
        #self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Remote(command_executor='http://192.168.1.49:4445/wd/hub', desired_capabilities = chrome_options.to_capabilities())

    def tearDown(self):
        self.driver.close()


class TestHome(TestPyOrgBase):
    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)

    def test_TC001_sign_up(self):
        self.home.clickf(CommonPageLocators.SIGN_UP)

    def test_TC002_sign_in(self):
        self.home.clickf(CommonPageLocators.LOG_IN)


class TestSignUp(TestPyOrgBase):
    def setUp(self):
        super().setUp()
        self.signup = SignUpPage(self.driver)

    def test_TC003_SignUp(self):
        self.signup.signup_information_for("test", "05555555555")
        # time.sleep(5)
        self.signup.clickf(SignUpPageLocators.NEXT_BUTTON)
        self.signup.clickf(SignUpPageLocators.NEXT_BUTTON2)
        self.signup.clickf(SignUpPageLocators.SIGN_UP_BUTTON)
        self.signup.clickf(SignUpPageLocators.OK_BUTTON)
        self.signup.clickf(SignUpPageLocators.VER_CODE)


class TestSignIn(TestPyOrgBase):
    def setUp(self):
        super().setUp()
        self.signin = SignInPage(self.driver)

    def test_TC004_SignIn(self):
        self.signin.signin_information_for("test@getnada.com", "1234567a")
        self.signin.clickf(SignInPageLocators.LOGIN_BUTTON)


if __name__ == '__main__':
    unittest.main()
