from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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

    return pwd

def cliking(browser, ruta):
    browser.find_element(By.XPATH, ruta).click()
    
def sending(*args):
    '''
    args[0] = browser
    args[1] = ruta
    args[2] = dato 1 mensaje
    args[3] = ENTER
    '''
    if len(args) == 3:
        args[0].find_element(By.XPATH, args[1]).send_keys(args[2]) 
    else:
        args[0].find_element(By.XPATH, args[1]).send_keys(args[2] + args[3]) 
    
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
    
    cliking(browser, '/html/body/ui-view/unauthenticated-container/div/div/unauthenticated-header/div/div[3]/ul[2]/li[2]/a')
    print("Ingreso a Join Today")
    time.sleep(2)
        
def step_1(browser, first_name, last_name, email_address, dia, mes, año):

    sending(browser, '//*[@id="firstName"]', first_name)
    print(f"Escribe el nombre: {first_name}")
    sending(browser, '//*[@id="lastName"]', last_name)
    print(f"Escribe el apellido: {last_name}")
    sending(browser, '//*[@id="email"]', email_address)
    print(f"Escribe el correo electronico: {email_address}")
    Select(browser.find_element(By.ID, 'birthMonth')).select_by_value("number:" + str(mes))
    print(f"Escribe el mes de nacimiento: {mes}")
    Select(browser.find_element(By.ID, 'birthDay')).select_by_value("number:" + str(dia))
    print(f"Escribe el dia de nacimiento: {dia}")
    Select(browser.find_element(By.ID, 'birthYear')).select_by_value("number:" + str(año))
    print(f"Escribe el año de nacimiento: {año}")

    time.sleep(1)
    cliking(browser, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/a')

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
    sending(browser, '//*[@id="zip"]', postal_code)
    print(f"Escribe el código postal: {postal_code}")
    
    cliking(browser, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[1]/div[4]/div[2]/div/div/div[1]/span/span[2]')
    
    sending(browser,
            '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[1]/div[4]/div[2]/div/div/input[1]',
            country,
            Keys.ENTER)
    print(f"Escribe el pais: {country}")
    time.sleep(1)
    
    cliking(browser, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/div/a')
    

def step_3(browser, computer, version, languague, mobile, modelo, op_sys):
    
    cliking(browser, '//*[@id="web-device"]/div[1]/div[2]/div/div[1]/span')
    sending(browser, '//*[@id="web-device"]/div[1]/div[2]/div/input[1]', computer, Keys.ENTER)
    print(f"Escribe el sistema operativo: {computer}")
    time.sleep(1)

    cliking(browser, '//*[@id="web-device"]/div[2]/div[2]/div/div[1]/span')
    sending(browser, '//*[@id="web-device"]/div[2]/div[2]/div/input[1]', version, Keys.ENTER)
    print(f"Escribe la version de {computer}: {version}")
    time.sleep(1)

    cliking(browser, '//*[@id="web-device"]/div[3]/div[2]/div/div[1]/span')
    sending(browser, '//*[@id="web-device"]/div[3]/div[2]/div/input[1]', languague, Keys.ENTER)
    print(f"Escribe el lenguaje del sistema operativo: {languague}")
    time.sleep(1)

    cliking(browser, '//*[@id="mobile-device"]/div[1]/div[2]/div/div[1]/span')
    sending(browser, '//*[@id="mobile-device"]/div[1]/div[2]/div/input[1]', mobile, Keys.ENTER)
    print(f"Escribe la marca del celular: {mobile}")
    time.sleep(1)

    cliking(browser, '//*[@id="mobile-device"]/div[2]/div[2]/div/div[1]/span')
    sending(browser, '//*[@id="mobile-device"]/div[2]/div[2]/div/input[1]', modelo, Keys.ENTER)
    print(f"Escribe el modelo del celular: {modelo}")
    time.sleep(1)

    cliking(browser, '//*[@id="mobile-device"]/div[3]/div[2]/div/div[1]/span')
    sending(browser, '//*[@id="mobile-device"]/div[3]/div[2]/div/input[1]', op_sys, Keys.ENTER)
    print(f"Escribe el sistema operativo del celular: {op_sys}")
    time.sleep(1)

    cliking(browser, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/div[2]/div/a')
      
def step_4(browser, pwd):
    sending(browser, '//*[@id="password"]', pwd)
    print(f"Escribe contraseña: \n{pwd}")
    sending(browser, '//*[@id="confirmPassword"]', pwd)
    print(f"Escribe la confirmacion de la contraseña: \n{pwd}")
    cliking(browser, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[4]/label/span')
    print("✅ STAY INFORMED! ")
    cliking(browser, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[5]/label/span[1]')
    print("✅ Terminos de uso")
    cliking(browser, '//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[6]/label/span[1]')
    print("✅ Privacidad")
    time.sleep(1)
    cliking(browser, '//*[@id="laddaBtn"]')
    print("\n Usuario creado")

#Inicializacion de variables
pagina = "https://utest.com/"

# Variables step 1
first_name = "Cristian"
last_name = "Gonzalez"
email_address = "alt.z1-fix1snf@yopmail.com"
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

