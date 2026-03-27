from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:
    """Класс для хранения методов ожидания у selenium"""
    
    def __init__(self, driver):
        self.driver = driver

    def wait_for_presence(self, element):
        """Метод для ожидания наличия элемента на странице."""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(element)
        )

    def wait_for_clickable(self, element):
        """Метод для ожидания кликабельности элемента на странице."""
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(element)
        )