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


header ="email","password"
data= [("bill.gates@company.com","Password123"),
    ("hello.world@company.com","Password123")
     ]
@mark.parametrize(header,data)
def test_login_positive_scenarios(pages,email,password):
    wrapper=Wrapper(_driver)
    wrapper.click_element(("link text","Log in"))
    wrapper.send_element(("id","Email"),value =email)
    wrapper.send_element(("id","Password"),value=password)
    wrapper.click_element(("xpath","//input[@value='Log in']"))

    login =LoginPage(_driver)
    login.click_login()
    login.login(email,password)

    pages.load()
    pages.loginpage.click_login()
    pages.loginpage.login(email,password)
    assert pages.loginpage.is_user_logged_in(email) ==True
    pages.homepage.click_logout()

data= [("bill.gates@company.com","123Password"),
      ("hello.world@company.com","abcpassword")
      ]
@mark.parametrize(header,data)
def test_login_negative_scenarios(pages,email,password):
    pages.load()
    pages.loginpage.click_login()
    pages.loginpage.login(email,password)
    assert pages.loginpage.is_user_logged_in(email) == False

