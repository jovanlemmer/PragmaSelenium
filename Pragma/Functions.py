from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



#Open Browser & Website
driver = WebDriver = webdriver.Chrome(executable_path='C:\\Users\iPay\AppData\Local\Programs\Python\Python37-32\Scripts\chromedriver.exe')

def openURL(URL):
    try:
        driver.get(URL)
        driver.maximize_window()
        print("Browser opened successful")
    except Exception as e:
        print("Open Browser Unsuccessful")
        print(e)

def click_on_element(element, locator_type):
    try:
        ClickButton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((locator_type, element)))
        ClickButton.click()
        print("Successfully Click")
    except Exception as e:
        print("Unsuccessfull Click")
        print(e)

#Hover Click
def hover_click(hoverclick_element, hover_locator_type, drp_element, drp_locator_type):
    try:
        hover_on_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((hover_locator_type, hoverclick_element)))
# Create an ActionChains object
        actions = ActionChains(driver)
# Hover over the element
        actions.move_to_element(hover_on_element)
# Perform the hover action
        actions.perform()
# Now, locate the element to select (which becames visible after hovering)
        ElementInDropdownList = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((drp_locator_type, drp_element)))
        ElementInDropdownList.click()
        print("Successfull Hover & Click on dropdown")
    except Exception as e:
        print("Unsuccessfull Click")
        print(e)

#Hover
def hover(hover_element, hover_locator_type):
    try:
        hover_on_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((hover_locator_type, hover_element)))
# Create an ActionChains object
        actions = ActionChains(driver)
# Hover over the element
        actions.move_to_element(hover_on_element)
# Perform the hover action
        actions.perform()
        print("Successfull Hover & Click on dropdown")
    except Exception as e:
        print("Unsuccessfull Click")
        print(e)


def validate_text_value(element, locator_type, assert_value):
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((locator_type, element)))
    if elem.is_displayed():
        value = elem.text
        if value == assert_value:
            print(f"Element {locator_type} used: {element}")
            print(f"Value Found: {value}")
            print(f"Expected value: {assert_value}, text found - PASSED")
            print(
                "############################################################################################")
        else:
            print(f"Element {locator_type} used: {element}")
            print(f"Value Found: {value}")
            print(f"Expected value: {assert_value} not found - FAILED")


