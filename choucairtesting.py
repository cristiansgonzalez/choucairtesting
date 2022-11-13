from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import secrets
import string

def pwd(pwd_length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    print(pwd)
    return pwd

def configuration_browser(page):
    #Configuracion e ingreso a la pagina por medio de google chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(page)
    print(f"\n\nIngreso a la pagina {page} correctamente")
    time.sleep(2)
    return browser

def join_today(browser):
    print("Ingreso a Join Today")
    browser.find_element(By.XPATH,
                         '/html/body/ui-view/unauthenticated-container/div/div/unauthenticated-header/div/div[3]/ul[2]/li[2]/a')\
        .click()
    time.sleep(2)
        
def step_1(browser, first_name, last_name, email_address, dia, mes, año):

    browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys(first_name)
    print(f"Escribe el nombre: {first_name}")
    browser.find_element(By.XPATH, '//*[@id="lastName"]').send_keys(last_name)
    print(f"Escribe el apellido: {last_name}")
    browser.find_element(By.XPATH, '//*[@id="email"]').send_keys(email_address)
    print(f"Escribe el correo electronico: {email_address}")
    Select(browser.find_element(By.ID, 'birthMonth')).select_by_value("number:" + str(mes))
    print(f"Escribe el mes de nacimiento: {mes}")
    Select(browser.find_element(By.ID, 'birthDay')).select_by_value("number:" + str(dia))
    print(f"Escribe el dia de nacimiento: {dia}")
    Select(browser.find_element(By.ID, 'birthYear')).select_by_value("number:" + str(año))
    print(f"Escribe el año de nacimiento: {año}")

    time.sleep(1)
    browser.find_element(By.XPATH,
                         '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/a')\
        .click()

def step_2(browser, city, state, postal_code, country):
    
    time.sleep(1)
    select_city = browser.find_element(By.XPATH, '//*[@id="city"]')
    select_city.clear()
    select_city.send_keys(f"{city} {state}")
    time.sleep(1)
    select_city.send_keys(Keys.DOWN + Keys.ENTER)
    print(f"Escribe la ciudad y el departamento o estado: {city} {state}")

    time.sleep(0.5)
    browser.find_element(By.XPATH, '//*[@id="zip"]').clear()
    browser.find_element(By.XPATH, '//*[@id="zip"]').send_keys(postal_code)
    print(f"Escribe el código postal: {postal_code}")
    
    browser.find_element(By.XPATH,
                         '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[1]/div[4]/div[2]/div/div/div[1]/span/span[2]')\
        .click()
    browser.find_element(By.XPATH,
                             '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[1]/div[4]/div[2]/div/div/input[1]')\
            .send_keys(country + Keys.ENTER)
    print(f"Escribe el pais: {country}")
    time.sleep(1)
    
    browser.find_element(By.XPATH,
                         '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/div/a')\
        .click()

def step_3(browser, computer, version, languague, mobile, modelo, op_sys):
    browser.find_element(By.XPATH,
                         '//*[@id="web-device"]/div[1]/div[2]/div/div[1]/span')\
        .click()
    browser.find_element(By.XPATH,
                         '//*[@id="web-device"]/div[1]/div[2]/div/input[1]')\
        .send_keys(computer + Keys.ENTER)
    print(f"Escribe el sistema operativo: {computer}")
    time.sleep(1)

    browser.find_element(By.XPATH,
                         '//*[@id="web-device"]/div[2]/div[2]/div/div[1]/span')\
        .click()
    browser.find_element(By.XPATH,
                         '//*[@id="web-device"]/div[2]/div[2]/div/input[1]')\
        .send_keys(version + Keys.ENTER)
    print(f"Escribe la version de {computer}: {version}")
    time.sleep(1)

    browser.find_element(By.XPATH,
                         '//*[@id="web-device"]/div[3]/div[2]/div/div[1]/span')\
        .click()
    browser.find_element(By.XPATH,
                         '//*[@id="web-device"]/div[3]/div[2]/div/input[1]')\
        .send_keys(languague + Keys.ENTER)
    print(f"Escribe Lenguaje del sistema operativo: {languague}")
    time.sleep(1)

    browser.find_element(By.XPATH,
                         '//*[@id="mobile-device"]/div[1]/div[2]/div/div[1]/span')\
        .click()
    browser.find_element(By.XPATH,
                         '//*[@id="mobile-device"]/div[1]/div[2]/div/input[1]')\
        .send_keys(mobile + Keys.ENTER)
    print(f"Escribe la marca del celular: {mobile}")
    time.sleep(1)

    browser.find_element(By.XPATH,
                         '//*[@id="mobile-device"]/div[2]/div[2]/div/div[1]/span')\
        .click()
    browser.find_element(By.XPATH,
                         '//*[@id="mobile-device"]/div[2]/div[2]/div/input[1]')\
        .send_keys(modelo + Keys.ENTER)
    print(f"Escribe el model del celular: {modelo}")
    time.sleep(1)

    browser.find_element(By.XPATH,
                         '//*[@id="mobile-device"]/div[3]/div[2]/div/div[1]/span')\
        .click()
    browser.find_element(By.XPATH,
                         '//*[@id="mobile-device"]/div[3]/div[2]/div/input[1]')\
        .send_keys(op_sys + Keys.ENTER)
    print(f"Escribe el sistema operativo del celular: {op_sys}")
    time.sleep(1)

    browser.find_element(By.XPATH,
                         '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/div[2]/div/a')\
        .click()    

def step_4(browser, pwd):
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(pwd)
    print(f"Escribe contraseña: \n{pwd}")
    browser.find_element(By.XPATH, '//*[@id="confirmPassword"]').send_keys(pwd)
    print(f"Escribe la confimacion de la contraseña: \n{pwd}")
    browser.find_element(By.XPATH,
                         '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[4]/label/span')\
                         .click()
    print("✅ STAY INFORMED! ")
    browser.find_element(By.XPATH,
                         '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[5]/label/span[1]')\
                         .click()
    print("✅ Terminos de uso")
    browser.find_element(By.XPATH,
                         '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[6]/label/span[1]')\
                         .click()
    print("✅ Privacidad")

#Inicializacion de variables
pagina = "https://utest.com/"

# Variables step 1
first_name = "Cristian"
last_name = "Gonzalez"
email_address = "alt.yi-3opk4lex@yopmail.com"
dia = 13
mes = 6
año = 1991

# Variables step 2
city = "Ibague"
state = "Tolima"
postal_code = 730001
country = "Colombia"

# Variables step 3
computer = "Windows"
version = "Windows 10"
languague = "Spanish"
mobile = "Apple"
modelo = "iPhone 14 Pro Max"
op_sys = "iOS 16.1 Beta"

# Variables step 4
pwd_length = 60
pwd = pwd(pwd_length)


browser = configuration_browser(pagina)

join_today(browser)

print("\n step 1\n")
step_1(browser, first_name, last_name, email_address, dia, mes, año)

print("\n step 2\n")
step_2(browser, city, state, postal_code, country)

print("\n step 3\n")
step_3(browser, computer, version, languague, mobile, modelo, op_sys)

print("\n step 4\n")
step_4(browser, pwd)

