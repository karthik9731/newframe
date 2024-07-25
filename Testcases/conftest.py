from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.safari.webdriver import WebDriver as Safari
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from pytest import fixture
from Pageobjects.homepage import HomePage
from Pageobjects.loginPage import LoginPage
from Pageobjects.registrationpage import RegistrationPage
from selenium import webdriver
#
allowed_environment = ("test", "stage")
allowed_browser = ("chrome", "firefox", "safari", "edge")
#
# # #Hook Function this will execute first before the test case execution
# # # You Can take command line argument
# # # parser is an inbult fixture which is used to create that command line arguments
def pytest_addoption(parser):
    parser.addoption("--env", action="store", dest="env", default="test", choices=allowed_environment)
    parser.addoption("--browser", action="store", dest="browser", default="chrome", choices=allowed_browser)


# #request is an inbuild fixture which is used to read the data from parser
@fixture
def _driver(request):
    browser_type = request.config.option.browser.capitalize()  #config some other config sir not explained
    driver = getattr(webdriver,browser_type)()  # #driver = Chrome() callable,----grtatr() is method
    yield driver
    driver.close()
    browser_type = request.config.option.browser

    if browser_type.upper()=="CHROME":
        driver=webdriver.Chrome()
    elif browser_type.upper()=="FIREFOX":
        driver =webdriver.Firefox()
    elif browser_type.upper()=="EDGE":
        driver = webdriver.Edge()
    elif browser_type.upper()=="SAFARI":
        driver =Safari()

    print("*********** setting *************")
    driver = Chrome()

    yield driver
    print("*********** teardown ***********")
    driver.close()
#
#
@fixture
def config(request):
    execution_env = request.config.option.env  # config also some other config not this function config
    if execution_env.upper()=="TEST":
        return TestConfigration()

    elif execution_env.upper()=="STAGE":
        return StageConfigration()
    else:
        raise Exception("Unknown Configration")

class TestConfigration:
    ''' TO MAINTAIN ALL TEST ENVIRONMENT CONFIGURATIONS '''
    url="https://demowebshop.tricentis.com/"
    email="hello.world@company.com"
    password= "Password123"

class StageConfigration:
    '''TO MAINTAIN ALL STAGE ENVIRONMENT RELATED CONFIGURATIONS'''
    url = "https://demowebshop.tricentis.com/"
    email = "hello.world@company.com"
    password = "Password123"

#
# # # env="test"

#
@fixture
def pages(_driver, config):
    class Pages:
        homepage = HomePage(_driver)
        loginpage = LoginPage(_driver)
        registrationpage = RegistrationPage(_driver)

        def load(self):
            _driver.get(config.url)
            _driver.maximize_window()


    return Pages()