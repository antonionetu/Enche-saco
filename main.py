from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import wait_whatsapp_work
from routines import find_contact, send_message

READY = False

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")

wait_whatsapp_work(driver, READY)

number_list = ["5579988105028", "5561992964304", "5579991538795"]

for number in number_list:
    find_contact(driver, number)
    send_message(driver, number, "https://www.youtube.com/watch?v=tA8tvhez9Mc")
