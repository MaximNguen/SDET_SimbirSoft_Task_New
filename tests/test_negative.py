import re

import allure
import pytest

from utils.URLStorage import URLStorage as URLS
from tests.mockData import TestData
from pages.main_page import MainPage

@allure.epic("UI Тесты")
@allure.feature("Негативные тест-кейсы")
class TestNegativeResult:
    """Негативные тест-кейсы для формы."""

    @classmethod
    def setup_class(cls):
        print("\n========= Начало выполнения негативного тест-кейса ==========")

    @classmethod
    def teardown_class(cls):
        print("========= Конец выполнения негативного тест-кейса ==========")

    @pytest.fixture(autouse=True)
    def setup(self, driver, url=URLS.main_page_url):
        self.main_page = MainPage(driver)
        self.main_page.open(url)
        yield self.main_page
        self.main_page.quit()
        
    @allure.story("Заполнение формы, кроме имени")
    @allure.title("Проверка отправки формы со всеми заполненными полями")
    @pytest.mark.parametrize("test_data", TestData.negative_without_name_data)
    def test_fill_form_without_name(self, test_data):
        allure.dynamic.description(
            f"""
            Тест проверяет отправку формы с заполнением всех полей, кроме имени.
            Данные теста:
            - Пароль: {test_data['password']}
            - Напитки: {test_data['drinks']}
            - Цвет: {test_data['color']}
            - Выбор: {test_data['automation']}
            - Email: {test_data['email']}
            """
        )
        
        self.main_page.fill_password(test_data['password'])
        self.main_page.checkbox_list_clicks(test_data['drinks'])
        self.main_page.radiobox_list_clicks()
        self.main_page.select_choose(test_data['automation'])
        self.main_page.email_send(test_data['email'])
        if not self._is_valid_email(test_data['email']):
            with allure.step("Тест не пройдет, так как в негативном тест кейсе обнаружен верный формат почты"):
                pytest.fail(f"Почта {test_data['email']} не выдала ошибку при вводе верного формата")
        self.main_page.send_longest()
        self.main_page.submit_click()
        
        name = self.main_page.get_name_input().get_attribute("value")
        password = self.main_page.get_password_input().get_attribute("value")
        email = self.main_page.get_email_input().get_attribute("value")
        message = self.main_page.get_message_input().get_attribute("value")
        alert_state = self.main_page.check_alert()
        
        with allure.step("Проверка, что форма не отправилась и отображается алерт"):
            assert name == "", "Поле имени должно быть пустым"
            assert password == test_data['password'], "Поле пароля должно быть заполнено"
            assert email == test_data['email'], "Поле email должно быть заполнено"
            assert message == "", "Поле сообщения должно быть пустым"
            assert alert_state == True, "Должен отображаться алерт при отправке формы без имени"
    
    @allure.story("Заполнение формы, кроме имени и некоторых полей")
    @allure.title("Проверка отправки формы со всеми заполненными полями")
    @pytest.mark.parametrize("test_data", TestData.negative_optional_only_data)
    def test_fill_form_without_name(self, test_data):
        allure.dynamic.description(
            f"""
            Тест проверяет отправку формы с заполнением всех полей.
            Данные теста:
            - Напитки: {test_data['drinks']}
            - Ожидание алерта: {test_data['expected_alert']},
            """
        )
        
        self.main_page.checkbox_list_clicks(test_data['drinks'])
        self.main_page.send_longest()
        self.main_page.submit_click()
        
        with allure.step("Проверка, что форма не отправилась и отображается алерт"):
            assert test_data['expected_alert'] == False, "Форма не должна отправляться при заполнении только необязательных полей"
            
    def _is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is None