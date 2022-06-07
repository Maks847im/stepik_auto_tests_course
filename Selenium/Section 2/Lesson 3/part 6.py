from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_xpath('//button[@type="submit"]').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_xpath('//button[@type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
