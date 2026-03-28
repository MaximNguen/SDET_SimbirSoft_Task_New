from selenium.webdriver.remote.webdriver import WebDriver
import allure


class PageFactory:
    """
    Фабрика для создания и управления страницами.
    Реализует паттерн Factory.
    """
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._main_page = None
    
    def get_main_page(self, refresh: bool = False) -> object:
        """Получить экземпляр страницы (Так как страниц всего 1 - автоматически создаваемая)."""
        if refresh or self._main_page is None:
            with allure.step("Создаем экземпляр главной страницы"):
                from pages.main_page import MainPage
                self._main_page = MainPage(self.driver)
        
        return self._main_page
    
    def reset(self):
        """Сбросить состояние страницы (очистить кэш)."""
        with allure.step("Сбрасываем состояние страницы"):
            self._main_page = None