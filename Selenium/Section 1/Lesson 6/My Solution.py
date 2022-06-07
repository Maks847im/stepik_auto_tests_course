from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    #browser.get(" http://suninjuly.github.io/registration1.html")
    browser.get(" http://suninjuly.github.io/registration2.html")
    browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("First name")
    browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Last name")
    browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("Email")
    browser.find_element(By.CSS_SELECTOR, ".second_block input.first").send_keys("Phone")
    browser.find_element(By.CSS_SELECTOR, ".second_block input.second").send_keys("Address")

    browser.find_element_by_xpath('//button[text()="Submit"]').click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()

