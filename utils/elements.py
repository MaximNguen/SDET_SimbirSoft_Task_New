from selenium.webdriver.common.by import By

class MainPageLocators:
    """Класс для хранения локаторов элементов и значений ячеек на странице."""
    
    name_input = (By.XPATH, "//input[@id='name-input']")
    password_input = (By.CSS_SELECTOR, "input[type='password']")
    checkboxes = (By.CSS_SELECTOR, 'input[name="fav_drink"]')
    radio = "Red"
    select = (By.ID, "automation")
    email_input = (By.ID, "email")
    list_items = (By.TAG_NAME, "li")
    message = (By.ID, "message")
    submit_button = (By.ID, "submit-btn")