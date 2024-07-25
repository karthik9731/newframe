from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from xlrd import open_workbook


#3=========  Read data from the Excel sheet(locator)=======================================================

def read_locator(sheetname):
    workbook = open_workbook(r"C:\Users\ckart\PycharmProjects\pythonProject1\newframe\TestData\objects.xls")
    excelsheet = workbook.sheet_by_name(sheetname)
    used_rows = excelsheet.nrows  #all the values in row
    data ={}
    for i in range(1,used_rows):
        temp_data = excelsheet.row_values(i) # it will return the values in the form of List stored in temp_data
        data[temp_data[0]]=(temp_data[1],temp_data[2])   # data={"link_register":("link_test","Register")}
    return data

#reading test data from excel sheet
def read_headers(sheetname,script_name):
    """return headers in comma seperated string"""
    workbook = open_workbook(r"C:\Users\ckart\PycharmProjects\pythonProject1\newframe\TestData\testdata.xls")
    excel_sheet = workbook.sheet_by_name(sheetname)
    used_rows = excel_sheet.nrows
    for i in range(0,used_rows):
        row = excel_sheet.row_values(i)
        if row[0]==script_name:
            headers = excel_sheet.row_values(i-1)
            headers=[item for item in headers if item.strip()] # List combrehension
            return ",".join(headers[2:])

def read_data(sheetname,script_name):
    """return data in the form of list of tuple"""
    workbook = open_workbook(r"C:\Users\ckart\PycharmProjects\pythonProject1\newframe\TestData\testdata.xls")
    excel_sheet = workbook.sheet_by_name(sheetname)
    used_rows = excel_sheet.nrows
    final_data=[]
    for i in range(0,used_rows):
        row = excel_sheet.row_values(i)
        if row[0]==script_name:
            # remove the unwanted space
            data=[item for item in row if item.strip()]
            # Only i intrested if Execute column is YES
            if data[1]=="Yes":
                final_data.append(tuple(data[2:]))
    return final_data





#2=====wait decorator========

#=======================================================================================================
#  2)
# in decorator we have to create a function usally in decorator we create two function one function inside other function
# in 2nd function we are giving two argument *args(it will accept any number of positional arguments)value stored in the form of tuple
#**kwargs we used for keyword arguments in kwargs value will be stored in the form of dictionary(K:W)pair
def _wait(func):
    def _wrapper(*args,**kwargs):
        # write the logic to wait for the elements
        instance=args[0] # instance is nothing but self
        _locator =args[1] # _locator =("link text","Register")
        # w = WebDriverWait(driver, 20)
        # w.until(visibility_of_element_located(locator)
        w=WebDriverWait(instance.driver,20)      #    WebDriverWait(self.driver,20)
        w.until(visibility_of_element_located(_locator))
        # execute the original function (click, enter, select)
        # original function gets executed only if there is not exception
        # in until
        return func(*args, **kwargs)
    return _wrapper

# Class decorator

# def wait(cls):
#1)==================================
class Wrapper:
    def __init__(self,driver):
        self.driver=driver

    @_wait    # click_element = wait(click_element)
    def click_element(self,locator):
        print(f"clicking on {locator}")
        # sleep(2)
        self.driver.find_element(*locator).click()

    @_wait    #send_element = wait(send_element)
    def send_element(self,locator, *, value):
        print(f"clicking on {locator}")
        # sleep(2)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @_wait   # select_item =
    def select_item(self,locator,*,item):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(item)

    @_wait  # mouse_hover = wait(mouse_hover)
    def mouse_hover(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @_wait
    def something(self):
        ...

    @_wait
    def get_alert_text(self):


        ...