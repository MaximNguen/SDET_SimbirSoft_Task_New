from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

from pages.factory_pages.page_factory import PageFactory

@pytest.fixture(scope="function")
def driver():
    """Фикстуа для создания драйвера с параметрами"""
    options = Options
    
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    
    yield driver
    
    driver.quit()
    
@pytest.fixture
def page_factory(driver):
    """Фикстура для фабрики страниц."""
    return PageFactory(driver)

@pytest.fixture
def main_page(page_factory):
    """Фикстура для главной страницы."""
    return page_factory.get_main_page()

@pytest.fixture
def fresh_main_page(page_factory):
    """Фикстура для новой (сброшенной) главной страницы."""
    page_factory.reset()
    return page_factory.get_main_page()