import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage


@pytest.fixture
def driver():
    driver_path = r'C:\webdriver\chromedriver.exe'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.feature('Тестирование SBIS и Tensor сайтов')
@allure.story('SBIS Page Test')
def test_sbis_page(driver):
    sbis_page = SbisPage(driver)

    with allure.step('Открыть сайт sbis.ru'):
        sbis_page.open()

    with allure.step('Кликнуть на кнопку "Контакты"'):
        sbis_page.click_contacts_button()

    with allure.step('Кликнуть на ссылку'):
        sbis_page.click_link()

    with allure.step('Кликнуть на баннер'):
        sbis_page.click_banner()


    driver.close()
    driver.switch_to.window(driver.window_handles[0])


@allure.story('Tensor Page Test')
def test_tensor_page(driver):
    tensor_page = TensorPage(driver)

    with allure.step('Открыть сайт tensor.ru'):
        tensor_page.open()

    with allure.step('Проверить наличие основного элемента'):
        tensor_page.verify_main_element_present()

    with allure.step('Нажать кнопку "Подробнее"'):
        tensor_page.click_more_button()

    with allure.step('Проверить, что открыта страница "О компании"'):
        tensor_page.verify_about_page_url()

    with allure.step('Проверить размеры блоков'):
        assert tensor_page.verify_block_sizes(), "Размеры блоков различаются"
