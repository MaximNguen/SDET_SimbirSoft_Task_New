import allure
import pytest

from utils.URLStorage import URLStorage as URLS
from tests.mockData import TestData
from pages.main_page import MainPage

@allure.epic("UI Тесты")
@allure.feature("Позитивные тест-кейсы")
class TestPositiveResult:
    """Позитивные тест-кейсы для формы."""

    @classmethod
    def setup_class(cls):
        print("\n========= Начало выполнения позитивного тест-кейса ==========")

    @classmethod
    def teardown_class(cls):
        print("========= Конец выполнения позитивного тест-кейса ==========")

    @pytest.fixture(autouse=True)
    def setup(self, driver, url=URLS.main_page_url):
        self.main_page = MainPage(driver)
        self.main_page.open(url)
        yield self.main_page
        self.main_page.quit()
        
    @allure.story("Полное заполнение формы")
    @allure.title("Проверка отправки формы со всеми заполненными полями")
    @pytest.mark.parametrize("test_data", TestData.positive_full_form_data)
    def test_fill_form_full(self, test_data):
        allure.dynamic.description(
            f"""
            Тест проверяет отправку формы с заполнением всех полей.
            Данные теста:
            - Имя: {test_data['name']}
            - Пароль: {test_data['password']}
            - Напитки: {test_data['drinks']}
            - Цвет: {test_data['color']}
            - Выбор: {test_data['automation']}
            - Email: {test_data['email']}
            """
        )
        
        self.main_page.enter_name(test_data['name'])
        self.main_page.fill_password(test_data['password'])
        self.main_page.checkbox_list_clicks(test_data['drinks'])
        self.main_page.radiobox_list_clicks()
        self.main_page.select_choose(test_data['automation'])
        self.main_page.email_send(test_data['email'])
        self.main_page.send_longest()
        self.main_page.submit_click()
        
        with allure.step("Достоверимся, что Alert выпал после отправки формы"):
            assert self.main_page.check_alert(), "Alert не выпал после нажатия Submit"
            assert self.main_page.check_text_alert() == test_data['expected_alert'], "Alert не появился после отправки формы"