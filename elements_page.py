from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.elements_button_locator = (By.XPATH, "//h5[text()='Elements']")
        self.check_box_locator = (By.XPATH, "//span[text()='Check Box']")
        self.home_directory_locator = (By.CSS_SELECTOR, "#tree-node > ol > li > span > button")
        self.downloads_directory_locator = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(3) > span > button")
        self.word_file_checkbox_locator = (By.XPATH, "//span[text()='Word File.doc']/preceding-sibling::span")

    def click_elements_button(self):
        elements_button = self.wait.until(EC.element_to_be_clickable(self.elements_button_locator))
        elements_button.click()

    def click_check_box(self):
        check_box = self.wait.until(EC.element_to_be_clickable(self.check_box_locator))
        check_box.click()

    def expand_home_directory(self):
        home_directory = self.wait.until(EC.element_to_be_clickable(self.home_directory_locator))
        home_directory.click()

    def expand_downloads_directory(self):
        downloads_directory = self.wait.until(EC.element_to_be_clickable(self.downloads_directory_locator))
        downloads_directory.click()

    def select_word_file_checkbox(self):
        word_file_checkbox = self.wait.until(EC.element_to_be_clickable(self.word_file_checkbox_locator))
        word_file_checkbox.click()
