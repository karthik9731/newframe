from Pageobjects.lib import Wrapper
class HomePage:
    def __init__(self,driver):
        self.driver= driver
    def click_login(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("link text", "Log in"))

    def click_register(self):
        wrapper= Wrapper(self.driver)
        wrapper.click_element(("link text", "Register"))

    def click_logout(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element("link text","Log out")