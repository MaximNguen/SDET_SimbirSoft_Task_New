from selenium.webdriver.common.by import By

class Elements:
    """Класс для хранения локаторов элементов на странице."""
    
    name_input = (By.XPATH, "//input[@id='name-input']")
    password_input = (By.CSS_SELECTOR, "input[type='password']")
    #CHECKBOX1 = (By.ID, "drink2") # Moloko
    #CHECKBOX2 = (By.ID, "drink3") # Coffee
    #RADIO1 = (By.ID, "color3")
    select = (By.ID, "automation")
    email_input = (By.ID, "email")
    list_items = (By.TAG_NAME, "li")
    message = (By.ID, "message")
    submit_button = (By.ID, "submit-btn")