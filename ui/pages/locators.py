"""LOCATORS FOR PAGES"""

from selenium.webdriver.common.by import By


class LoginPageLocators:

    BTN_FEEDBACK_SURVEY = (By.CSS_SELECTOR, 'button.uui-button-box')
    BTN_EPAM_LOGIN = (By.CSS_SELECTOR, 'button.Button__button.Button__blue.SsoAuthLinks__epamSsoButton')
    BTN_GITHUB_LOGIN = (By.CSS_SELECTOR, 'button.Button__button.Button__darkGray')
    BTN_SIGN_IN = (By.CSS_SELECTOR, 'button[type="submit"]')
    BTN_QUICK_ACCESS = (By.CSS_SELECTOR, 'button.Button__button.Button__blueTransparent')
    BTN_QA_CANCEL = (By.CSS_SELECTOR, 'button.Button__button.Button__blueTransparent')
    BTN_QA_ENTER = (By.CSS_SELECTOR, 'button.Button__button.Button__blue.styles__actionButton')

    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[placeholder="Enter Your Email"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[placeholder="Enter Your Password"]')
    INPUT_QA_NAME = (By.CSS_SELECTOR, 'input[placeholder="Enter Your Name"]')

    LINK_HEADER_LOGO = (By.CSS_SELECTOR, 'a[href="/poker"]')
    LINK_RECOVER_MY_PASSWORD = (By.CSS_SELECTOR, 'a.SignInForm__recoverLink')
    LINK_SIGN_UP = (By.CSS_SELECTOR, 'a.TextLink__link')

    TEXT_MAIN_TITLE = (By.CSS_SELECTOR, 'h2.WelcomeTitle__title')
    TEXT_SIGN_IN = (By.CSS_SELECTOR, 'h4.Subtitle__secondaryTitle')
    TEXT_DONT_HAVE_ACCOUNT = (By.CSS_SELECTOR, 'div.TextLink__container > span')
    TEXT_QA_QUICK_ACCESS = (By.CSS_SELECTOR, 'h4.Subtitle__secondaryTitle')
    TEXT_QA_NOTICE = (By.CSS_SELECTOR, 'p.QuickAccessForm__noticeMessage')

    PIC_EPAM_LOGO = (By.CSS_SELECTOR, 'img[alt="epam-logo"]')

    MODAL_WHATS_NEW = (By.CSS_SELECTOR, 'div.ant-modal-content')

    ERR_MESSAGE_EMAIL = (By.CSS_SELECTOR, 'div[data-testid="text-field-error"]')
    ERR_POP_UP = (By.CSS_SELECTOR, 'div.uui-snackbar-item-self')
