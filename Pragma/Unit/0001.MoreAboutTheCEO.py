from Pragma.Functions import *
import csv

intID = "1"
DatasheetCSV = 'C:\\Users\iPay\PycharmProjects\PragmaSelenium\Pragma\Data\AboutTheCEO.csv'

#----------------READ DATASHEET PER SET ROW NUMBER INDEX----------------#
def ReadData(row):

    SetColNumIndex = -1  # Because zero index

#----------------Control Flow Data----------------#
    global Exe
    SetColNumIndex += 1
    data=row  #Get Row
    Exe=(data[SetColNumIndex])
    if Exe != "":
        print(Exe)

    global ID
    SetColNumIndex += 1
    data=row  #Get Row
    ID=(data[SetColNumIndex])
    if ID != "":
        print(ID)

    global PreID
    SetColNumIndex += 1
    data=row  #Get Row
    PreID=(data[SetColNumIndex])
    if PreID != "":
        print(PreID)

    global URL
    SetColNumIndex += 1
    data=row  #Get Row
    URL=(data[SetColNumIndex])
    if URL != "":
        print(URL)

#Button Accept All popup
    global AcceptAll
    SetColNumIndex += 1
    data=row  #Get Row
    AcceptAll=(data[SetColNumIndex])
    if AcceptAll != "":
        print(AcceptAll)

    global element_AcceptAll
    SetColNumIndex += 1
    data=row  #Get Row
    element_AcceptAll=(data[SetColNumIndex])
    if element_AcceptAll != "":
        print(element_AcceptAll)

    global locatorType_AcceptAll
    SetColNumIndex += 1
    data=row  #Get Row
    locatorType_AcceptAll=(data[SetColNumIndex])
    if locatorType_AcceptAll != "":
        print(locatorType_AcceptAll)

#Hover over "About Us", Then click on "Leadership
    global hoverclick
    SetColNumIndex += 1
    data=row  #Get Row
    hoverclick=(data[SetColNumIndex])
    if hoverclick != "":
        print(hoverclick)

    global hoverclick_element
    SetColNumIndex += 1
    data=row  #Get Row
    hoverclick_element=(data[SetColNumIndex])
    if hoverclick_element != "":
        print(hoverclick_element)

    global hoverclick_locator_type
    SetColNumIndex += 1
    data=row  #Get Row
    hoverclick_locator_type=(data[SetColNumIndex])
    if hoverclick_locator_type != "":
        print(hoverclick_locator_type)

    global drp_element
    SetColNumIndex += 1
    data=row  #Get Row
    drp_element=(data[SetColNumIndex])
    if drp_element != "":
        print(drp_element)

    global drp_locator_type
    SetColNumIndex += 1
    data=row  #Get Row
    drp_locator_type=(data[SetColNumIndex])
    if drp_locator_type != "":
        print(drp_locator_type)

    global name_of_list
    SetColNumIndex += 1
    data=row  #Get Row
    name_of_list=(data[SetColNumIndex])
    if name_of_list != "":
        print(name_of_list)

#Hover over "More about the CEO" then Click on Button "More about the CEO"
    global hover
    SetColNumIndex += 1
    data=row  #Get Row
    hover=(data[SetColNumIndex])
    if hover != "":
        print(hover)

    global hover_element
    SetColNumIndex += 1
    data=row  #Get Row
    hover_element=(data[SetColNumIndex])
    if hover_element != "":
        print(hover_element)

    global hover_locator_type
    SetColNumIndex += 1
    data=row  #Get Row
    hover_locator_type=(data[SetColNumIndex])
    if hover_locator_type != "":
        print(hover_locator_type)

    global click
    SetColNumIndex += 1
    data=row  #Get Row
    click=(data[SetColNumIndex])
    if click != "":
        print(click)

    global element_click
    SetColNumIndex += 1
    data=row  #Get Row
    element_click=(data[SetColNumIndex])
    if element_click != "":
        print(element_click)

    global locatortype_click
    SetColNumIndex += 1
    data=row  #Get Row
    locatortype_click=(data[SetColNumIndex])
    if locatortype_click != "":
        print(locatortype_click)

#Validate Date of Article
    global validateText
    SetColNumIndex += 1
    data=row  #Get Row
    validateText=(data[SetColNumIndex])
    if validateText != "":
        print(validateText)

    global element_validateText
    SetColNumIndex += 1
    data=row  #Get Row
    element_validateText=(data[SetColNumIndex])
    if element_validateText != "":
        print(element_validateText)

    global locatortype_validateText
    SetColNumIndex += 1
    data=row  #Get Row
    locatortype_validateText=(data[SetColNumIndex])
    if locatortype_validateText != "":
        print(locatortype_validateText)

    global assert_value
    SetColNumIndex += 1
    data=row  #Get Row
    assert_value=(data[SetColNumIndex])
    if assert_value != "":
        print(assert_value)

# ----------------FRAMEWORK EXECUTION HANDLER----------------#
def Framework():
    print("Recordset action start")

    # ----------------Open URL----------------#
    if URL != "":
        openURL(URL)
        #driver.implicitly_wait(15)

    # ----------------Accept All----------------#
    if AcceptAll != "":
        click_on_element("//button[@data-cky-tag='accept-button']", By.XPATH)

    # ----------------Hover Click----------------#
    if hoverclick != "":
        hover_click("/html/body/header/div[2]/nav/div/div[1]/ul[1]/li[1]/a", By.XPATH, f"(//li[normalize-space()='{name_of_list}'])[1]", By.XPATH)

    # ----------------Hover----------------#
    if hover != "":
        #driver.implicitly_wait(15)
        hover_click("(//a[normalize-space()='More about the CEO'])[1]", By.XPATH, "(//a[normalize-space()='More about the CEO'])[1]", By.XPATH)

    # ----------------Hover----------------#
    if validateText != "":
        validate_text_value("(//div[@class='post-date'])[1]", By.XPATH, assert_value)

#----------------EXECUTION SCRIPT----------------#
print("-------- MMA LOGIN EXECUTION START --------")

SetRowNumIndex = 0

# Get PreID RowIndex Number to use to speed up lookup for ReadData function.
PreID = intID
y = PreID
with open (DatasheetCSV,'rU') as csvfile:
    next(csvfile, None) #skip header
    plotlist = csv.reader(csvfile, delimiter='\t') #\t = TAB Delimiter
    for i, row in enumerate(plotlist):
        if row[2] == y:
            print("Next Row")
            SetRowNumIndex = i
            ReadData(row)
            Framework()
            i += 1
        else:
            print("Skipped Next Row")
csvfile.close