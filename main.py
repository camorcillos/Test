from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
import re

class WebScraper:

    def scrapeEmailAddresses(self, driver, pageUrl):
        driver.get(pageUrl)
        driver.implicitly_wait(10)  # Espera un máximo de 10 segundos para que los elementos se carguen
        elements = driver.find_elements(By.XPATH, '//*')

        emails = []
        for element in elements:
            email_text = element.text
            email = re.search(r'[\w\.-]+@[\w\.-]+', email_text)
            if email:
                emails.append(email.group())

        unique_emails = list(set(emails))
        return unique_emails

    def scrapeMobileNumbers(self, driver, pageUrl):
        driver.get(pageUrl)
        driver.implicitly_wait(10)  # Espera un máximo de 10 segundos para que los elementos se carguen
        elements = driver.find_elements(By.XPATH, '//*')

        numbers = []
        for element in elements:
            number_text = element.text
            number = re.search(r'\b\d{10}\b', number_text)
            if number:
                numbers.append(number.group())

        unique_numbers = list(set(numbers))
        return unique_numbers

    # do not modify
    def get(self, url, driver):
        driver.get(url)
        return driver.page_source

chromeOptions = Options()
args = ['--window-size=1920,1080','--headless', '--disable-gpu', '--log-level=3', '--disable-features=ChromeWhatsNewUI', '--no-sandbox', '--disable-crash-reporter', '--disable-extensions', '--disable-in-process-stack-traces', '--disable-logging', '--disable-dev-shm-usage']      
[chromeOptions.add_argument(arg) for arg in args]
chromedriver_autoinstaller.install()  
driver = webdriver.Chrome(options=chromeOptions)  
execute = WebScraper()
emails = execute.scrapeEmailAddresses(driver, "http://127.0.0.1:5000")
numbers = execute.scrapeMobileNumbers(driver, "http://127.0.0.1:5000")

print(emails)
print(numbers)
