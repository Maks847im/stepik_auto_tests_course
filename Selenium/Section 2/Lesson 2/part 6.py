from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
    browser.get("http://SunInJuly.github.io/execute_script.html")
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_id("robotCheckbox").click()

    robotsRule = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()


    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
