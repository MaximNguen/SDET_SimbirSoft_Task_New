# utils/test_data.py
import allure


class TestData:
    """Класс для хранения тестовых данных."""
    
    # Положительные тест-кейсы: полное заполнение формы
    positive_full_form_data = [
        {
            "name": "Maxim",
            "password": "9012832",
            "drinks": ["Milk", "Coffee"],
            "color": "Red",
            "automation": "Yes",
            "email": "maxim@example.com",
            "expected_alert": "Message received!",
            "expected_text_message": "5, Katalon Studio"
        },
        {
            "name": "Pasha",
            "password": "kasljdasds",
            "drinks": ["Milk", "Coffee"],
            "color": "Red",
            "automation": "No",
            "email": "pasha@mail.ru",
            "expected_alert": "Message received!",
            "expected_text_message": "5, Katalon Studio"
        },
        {
            "name": "Egor228443",
            "password": "()*@)(#*!@*#)",
            "drinks": ["Milk", "Coffee"],
            "color": "Red",
            "automation": "Undecided",
            "email": "egor@gmail.com",
            "expected_alert": "Message received!",
            "expected_text_message": "5, Katalon Studio"
        },
    ]
    
    # Положительные тест-кейсы: только обязательные поля (только имя)
    positive_required_only_data = [
        {"name": "klasjdsad", "expected_alert": "Message received!"},
        {"name": "skjdsadasdd", "expected_alert": "Message received!"},
        {"name": "28973123*(@&#*(&!@#&asjkhdaskld", "expected_alert": "Message received!"}
    ]
    
    # Положительные тест-кейсы: неполное заполнение (проверка скролла)
    positive_partial_form_data = [
        {"name": "91283990()*@(*!@$", "expected_alert": "Message received!", "expected_text_message": "5, Katalon Studio"},
        {"name": "[;];;;];]", "expected_alert": "Message received!", "expected_text_message": "5, Katalon Studio"},
        {"name": "28973123*(@&#*(&!@#&asjkhdaskld", "expected_alert": "Message received!", "expected_text_message": "5, Katalon Studio"},
    ]
    
    # Негативные тест-кейсы: заполнение всех полей кроме имени
    negative_without_name_data = [
        {
            "password": "92138123",
            "drinks": ["Milk", "Coffee"],
            "color": "Red",
            "automation": "Yes",
            "email": "name@example.ru",
            "expected_alert": False,
            "expected_text_message": "5, Katalon Studio"
        },
        {
            "password": "jksdhasd",
            "drinks": ["Milk", "Coffee"],
            "color": "Red",
            "automation": "Yes",
            "email": "name@example.rum",
            "expected_alert": False,
            "expected_text_message": "5, Katalon Studio"
        },
        {
            "password": "hsad127327(@)*(][][;",
            "drinks": ["Milk", "Coffee"],
            "color": "Red",
            "automation": "Yes",
            "email": "name@example.ru",
            "expected_alert": False,
            "expected_text_message": "5, Katalon Studio"
        },
    ]
    
    # Негативные тест-кейсы: только необязательные поля
    negative_optional_only_data = [
        {
            "drinks": ["Milk", "Coffee"],
            "expected_alert": False,
            "description": "Заполнены только напитки"
        }
    ]