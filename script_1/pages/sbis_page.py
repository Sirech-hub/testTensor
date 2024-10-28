from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def open(self):
        self.driver.get(self.base_url)

    def click_contacts_button(self):
        contacts_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]'))
        )
        contacts_button.click()

    def click_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]'))
        )
        link.click()

    def click_banner(self):
        banner = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img'))
        )
        banner.click()
