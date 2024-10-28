import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Путь к веб-драйверу
driver_path = r'C:\webdriver\chromedriver.exe'

# Указываем путь для сохранения загружаемого файла
download_dir = r"C:\Users\Larkov\PycharmProjects\Project\donload"
downloaded_file_name = "sbisplugin-setup-web.exe"
expected_file_size_mb = 11.482635498046875
expected_file_size_bytes = expected_file_size_mb * 1024 * 1024

# Создаем директорию, если она не существует
os.makedirs(download_dir, exist_ok=True)

# Настройки Chrome для автоматического сохранения загружаемых файлов
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
})

# Инициализация драйвера с заданными опциями
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 1. Переход на сайт https://sbis.ru/
driver.get("https://sbis.ru/")

# 2. Клик на кнопку "Скачать локальные версии"
time.sleep(3)
download_button = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a')
download_button.click()

# 3. Клик на кнопку "Скачать (Exe 11.48 МБ)"
time.sleep(3)
download_link = driver.find_element(By.LINK_TEXT, "Скачать (Exe 11.48 МБ)")
download_link.click()

# 4. Ожидание загрузки файла
downloaded_file_path = os.path.join(download_dir, downloaded_file_name)

# Проверка, что файл загружен
print("Ожидание завершения загрузки файла...")
while not os.path.exists(downloaded_file_path):
    time.sleep(1)

print("Файл успешно скачан:", downloaded_file_path)

# 5. Проверка размера файла
actual_file_size = os.path.getsize(downloaded_file_path)
if abs(actual_file_size - expected_file_size_bytes) < 1024:
    print("Размер файла корректный:", actual_file_size / (1024 * 1024), "МБ")
else:
    print("Ошибка: размер файла некорректный. Ожидался:", expected_file_size_mb, "МБ, получено:", actual_file_size / (1024 * 1024), "МБ")

driver.quit()

# If you got here. you managed to run this file. may the force be with you Jedi