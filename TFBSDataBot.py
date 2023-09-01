import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the webdriver
driver = webdriver.Chrome()

# URL of the website to automate
url = 'https://www.prodoric.de/vfp/'

# Open the website
driver.get(url)

def pasteStuff():
    # Find the 'li' element corresponding to the "Paste" option and click it
    paste_option = driver.find_element(By.XPATH, '//li[@name="Paste"]')
    paste_option.click()
    time.sleep(3)

    # Find the textarea by its ID and set the value
    sequence = '>MTK2_006\naacgattacgccaagctggccggcccgtacggccacgcggatctcgacattgattattgactagtctgtggaatgtgtgtcagttagggtgtggaaagtccccaggctccccagcaggcagaagtatgcaaagcatgcatctcaattagtcagcaaccaggtgtggaaagtccccaggctccccagcaggcagaagtatgcaaagcatgcatctcaattagtcagcaaccatagtcccgcccctaactccgcccatcccgcccctaactccgcccagttccgcccattctccgccccatggctgactaattttttttatttatgcagaggccgaggccgcctctgcctctgagctattccagaagtagtgaggaggcttttttggaggcctaggcttttgcaaaaagctcccgggagcttgtatatccagccac'

    textarea = driver.find_element(By.ID, 'input_fasta')
    textarea.clear()
    textarea.send_keys(sequence)
    time.sleep(3)

# Find the dropdown input and click it
dropdown_input = driver.find_element(By.CSS_SELECTOR, '#matrix-panel .dropdown-input')
dropdown_input.click()
time.sleep(1)


# Find all dropdown options and iterate through them
dropdown_options = driver.find_elements(By.CSS_SELECTOR, '#matrix-panel ul.dropdown li')
count = 0
needed =["MX000003", "MX000004", "MX000008", "MX000028", "MX000029", "MX000031", "MX000040", "MX000091", "MX000092", "MX000093", "MX000094", "MX000095", "MX000096", "MX000097", "MX000098", "MX000099", "MX000100", "MX000114", "MX000115", "MX000116", "MX000118", "MX000119", "MX000121", "MX000123", "MX000124", "MX000125", "MX000126", "MX000127", "MX000128", "MX000129", "MX000130", "MX000131", "MX000132", "MX000133", "MX000134", "MX000135", "MX000136", "MX000137", "MX000138", "MX000139", "MX000140", "MX000141", "MX000143", "MX000144", "MX000145", "MX000148", "MX000149", "MX000150", "MX000151", "MX000152", "MX000154", "MX000156", "MX000157", "MX000158", "MX000160", "MX000165", "MX000169", "MX000170", "MX000171", "MX000172", "MX000173", "MX000174", "MX000175", "MX000177", "MX000178", "MX000179", "MX000180", "MX000182", "MX000183", "MX000184", "MX000185", "MX000187", "MX000200", "MX000201", "MX000202", "MX000204", "MX000218", "MX000220", "MX000223", "MX000224", "MX000235", "MX000236", "MX000237", "MX000238", "MX000239", "MX000266", "MX000319", "MX000392", "MX000395", "MX000396", "MX000398", "MX000399", "MX000400", "MX000410", "MX000411", "MX000412"]
print([i.text for i in dropdown_options])
import re
try:
    for option in needed:
    # Click the option to select it
        pasteStuff()
        dropdown_input = driver.find_element(By.CSS_SELECTOR, '#matrix-panel .dropdown-input')
        dropdown_input.click()
        time.sleep(1)
        optionsss = driver.find_elements(By.CSS_SELECTOR, '#matrix-panel ul.dropdown li')
        for i in optionsss:
            if re.search(option, i.text):
                i.click()
                break
        time.sleep(2)
 
        
        time.sleep(5)
        # Find the submit button by its CSS selector and click it
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="Submit"]')
        submit_button.click()

        # Wait for the page to load (you may need to increase the sleep time if necessary)
        time.sleep(3)
        csv_button = None

        while 1==1:
            try:
                csv_button = driver.find_element(By.CSS_SELECTOR, 'div.vfpresult-buttons > div:nth-child(1) > button:nth-child(2)')
                csv_button.click()
                break
            except:
                pass
     
            
        # Perform any other actions or extract data from the page as needed
        # ...
        time.sleep(5)
        element = driver.find_element(By.CSS_SELECTOR,'a[href="/vfp/"]')
        count = count + 1
# Click the element
        element.click()
except(e):
    print(e)
# Close the webdriver
