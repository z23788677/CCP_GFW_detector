import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

def screenshooter(URL):
    if type(URL) != str:
        return "URL ERROR"

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')

    driver = webdriver.Firefox(
        executable_path=GeckoDriverManager().install(),
        options=firefox_options
    )

    driver.get(URL)

    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, 0);")

    page_width = driver.execute_script("return document.body.scrollWidth")
    page_height = driver.execute_script("return document.body.scrollHeight")

    driver.set_window_size(page_width, page_height)

    driver.save_screenshot('screenshot.png')

    driver.quit()
    try:
        os.remove("geckodriver.log")
    except:
        pass