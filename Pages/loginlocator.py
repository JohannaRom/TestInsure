from selenium.webdriver.common.by import By


class LoginLocator:
    emailfield=(By.NAME,"email")
    passwordfield=(By.NAME,"password")
    loginbtn=(By.NAME,"submit")
    textwelcome="Broker Insurance WebPage"
    loginsuccess=(By.XPATH,"//*[text()='Broker Insurance WebPage']")
