from Pragma.Functions import *

#URL
URL = 'https://www.pragmaworld.net/'
openURL(URL)

#############################################
#Click On Element
click_on_element("//button[@data-cky-tag='accept-button']", By.XPATH)

#############################################
#Click on Dropdown
name_of_list = "Leadership"

hover_click("/html/body/header/div[2]/nav/div/div[1]/ul[1]/li[1]/a", By.XPATH, f"(//li[normalize-space()='{name_of_list}'])[1]", By.XPATH)

#############################################
#Hover to enable click
hover("(//a[normalize-space()='More about the CEO'])[1]", By.XPATH)
#Click On Element
click_on_element("(//a[normalize-space()='More about the CEO'])[1]", By.XPATH)

#############################################
#Validate Text
assert_value = "Visionary leadership"

validate_text_value("(//div[@class='post-date'])[1]", By.XPATH, assert_value)

