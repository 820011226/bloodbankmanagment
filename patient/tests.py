from django.test import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import secret

def patient_login():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/patient/patientlogin")  # Replace with the actual login page URL
    driver.maximize_window()
    assert "Blood Bank Management System" in driver.title  # Replace with the expected title of the login page
    
    email_field = driver.find_element(By.ID, "id_username")  # Replace with the correct ID for the email field
    password_field = driver.find_element(By.ID, "id_password")  # Replace with the correct ID for the password field
    login_btn = driver.find_element(By.NAME, "LOGIN")  # Replace with the correct name of the login button
    
    email_field.clear()
    email_field.send_keys(secret.email)  # Replace with the actual patient email
    password_field.clear()
    password_field.send_keys(secret.password)  # Replace with the actual patient password
    login_btn.click()

    # This is just to wait in order to interact with the logged-in patient page
    driver.implicitly_wait(10)
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'no element')
    except NoSuchElementException:
        print('Exiting...')
    
    driver.close()

if __name__ == '__main__':
    patient_login()

# Create your tests here.
