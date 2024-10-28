import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.sbis_page import SbisPage

driver_path = r'C:\webdriver\chromedriver.exe'
service = Service(executable_path=driver_path)


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.feature('Тестирование сайта SBIS')
def test_sbis(setup):
    page = SbisPage(setup)

    page.go_to_homepage()
    page.click_contacts()
    page.click_new_button()

    assert page.check_region_displayed("Костромская обл."), "Регион 'Костромская обл.' не найден."
    assert page.check_partners_displayed(), "Список партнёров не отображается!"

    page.select_region('//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    page.select_region('//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')

    assert page.check_url_contains("41-kamchatskij-kraj"), "URL не включает '41-kamchatskij-kraj'."
    assert page.check_meta_content(
        "СБИС Контакты — Камчатский край"), "Title не включает 'СБИС Контакты — Камчатский край'."
    assert page.check_region_displayed("Камчатский край"), "Кнопка не включает 'Камчатский край'."
    assert page.check_partner_in_list("СБИС - Камчатка"), "Список партнёров не содержит 'СБИС - Камчатка'."
