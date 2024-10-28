from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Путь
driver_path = r'C:\webdriver\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

try:
    # 1. Перейти на сайт https://sbis.ru/
    driver.get('https://sbis.ru/')
    time.sleep(3)

    # 2. Кликнуть на раздел "Контакты"
    contacts_button = driver.find_element(By.XPATH,
                                          '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]')
    contacts_button.click()
    time.sleep(2)

    # 3. Кликнуть на кнопку с новым XPath
    button = driver.find_element(By.XPATH,
                                 '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]')
    button.click()
    time.sleep(2)

    # 4. Проверить, что регион "Костромская обл." отображается
    region_element = driver.find_element(By.XPATH,
                                         '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link" and text()="Костромская обл."]')
    if region_element.is_displayed():
        print("Регион 'Костромская обл.' успешно найден!")
    else:
        print("Регион 'Костромская обл.' не найден.")

    # 5. Проверить наличие "списка партнёров"
    partner_list_1 = driver.find_element(By.XPATH,
                                         '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div')
    partner_list_2 = driver.find_element(By.XPATH,
                                         '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[3]/div')
    partner_list_3 = driver.find_element(By.XPATH,
                                         '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[5]/div')

    if partner_list_1.is_displayed() and partner_list_2.is_displayed() and partner_list_3.is_displayed():
        print("Список партнёров отображается!")
    else:
        print("Список партнёров не отображается.")

    # 6. Кликнуть на кнопку "Костромская область"
    kostroma_button = driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    kostroma_button.click()
    time.sleep(2)

    # 7. Кликнуть на кнопку "Камчатский регион"
    kamchatka_button = driver.find_element(By.XPATH,
                                           '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')
    kamchatka_button.click()
    time.sleep(2)

    # 8. Проверить, что URL включает "41-kamchatskij-kraj"
    current_url = driver.current_url
    if "41-kamchatskij-kraj" in current_url:
        print("URL включает '41-kamchatskij-kraj'.")
    else:
        print("URL не включает '41-kamchatskij-kraj'.")

    # 9. Проверить, что тег /html/head/meta[16] включает "СБИС Контакты — Камчатский край"
    meta_tag = driver.find_element(By.XPATH, '/html/head/meta[16]')
    meta_content = meta_tag.get_attribute("content")
    if "СБИС Контакты — Камчатский край" in meta_content:
        print("Title включает 'СБИС Контакты — Камчатский край'.")
    else:
        print("Title не включает 'СБИС Контакты — Камчатский край'.")

    # 10. Проверить, что кнопка включает "Камчатский край"
    region_button = driver.find_element(By.XPATH,
                                        '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link" and text()="Камчатский край"]')
    if region_button.is_displayed():
        print("Кнопка включает 'Камчатский край'.")
    else:
        print("Кнопка не включает 'Камчатский край'.")

    # 11. Проверить, что "список партнёров" содержит "СБИС - Камчатка"
    sbis_kamchatka = driver.find_element(By.XPATH,
                                         '//div[@title="СБИС - Камчатка" and @class="sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32"]')
    if "СБИС - Камчатка" in sbis_kamchatka.text:
        print("Список партнёров содержит 'СБИС - Камчатка'.")
    else:
        print("Список партнёров не содержит 'СБИС - Камчатка'.")

    # Подождать, чтобы увидеть результат (например, 5 секунд)
    time.sleep(5)

finally:
    driver.quit()
