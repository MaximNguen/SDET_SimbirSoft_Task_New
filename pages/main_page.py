import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
import allure

from pages.base_page import BasePage
from utils.elements import MainPageLocators as MPL
from utils.waitUtils import WaitUtils as WU

class MainPage(BasePage):
    """Класс для взаимодействия с главной страницей приложения."""
    
    def __init__(self, driver):
        """Инициализация драйвера и утилит ожидания."""
        super().__init__(driver)
        self.wait = WU(driver)
        
    def open(self, url) -> None:
        """Открытие страницы по URL."""
        with allure.step(f"Открыть страницу по URL: {url}"):
            self.driver.get(url)
            
    def scroll(self, element) -> None:
        """Метод прокрутки до указанного элемента."""
        with allure.step(f"Прокрутить страницу до элемента: {element}"):
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            
    def quit(self) -> None:
        """Метод выхода из браузера."""
        with allure.step("Закрываем браузер"):
            self.driver.quit()
            
    def get_name_input(self) -> WebElement:
        """Метод для получения элемента поля ввода имени."""
        self.wait.wait_for_presence((MPL.name_input[0], MPL.name_input[1]))
        name = self.find_element(MPL.name_input[0], MPL.name_input[1])
        self.scroll(name)
        with allure.step("Поиск поле для ввода имени"):
            return name
        
    def enter_name(self, text) -> None:
        """Метод для ввода текста в поле имени."""
        with allure.step("Ввод текста в поле имени"):
            return self.get_name_input().send_keys(text)
        
    def get_password_input(self) -> WebElement:
        """Метод для получения элемента поля ввода пароля."""
        self.wait.wait_for_presence((MPL.password_input[0], MPL.password_input[1]))
        password = self.find_element(MPL.password_input[0], MPL.password_input[1])
        self.scroll(password)
        with allure.step("Поиск поле для пароля"):
            return password

    def fill_password(self, text) -> None:
        """Метод для ввода текста в поле пароля."""
        with allure.step("Ввод пароля"):
            return self.get_password_input().send_keys(text)
        
    def checkbox_list_clicks(self, selected_checkboxes) -> None:
        """Метод для кликов по чекбоксам из списка."""
        self.wait.wait_for_presence((MPL.checkboxes[0], MPL.checkboxes[1]))
        checkboxes = self.find_elements(MPL.checkboxes[0], MPL.checkboxes[1])
        self.scroll(checkboxes[0])
        for checkbox in checkboxes:
            with allure.step(f"Проверяем чекбокс {checkbox.get_attribute('value')}"):
                checkbox_value = checkbox.get_attribute("value")
                if checkbox_value in selected_checkboxes:
                    with allure.step(f"Выбираем чекбокс {checkbox_value} - он нам подходит"):
                        checkbox.click()
                else:
                    with allure.step(f"Этот чекбокс {checkbox.get_attribute('value')} не подходит нам"):
                        continue
                    
    def radiobox_list_clicks(self) -> None:
        """Метод для кликов по радиокнопкам из списка."""
        self.wait.wait_for_presence((MPL.RADIO1[0], MPL.RADIO1[1]))
        radioboxes = self.find_elements(MPL.RADIO1[0], MPL.RADIO1[1])
        self.scroll(radioboxes[0])
        for radiobox in radioboxes:
            with allure.step(f"Проверяем радиокнопку {radiobox.get_attribute('value')}"):
                if radiobox.get_attribute("value") == MPL.radio:
                    with allure.step("Выбираем радиокнопку Red - она нам подходит"):
                        radiobox.click()
                else:
                    with allure.step(f"Этот радиобокс {radiobox.get_attribute('value')} не подходит нам"):
                        continue
        
    def select(self) -> WebElement:
        """Метод для выбора элемента из выпадающего списка."""
        self.wait.wait_for_presence((MPL.select[0], MPL.select[1]))
        select_element = self.find_element(MPL.select[0], MPL.select[1])
        self.scroll(select_element)
        with allure.step("Ищем поле с выбором"):
            return select_element
        
    def select_choose(self, value) -> None:
        """Метод для выбора элемента из выпадающего списка по значению."""
        self.wait.wait_for_clickable((MPL.select[0], MPL.select[1]))
        with allure.step(f"Выбираем элемент {value} из выпадающего списка"):
            select = Select(self.select())
            select.select_by_visible_text(value)
            
    def email(self) -> WebElement:
        """Метод для получения элемента поля ввода почты."""
        self.wait.wait_for_presence((MPL.email_input[0], MPL.email_input[1]))
        email = self.find_element(MPL.email_input[0], MPL.email_input[1])
        self.scroll(email)
        with allure.step("Ищем поле для ввода почты"):
            return email

    def email_send(self, mail) -> None:
        """Метод для ввода текста в поле почты с валидацией формата."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, mail):
            with allure.step("Вводим почту, прошедший валидацию"):
                return self.email().send_keys(mail)
        else:
            with allure.step("Почта у нас не прошла валидацию на формат name@example.com"):
                raise ValueError(f'Ваша почта - {mail} не соответствует формату name@example.com')

    def message(self) -> WebElement:
        """Метод для получения элемента поля ввода сообщений."""
        self.wait.wait_for_presence((MPL.message[0], MPL.message[1]))
        mess = self.find_element(MPL.message[0], MPL.message[1])
        self.scroll(mess)
        with allure.step("Ищем поле для сообщенй"):
            return mess

    def send_longest(self) -> None:
        """Метод для ввода самого длинного текста из списка в поле сообщений."""
        self.wait.wait_for_presence((MPL.list_items[0], MPL.list_items[1]))
        lst = self.find_elements(MPL.list_items[0], MPL.list_items[1])
        texts = [element.text for element in lst]
        texts = sorted(texts, key=lambda x: len(x))
        with allure.step("Вводим нужный текст в поле сообщений"):
            return self.message().send_keys(texts[-1])
        
    def submit(self) -> WebElement:
        """Метод для получения элемента кнопки подтверждения."""
        self.wait.wait_for_clickable((MPL.submit[0], MPL.submit[1]))
        submitButton = self.find_element(MPL.submit[0], MPL.submit[1])
        self.scroll(submitButton)
        with allure.step("Ищем кнопку подтвердить"):
            return submitButton
        
    def submit_click(self) -> None:
        """Метод для клика по кнопке подтверждения."""
        self.wait.wait_for_clickable((MPL.submit[0], MPL.submit[1]))
        with allure.step("Подтверждаем"):
            return self.driver.execute_script("arguments[0].click();", self.submit())

    def check_state_alert(self) -> str:
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