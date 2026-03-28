import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import allure
from typing import List

from pages.base_page import BasePage
from utils.elements import MainPageLocators as MPL

class MainPage(BasePage):
    """Класс для взаимодействия с главной страницей приложения."""
    
    def __init__(self, driver):
        """Инициализация драйвера и утилит ожидания."""
        super().__init__(driver)
        
    def open(self, url: str = None) -> 'MainPage':
        """Открытие страницы по URL."""
        with allure.step(f"Открыть страницу по URL: {url}"):
            self.driver.get(url)
        return self
            
    def scroll(self, element: WebElement) -> 'MainPage':
        """Метод прокрутки до указанного элемента."""
        with allure.step(f"Прокрутить страницу до элемента: {element}"):
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self
    
    def quit(self) -> 'MainPage':
        """Метод выхода из браузера."""
        with allure.step("Закрываем браузер"):
            self.driver.quit()
        return self
            
    def get_name_input(self) -> WebElement:
        """Метод для получения элемента поля ввода имени."""
        self.wait.wait_for_presence(MPL.name_input)
        name = self.find_element(*MPL.name_input)
        self.scroll(name)
        with allure.step("Поиск поле для ввода имени"):
            return name
        
    def enter_name(self, text: str = None) -> 'MainPage':
        """Метод для ввода текста в поле имени."""
        with allure.step("Ввод текста в поле имени"):
            self.get_name_input().send_keys(text)
        return self
        
    def get_password_input(self) -> WebElement:
        """Метод для получения элемента поля ввода пароля."""
        self.wait.wait_for_presence(MPL.password_input)
        password = self.find_element(*MPL.password_input)
        self.scroll(password)
        with allure.step("Поиск поле для пароля"):
            return password

    def fill_password(self, text: str = None) -> 'MainPage':
        """Метод для ввода текста в поле пароля."""
        with allure.step("Ввод пароля"):
            self.get_password_input().send_keys(text)
        return self
        
    def checkbox_list_clicks(self, selected_checkboxes: List[str] = []) -> 'MainPage':
        """Метод для кликов по чекбоксам из списка."""
        self.wait.wait_for_presence(MPL.checkboxes)
        checkboxes = self.find_elements(*MPL.checkboxes)
        self.scroll(checkboxes[0])
        for checkbox in checkboxes:
            checkbox_id = checkbox.get_attribute("id")
            label = self.find_element(By.XPATH, f"//label[@for='{checkbox_id}']")
            label_text = label.text
            with allure.step(f"Проверяем чекбокс {checkbox.get_attribute('value')}"):
                if label_text in selected_checkboxes:
                    with allure.step(f"Выбираем чекбокс {label_text} - он нам подходит"):
                        self.scroll(checkbox)
                        if not checkbox.is_selected():
                            checkbox.click()
                else:
                    with allure.step(f"Этот чекбокс {checkbox.get_attribute('value')} не подходит нам"):
                        continue
        return self
                    
    def radiobox_list_clicks(self) -> 'MainPage':
        """Метод для кликов по радиокнопкам из списка."""
        self.wait.wait_for_presence(MPL.radio)
        radioboxes = self.find_elements(*MPL.radio)
        self.scroll(radioboxes[0])
        for radiobox in radioboxes:
            with allure.step(f"Проверяем радиокнопку {radiobox.get_attribute('value')}"):
                if radiobox.get_attribute("value") == MPL.radio_value:
                    with allure.step("Выбираем радиокнопку Red - она нам подходит"):
                        if not radiobox.is_selected():
                            radiobox.click()
                    return self
        raise AssertionError(f"Радиокнопка со значением '{MPL.radio_value}' не найдена")
    
    def get_select(self) -> WebElement:
        """Метод для выбора элемента из выпадающего списка."""
        self.wait.wait_for_presence(MPL.select)
        select_element = self.find_element(*MPL.select)
        self.scroll(select_element)
        with allure.step("Ищем поле с выбором"):
            return select_element
        
    def select_choose(self, value: str = None) -> 'MainPage':
        """Метод для выбора элемента из выпадающего списка по значению."""
        self.wait.wait_for_clickable(MPL.select)
        with allure.step(f"Выбираем элемент {value} из выпадающего списка"):
            select = Select(self.get_select())
            select.select_by_visible_text(value)
        return self
            
    def get_email_input(self) -> WebElement:
        """Метод для получения элемента поля ввода почты."""
        self.wait.wait_for_presence(MPL.email_input)
        email = self.find_element(*MPL.email_input)
        self.scroll(email)
        with allure.step("Ищем поле для ввода почты"):
            return email

    def email_send(self, mail: str = None) -> 'MainPage':
        """Метод для ввода текста в поле почты с валидацией формата."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, mail):
            with allure.step("Вводим почту, прошедший валидацию"):
                self.get_email_input().send_keys(mail)
        else:
            with allure.step("Почта у нас не прошла валидацию на формат name@example.com"):
                raise ValueError(f'Ваша почта - {mail} не соответствует формату name@example.com')
        return self    
            
    def get_message_input(self) -> WebElement:
        """Метод для получения элемента поля ввода сообщений."""
        self.wait.wait_for_presence(MPL.message)
        mess = self.find_element(*MPL.message)
        self.scroll(mess)
        with allure.step("Ищем поле для сообщенй"):
            return mess

    def send_longest(self) -> 'MainPage':
        """Метод для ввода самого длинного текста из списка в поле сообщений."""
        self.wait.wait_for_presence(MPL.list_items)
        lst = self.find_elements(*MPL.list_items)
        texts = [element.text for element in lst]
        texts = sorted(texts, key=lambda x: len(x))
        with allure.step("Вводим нужный текст в поле сообщений"):
            self.get_message_input().send_keys(texts[-1])
        return self
        
    def get_submit(self) -> WebElement:
        """Метод для получения элемента кнопки подтверждения."""
        self.wait.wait_for_clickable(MPL.submit_button)
        submitButton = self.find_element(*MPL.submit_button)
        self.scroll(submitButton)
        with allure.step("Ищем кнопку подтвердить"):
            return submitButton
        
    def submit_click(self) -> 'MainPage':
        """Метод для клика по кнопке подтверждения."""
        self.wait.wait_for_clickable(MPL.submit_button)
        with allure.step("Подтверждаем"):
            self.driver.execute_script("arguments[0].click();", self.get_submit())
        return self
    
    def check_text_alert(self) -> str:
        """Метод для просмотра текста, который выпал из Alert после клика по кнопке подтверждения."""
        alert = self.driver.switch_to.alert
        with allure.step("Проверяем какой текст выпал из Alert"):
            return alert.text
        
    def check_alert(self) -> bool:
        """Метод для проверки наличия Alert после клика по кнопке подтверждения."""
        try:
            alert = self.driver.switch_to.alert
            with allure.step("Нам выпал алерт"):
                return True
        except:
            with allure.step("Нам алерт не выпал, тест относится к негативному тест кейсу"):
                return False