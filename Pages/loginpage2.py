from pages.basepage import BasePage
from pages.loginlocator import LoginLocator
from resources.constants import MAX_WAIT_INTERVAL


class LoginPage(BasePage):

    def loginusernamepassword(self,userpass):
        self.findelementuserpass(LoginLocator.emailfield,userpass[0])
        self.findelementuserpass(LoginLocator.passwordfield, userpass[1])

    def submitafterlogin(self):
        self.explicitlywaitelementclick(MAX_WAIT_INTERVAL,LoginLocator.loginbtn)

    def successloginpage(self):
        successtext= self.getattributeofelement(MAX_WAIT_INTERVAL,LoginLocator.loginsuccess).text
        if successtext==LoginLocator.textwelcome:
            print("Login successful")
        else:
            print("Unsuccessful Login")