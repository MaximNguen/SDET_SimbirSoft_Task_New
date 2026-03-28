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
        
        name = self.main_page.get_name_input().get_attribute("value")
        password = self.main_page.get_password_input().get_attribute("value")
        email = self.main_page.get_email_input().get_attribute("value")
        message = self.main_page.get_message_input().get_attribute("value")
        
        self.main_page.submit_click()
        
        with allure.step("Проверяем, что вставленные данные совпадают с данными в форме после отправки"):
            assert name == test_data['name'], f"Имя не совпало, получили в поле - {name}"
            assert password == test_data['password'], f"Пароль не совпал, получили в поле - {password}"
            assert email == test_data['email'], f"Email не совпал, получили в поле - {email}"
            assert message == test_data['expected_text_message'], f"Текст сообщения не совпал с ожидаемым, получили в поле - {message}"
        
        alert_text = self.main_page.check_text_alert()
        with allure.step("Достоверимся, что Alert выпал после отправки формы"):
            assert alert_text == test_data['expected_alert'], f"Alert не появился после отправки формы, получили - {alert_text}"
            
    @allure.story("Ввод только требующихся полей")
    @allure.title("Проверка отправки формы со всеми требующимися полями")
    @pytest.mark.parametrize("test_data", TestData.positive_required_only_data)
    def test_fill_only_required(self, test_data):
        allure.dynamic.description(
            f"""
            Тест проверяет отправку формы с заполнением только требующихся полей.
            Данные теста:
            - Имя: {test_data['name']}
            """
        )
        
        self.main_page.enter_name(test_data['name'])
        name = self.main_page.get_name_input().get_attribute("value")
        
        self.main_page.submit_click()
        
        with allure.step("Проверяем, что вставленные данные совпадают с данными в форме после отправки"):
            assert name == test_data['name'], f"Имя не совпало, получили в поле - {name}"
            
        alert_text = self.main_page.check_text_alert()  
        with allure.step("Достоверимся, что Alert выпал после отправки формы"):
            assert alert_text == test_data['expected_alert'], f"Alert не появился после отправки формы, получили - {alert_text}"
            
    @allure.story("Неполный ввод полей, в том числе имени")
    @allure.title("Проверка отправки формы с частично заполненными полями")
    @pytest.mark.parametrize("test_data", TestData.positive_partial_form_data)
    def test_fill_form_partial(self, test_data):
        allure.dynamic.description(
            f"""
            Тест проверяет отправку формы с заполнением некоторых полей.
            Данные теста:
            - Имя: {test_data['name']}
            """
        )
        
        self.main_page.enter_name(test_data['name'])
        self.main_page.send_longest()
        
        name = self.main_page.get_name_input().get_attribute("value")
        message = self.main_page.get_message_input().get_attribute("value")
        
        self.main_page.submit_click()
        
        with allure.step("Проверяем, что вставленные данные совпадают с данными в форме после отправки"):
            assert name == test_data['name'], f"Имя не совпало, получили в поле - {name}"
            assert message == test_data['expected_text_message'], f"Текст сообщения не совпал с ожидаемым, получили в поле - {message}"
            
        with allure.step("Достоверимся, что Alert выпал после отправки формы"):
            alert_text = self.main_page.check_text_alert()
            assert alert_text == test_data['expected_alert'], f"Alert не появился после отправки формы, получили - {alert_text}"