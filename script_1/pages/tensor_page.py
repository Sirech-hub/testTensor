from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://tensor.ru/"

    def open(self):
        self.driver.get(self.base_url)

    def verify_main_element_present(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]'))
        )

    def click_more_button(self):
        more_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
        more_button.click()

    def verify_about_page_url(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://tensor.ru/about"))

    def verify_block_sizes(self):
        blocks = [
            self.driver.find_element(By.XPATH, f'//*[@id="container"]/div[1]/div/div[4]/div[2]/div[{i+1}]/a/div[1]')
            for i in range(4)
        ]
        sizes = [block.size for block in blocks]
        return all(size == sizes[0] for size in sizes)
