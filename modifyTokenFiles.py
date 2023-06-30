from CreateService import gmailServiceCreate
import selenium

#https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08

def replaceTokenFiles():
    driver = webdriver.Chrome()
    service = gmailServiceCreate()
    #driver.get(authentification website)
    