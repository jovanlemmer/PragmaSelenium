from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


#Open Browser & Website
driver = WebDriver = webdriver.Chrome(executable_path='C:\\Users\iPay\AppData\Local\Programs\Python\Python37-32\Scripts\chromedriver.exe')
driver.get('https://www.pragmaworld.net/')
driver.maximize_window()

#Click On Accept All
#driver.find_element(by=By.XPATH, value="//button[@data-cky-tag='accept-button']")

btn_element = "//button[@data-cky-tag='accept-button']"
btn_locator_type = By.XPATH

ClickButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((btn_locator_type, btn_element)))

ClickButton.click()



#Hover
hover_element = "/html/body/header/div[2]/nav/div/div[1]/ul[1]/li[1]/a"
hover_locator_type = By.XPATH
# Locate the element to hover over and select
hover_on_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((hover_locator_type, hover_element)))
# Create an ActionChains object
actions = ActionChains(driver)
# Hover over the element
actions.move_to_element(hover_on_element)
# Perform the hover action
actions.perform()


#Click on Dropdown
name_of_list = "Leadership"
drp_element = f"(//li[normalize-space()='{name_of_list}'])[1]"
drp_locator_type = By.XPATH

# Now, locate the element to select (which becames visible after hovering)
ElementInDropdownList = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((drp_locator_type, drp_element)))

ElementInDropdownList.click()




#Validate Text
element = "(//h3[normalize-space()='Visionary leadership'])[1]"
locator_type = By.XPATH
assert_value = "Visionary leadership"

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


