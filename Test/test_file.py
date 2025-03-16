from pages.loginpage2 import LoginPage
#from pages.quotationcheckpage3 import RequestQuotationCheck
#from pages.quotationpage3 import RegisterQuotation
#from pages.registerformpage1 import RegisterPage
import time

from resources.constants import TEST_SITE_URL


#from pages.retrievequotation4 import RetrieveQuotation


class Testcases:
    # Test Case 1 Using the credentials created in the test case1 trying Logging in successfully
    def test_login(self,driver,username_password):
        user1login=LoginPage(driver)
        user1login.navigateto(TEST_SITE_URL)
        user1login.loginusernamepassword(username_password)
        user1login.submitafterlogin()
        user1login.successloginpage()
        time.sleep(5)
        print("Test1 complete")

    """#Test Case 1 Going to the website, clicking Register button,pytest
    # Filling the signup as new userform
    def test_registeruser(self, driver, username_password):
        user1form=RegisterPage(driver)
        user1form.waitandselectdropdown()
        user1form.findelementuserpassandtype(username_password)
        user1form.submitbutnclick()
        user1form.pageattibute()
        print("Test1 complete")

        #time.sleep(10)
    
    #Test Case 3 Clicking the request quotation tab and filling in details and calculating premium
    # and saving quotation and storing the unique identification number in a txt file and going back to the main page
    def test_quotationrequest(self,driver):
        user1request=RequestQuotation(driver)
        user1request.checkurl(driver)
        user1request.checkforrequestquotationbtn()
        premiumamt=user1request.successquotationpage()
        try:
            assert premiumamt!='',"Premium amount not calculated"
        except Exception as e:
            print("An error ocurred: %" % e)
        else:
            print("Premium amount calculated is with " premiumamt)
            user1request.savequotation()
        finally:
            print("Test3 complete")

#Test Case4 Clicking the request quotation tab and filling in details except vehicle value field and clicking
# calculation premium. A color change in the 'Estimated value' is seen which is asserted and unsuccessful
# premium calculation is also asserted"""