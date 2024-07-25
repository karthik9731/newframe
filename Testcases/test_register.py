from Pageobjects.lib import Wrapper,read_headers,read_data
from pytest import mark
from Pageobjects.registrationpage import RegistrationPage
from Pageobjects.loginPage import LoginPage

#1============================================================================================================================
header="gender,fname,lname,email,password"
data=[("male","Karthik","c","ckarthikc@gmail.com","Karthik@12")]
#
@mark.parametrize(header,data)
def test_registration(pages,gender,fname,lname,email,password):# _driver is fixture it is passing
    wrapper = Wrapper(_driver)
    wrapper.click_element(("link text","Register"))
    if gender=="male":
        wrapper.click_element(("id","gender-male"))
    else:
        wrapper.click_element(("id", "gender-female"))
    wrapper.send_element(("id","FirstName"),value=fname)
    wrapper.send_element(("id","LastName"),value=lname)
    wrapper.send_element(("id","Email"),value=email)
    wrapper.send_element(("id","Password"),value=password)
    wrapper.send_element(("id","ConfirmPassword"),value=password)
    wrapper.click_element(("name", "register-button"))

    registration =RegistrationPage(_driver)
    registration.click_register()
    registration.registration(gender,fname,lname,email,password)

    pages.load()
    pages.registrationpage.click_register()
    pages.registrationpage.registration(gender,fname,lname,email,password)

#===================================================================================================================================
# 2 doing verification and validation using assert
header="gender,fname,lname,email,password"
data=[("male","Karthik","c","ckarthikc@gmail.com","Karthik@12")]
@mark.parametrize(header,data)
def test_registration_unique(pages,gender,fname,lname,email,password):# _driver is fixture it is passing

    pages.load()
    pages.registrationpage.click_register()
    pages.registrationpage.registration(gender,fname,lname,email,password)
    assert pages.registrationpage.is_user_registered()==True


data=[("male","Karthik","c","ckarthikc@gmail.com","Karthik@12C")]
@mark.parametrize(header,data)
def test_registration_duplicate(pages,gender,fname,lname,email,password):# _driver is fixture it is passing

    pages.load()
    pages.registrationpage.click_register()
    pages.registrationpage.registration(gender,fname,lname,email,password)
    assert pages.registrationpage.is_user_registered()==False

#=======================================3  Reading locators from xl sheet==============================================================================================

header="gender,fname,lname,email,password"
data=[("male","Karthik","c","ckarthikc@gmail.com","Karthik@12")]

header=read_headers("smoke","test_registration")
data=read_data("smoke","test_registration")
@mark.parametrize(header,data)
def test_registration_unique(pages,gender,fname,lname,email,password,confirmpassword):# _driver is fixture it is passing

    pages.load()
    pages.registrationpage.click_register()
    pages.registrationpage.registration(gender,fname,lname,email,password,confirmpassword)
    assert pages.registrationpage.is_user_registered()==True