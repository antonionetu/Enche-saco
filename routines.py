from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from utils import write_message, confirm_message


def go_to_core_group(driver):
    core_group = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="Save things"]'))
    )
    core_group.click()

    sleep(3)


def find_contact(driver, number):
    go_to_core_group(driver)

    number = f"Wa.me/{number}"

    input_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Type a message"]'))
    )
    input_label.click()

    sleep(1)
    
    write_message(input_label, number)
    confirm_message(driver)

    sleep(3)


def send_message(driver, number, message):
    span_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f'a[title="http://Wa.me/{number}"]'))
    )
    span_element.click()

    sleep(3)

    input_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Type a message"]'))
    )

    sleep(1)

    write_message(input_label, message)
    confirm_message(driver)

    sleep(1)
