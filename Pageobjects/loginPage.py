from Pageobjects.lib import Wrapper ,read_locator
from Pageobjects.homepage import HomePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
#1===============================================================================
class LoginPage(HomePage):
    def login(self,email,password):
        wrapper=Wrapper(self.driver)
        wrapper.send_element(("id", "Email"), value=email)
        wrapper.send_element(("id", "Password"), value=password)
        wrapper.click_element(("xpath", "//input[@value='Log in']"))
#


#2  Read the data from the script ======================================================================
class LoginPage(HomePage):

    locators={
        "txt_email":("name","email"),
        "txt_password":("id","password"),
        "btn_login":("xpath","//input[@value='log in']")
    }
    def login(self,email,password):
#
        wrapper = Wrapper(self.driver)
        wrapper.send_element(self.locators["txt_email"], value=email)
        wrapper.send_element(self.locators["txt_password"], value=password)
        wrapper.click_element(self.locators["btn_login"])


 #3---------Read data from Excell sheet locaters================================================================
class LoginPage(HomePage):

    locators = read_locator("loginpage") # "loginpage"-sheetname from the excelsheet

    def login(self,email,password):
        wrapper=Wrapper(self.driver)
        wrapper.send_element(self.locators["txt_email"], value=email)
        wrapper.send_element(self.locators["txt_password"], value=password)
        wrapper.click_element(self.locators["btn_login"])


    def is_user_logged_in(self,email):
        for _ in range(5):
            try:
                element = self.driver.find_element("xpath",f"//a[text()='{email}']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False