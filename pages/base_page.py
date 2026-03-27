class BasePage:
    """
    Базовая страница для всех страниц приложения.
    Содержит общие методы для взаимодействия
    с элементами страницы.
    """
    
    def __init__(self, driver):
        """Инициализация драйвера."""
        self.driver = driver
        
    def find_element(self, *locator):
        """Поиск элемента на странице по локатору."""
        return self.driver.find_element(*locator)
    
    def click(self, *locator):
        """Клик по элементу, найденному по локатору."""
        self.find_element(*locator).click()
        
    def find_elements(self, *locator):
        """Поиск всех элементов на странице по локатору."""
        return self.driver.find_elements(*locator)