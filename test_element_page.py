from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from elements_page import ElementsPage

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
