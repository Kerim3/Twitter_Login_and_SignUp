from selenium.webdriver.common.by import By


class CommonPageLocators:
    SIGN_UP = (By.LINK_TEXT, "Sign up")
    LOG_IN = (By.LINK_TEXT, "Log in")


class SignUpPageLocators:
    NAME_INPUT = (By.NAME, "name")
    PHONE_INPUT = (By.NAME, "phone_number")
    NEXT_BUTTON = (By.CSS_SELECTOR,
                   ".css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1vsu8ta.r-aj3cln.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr")
    NEXT_BUTTON2 = (By.CSS_SELECTOR, ".r-1joea0r.r-1vsu8ta.r-18qmn74 > div")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, ".r-jwli3a")
    OK_BUTTON = (By.CSS_SELECTOR, ".css-18t94o4:nth-child(2) > .css-901oao > .css-901oao > .css-901oao")
    VER_CODE = (By.NAME, "verfication_code")


class SignInPageLocators:
    USER_NAME = (
        By.CSS_SELECTOR, "#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input")
    PASSWORD = (
        By.CSS_SELECTOR, "#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#page-container > div > div.signin-wrapper > form > div.clearfix > button")
