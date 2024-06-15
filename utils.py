from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def wait_whatsapp_work(driver, READY):
    times = 0

    while not READY:
        try: 
            span_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="Save things"]'))
            )
            READY = True
        except:
            print(f"{times} - Not Ready Yet...")
    
        times += 1
        sleep(3)


def write_message(label, message):
    for l in message:
        label.send_keys(l)
        sleep(0.01)
    sleep(3)

    
def confirm_message(driver):
    send_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Send"]'))
    )
    send_button.click()
