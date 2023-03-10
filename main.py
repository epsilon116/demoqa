from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_elements_button(self):
        elements_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
        elements_button.click()

    def click_check_box(self):
        check_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Check Box']")))
        check_box.click()

    def expand_home_directory(self):
        home_directory = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Home']")))
        home_directory.click()

    def expand_downloads_directory(self):
        downloads_directory = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Downloads']")))
        downloads_directory.click()

    def select_word_file_checkbox(self):
        word_file_checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Word File.doc']/preceding-sibling::span")))
        word_file_checkbox.click()


# создание экземпляра браузера и открытие страницы
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demoqa.com/")

# создание экземпляра страницы Elements
elements_page = ElementsPage(driver)

# нажатие кнопки Elements и переход к странице Check Box
elements_page.click_elements_button()
elements_page.click_check_box()

# выбор каталогов Home и Downloads и выбор Word File.doc
elements_page.expand_home_directory()
elements_page.expand_downloads_directory()
elements_page.select_word_file_checkbox()

# закрытие браузера
driver.quit()