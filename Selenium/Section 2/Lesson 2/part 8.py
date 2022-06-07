from selenium import webdriver
import time
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element_by_name("firstname").send_keys("12313")
    browser.find_element_by_name("lastname").send_keys("12313")
    browser.find_element_by_name("email").send_keys("12313")

    file_input = browser.find_element_by_name("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')  # добавляем к этому пути имя файла
    file_input.send_keys(file_path)

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
