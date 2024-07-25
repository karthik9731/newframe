from Pageobjects.lib import Wrapper,read_locator
from Pageobjects.homepage import HomePage
from selenium.common.exceptions import NoSuchElementException
from time import sleep
class RegistrationPage(HomePage):
    locators=read_locator("registrationpage")
    def registration(self,gender,fname,lname,email,password,confirmpassword):
        wrapper = Wrapper(self.driver)
        if gender == "male":
            wrapper.click_element(("id","gender-male"))
        else:
            wrapper.click_element(("id", "gender-female"))
        wrapper.send_element(("id","FirstName"),value=fname)
        wrapper.send_element(("id","LastName"),value=lname)
        wrapper.send_element(("id","Email"),value=email)
        wrapper.send_element(("id","Password"),value=password)
        wrapper.send_element(("id","ConfirmPassword"),value=password)
        wrapper.click_element(("name", "register-button"))

#============================================Reading from the excel sheet==============================================
        wrapper = Wrapper(self.driver)
        if gender == "male":
            wrapper.click_element(self.locators["rdo_male"])
        else:
            wrapper.click_element(self.locators["rdo_female"])
        wrapper.send_element(self.locators["txt_fname"], value=fname)
        wrapper.send_element(self.locators["txt_lname"], value=lname)
        wrapper.send_element(self.locators["txt_email"], value=email)
        wrapper.send_element(self.locators["txt_password"], value=password)
        wrapper.send_element(self.locators["txt_confirmpassword"], value=confirmpassword)
        wrapper.click_element(self.locators["btn_register"])
    def is_user_registered(self):
        for _ in range(5):
            try:
                element=self.driver.find_element("xpath","//div[@class='result']")
                element.is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False