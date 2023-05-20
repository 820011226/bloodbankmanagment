from django.test import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import secret

def donate_blood():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/bloodbank/donate")  # Replace with the actual blood donation page URL
    driver.maximize_window()
    assert "Blood Bank Management System" in driver.title  # Replace with the expected title of the blood donation page
    
    # Fill in the blood donation form
    full_name_field = driver.find_element(By.ID, "id_full_name")  # Replace with the correct ID for the full name field
    blood_group_field = driver.find_element(By.ID, "id_blood_group")  # Replace with the correct ID for the blood group field
    donation_date_field = driver.find_element(By.ID, "id_donation_date")  # Replace with the correct ID for the donation date field
    donation_time_field = driver.find_element(By.ID, "id_donation_time")  # Replace with the correct ID for the donation time field
    donate_btn = driver.find_element(By.NAME, "donate")  # Replace with the correct name of the donate button
    
    full_name_field.clear()
    full_name_field.send_keys(secret.full_name)  # Replace with the actual donor's full name
    blood_group_field.clear()
    blood_group_field.send_keys(secret.blood_group)  # Replace with the actual donor's blood group
    donation_date_field.clear()
    donation_date_field.send_keys(secret.donation_date)  # Replace with the actual donation date
    donation_time_field.clear()
    donation_time_field.send_keys(secret.donation_time)  # Replace with the actual donation time
    donate_btn.click()

    # This is just to wait in order to interact with the confirmation page or perform additional assertions
    driver.implicitly_wait(10)
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'no element')
    except NoSuchElementException:
        print('Exiting...')
    
    driver.close()

if __name__ == '__main__':
    donate_blood()

# Create your tests here.
