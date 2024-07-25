from Pageobjects.lib import Wrapper,read_headers,read_data
from pytest import mark
from Pageobjects.loginPage import LoginPage



# =======================reading the test data from excel sheet============================================================================
# # 8)
headers=read_headers("smoke","test_login_positive")
data=read_data("smoke","test_login_positive")
@mark.parametrize(headers,data)
def test_login_positive_scenarios(pages,email,password):
    pages.load()
    pages.loginpage.click_login()
    pages.loginpage.login(email, password)
    assert pages.loginpage.is_user_logged_in(email) == True

headers=read_headers("smoke", "test_login_negative")
data = read_data("smoke","test_login_negative")
@mark.parametrize(headers,data)
def test_login_negative_scenarios(pages,email,password):
    pages.load()
    pages.loginpage.click_login()
    pages.loginpage.login(email,password)
    assert pages.loginpage.is_user_logged_in(email) == False


#===================7=============================
# we have to import the inbuilt decorator mark from pytest
# we have to create one header and data
# decorate mark above the function of test_login_positive_scenarios


# header ="email","password"
# data= [("bill.gates@company.com","Password123"),
#     ("hello.world@company.com","Password123")
#      ]
# @mark.parametrize(header,data)
#def test_login_positive_scenarios(pages,email,password):
    # wrapper=Wrapper(_driver)
    # wrapper.click_element(("link text","Log in"))
    # wrapper.send_element(("id","Email"),value =email)
    # wrapper.send_element(("id","Password"),value=password)
    # wrapper.click_element(("xpath","//input[@value='Log in']"))

    # login =LoginPage(_driver)
    # login.click_login()
    # login.login(email,password)

#     pages.load()
#     pages.loginpage.click_login()
#     pages.loginpage.login(email,password)
#     assert pages.loginpage.is_user_logged_in(email) ==True
#     pages.homepage.click_logout()
#
# data= [("bill.gates@company.com","123Password"),
#       ("hello.world@company.com","abcpassword")
#       ]
# @mark.parametrize(header,data)
# def test_login_negative_scenarios(pages,email,password):
#     pages.load()
#     pages.loginpage.click_login()
#     pages.loginpage.login(email,password)
#     assert pages.loginpage.is_user_logged_in(email) == False





#1 step           Regular way of writing script
# driver=Chrome()
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# sleep(3)
# driver.find_element("link text","Log in").click()
# sleep(3)
# driver.find_element("id","Email").send_keys("abc@gmail.com")
# sleep(3)
# driver.find_element("id","Password").send_keys("abcpassword")
# sleep(3)
# driver.find_element("xpath","//input[@value='Log in']").click()
# sleep(3)

#==================================================================================
#2 step--------Seperate function creating  for click  and sendkeys
# def click_element(locator_type,locator_value):
#     driver.find_element(locator_type,locator_value).click()
# def send_element(locator_type,locator_value,value):
#     driver.find_element(locator_type,locator_value).clear()
#     driver.find_element(locator_type,locator_value).send_keys(value)

#====================================================================
#3 step (using the fuction created in step 2 used here)
# driver=Chrome()
# driver.maximize_window()
# driver.get("https://demowebshop.tricentis.com/")
#
# click_element("link text","Log in")
#
# send_element("id","Email","abc@gmail.com")
#
# send_element("id","Password","abssdr")
#
# click_element("xpath","//input[@value='Log in']")
# driver.close()

#===============================================================================
#4

# def click_element(locator):
#     print(f"clicking on {locator}")
#     driver.find_element(*locator).click()
#     sleep(2)
#
# def send_element(locator,*,value):
#     print(f"clicking on {locator}")
#     driver.find_element(*locator).clear()
#     sleep(2)
#     driver.find_element(*locator).send_keys(value)
#     sleep(2)

# driver=Chrome()
# driver.maximize_window()
# driver.get("https://demowebshop.tricentis.com/")
#
# click_element(("link text","Log in"))
# send_element(("id","Email"),value ="abc@gmail.com")
# send_element(("id","Password"),value="abssdr")
# click_element(("xpath","//input[@value='Log in']"))
# driver.close()

#===============================================================================
#5 separete class i created in lib.py(Wrapper class and object  created here)

# driver=Chrome()
# driver.maximize_window()
# driver.get("https://demowebshop.tricentis.com/")
# wrapper=Wrapper(driver)
# wrapper.click_element(("link text","Log in"))
# wrapper.send_element(("id","Email"),value ="abc@gmail.com")
# wrapper.send_element(("id","Password"),value="abssdr")
# wrapper.click_element(("xpath","//input[@value='Log in']"))
# driver.close()


#==============================================================================================================

#6
# Rename the file from login.py to test_login.py
# Remove the First 3 and last line from the script

# def test_login_positive_scenarios(_driver):
#     wrapper=Wrapper(_driver)
#     wrapper.click_element(("link text","Log in"))
#     wrapper.send_element(("id","Email"),value ="abc@gmail.com")
#     wrapper.send_element(("id","Password"),value="abssdr")
#     wrapper.click_element(("xpath","//input[@value='Log in']"))