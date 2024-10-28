from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Путь к веб-драйверу
driver_path = r'C:\webdriver\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

try:
    # 1. Перейти на сайт sbis.ru
    driver.get("https://sbis.ru/")

    # 2. Кликнуть на кнопку контакты
    contacts_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]'))
    )
    contacts_button.click()

    # 3. Кликнуть на ссылку
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]'))
    )
    link.click()

    # 4. Кликнуть на баннер
    banner = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img'))
    )
    banner.click()

    # Закрыть вкладку с баннером
    driver.close()

    # Переключиться обратно на основную вкладку, если открылась новая
    driver.switch_to.window(driver.window_handles[0])

    # 5. Перейти на tensor.ru
    driver.get("https://tensor.ru/")

    # 6. Проверить наличие элемента
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]'))
        )

        # 7. Нажать кнопку подробнее
        more_button = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
        more_button.click()

        # 8. Убедиться, что открывается нужный URL
        WebDriverWait(driver, 10).until(EC.url_to_be("https://tensor.ru/about"))
        print("Тест пройден успешно: открыта страница 'О компании'.")

        # 9. Проверить размеры 4 блоков
        block1 = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]')
        block2 = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]')
        block3 = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]')
        block4 = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]')

        size1 = block1.size
        size2 = block2.size
        size3 = block3.size
        size4 = block4.size

        if size1 == size2 == size3 == size4:
            print("Все 4 блока имеют одинаковые размеры.")
        else:
            print("Размеры блоков различаются.")

    except Exception as e:
        print("Элемент не найден, тест завершен.")
        print(f"Ошибка: {e}")

finally:
    driver.quit()
