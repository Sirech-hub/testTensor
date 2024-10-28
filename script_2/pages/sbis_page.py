from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_homepage(self):
        self.driver.get('https://sbis.ru/')

    def click_contacts(self):
        contacts_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]'))
        )
        contacts_button.click()

    def click_new_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]'))
        )
        button.click()

    def check_region_displayed(self, region_name):
        region_element = self.driver.find_element(By.XPATH, f'//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link" and text()="{region_name}"]')
        return region_element.is_displayed()

    def check_partners_displayed(self):
        partners = [
            '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div',
            '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[3]/div',
            '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[5]/div',
        ]
        return all(self.driver.find_element(By.XPATH, partner).is_displayed() for partner in partners)

    def select_region(self, region_xpath):
        region_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, region_xpath))
        )
        region_button.click()

    def check_url_contains(self, substring):
        return substring in self.driver.current_url

    def check_meta_content(self, content):
        meta_tag = self.driver.find_element(By.XPATH, '/html/head/meta[16]')
        return content in meta_tag.get_attribute("content")

    def check_partner_in_list(self, partner_name):
        partner_element = self.driver.find_element(By.XPATH, f'//div[@title="{partner_name}" and @class="sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32"]')
        return partner_name in partner_element.text
