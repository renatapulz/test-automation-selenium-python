from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

class HomePage:
    URL = "https://practice.qabrains.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def click_menu(self, label):
        self.driver.find_element(By.LINK_TEXT, label).click()

    def click_side_menu(self, label):
        xpath = f"//li[@role='menuitem' and contains(., '{label}')]"  # O '.' busca em todo o conteúdo da linha, ignorando se tem ícone ou span no meio
        
        elemento = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        elemento.click()

    def get_side_menu_items(self):
        # Espera até os itens do menu aparecerem
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "li[role='menuitem']:not([aria-disabled='true'])")
            )
        )

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def url_matches(self, expected_url):
        current_parsed = urlparse(self.get_current_url())
        expected_parsed = urlparse(expected_url)
        return (
            current_parsed.netloc == expected_parsed.netloc and
            current_parsed.path.rstrip('/') == expected_parsed.path.rstrip('/')
        )

    def go_to_menu(self, label):
        self.click_menu(label)
        if len(self.driver.window_handles) > 1:
            self.switch_to_last_tab()
    
    def validate_page_content(self, expected_text, search_type):
        wait = WebDriverWait(self.driver, 7)
        
        if search_type == "button":
            xpath = f"//button[@type='submit' and contains(., '{expected_text}')]"
        elif search_type == "title_div":
            xpath = f"//div[@data-slot='alert-title' and contains(., '{expected_text}')]"
        elif search_type == "h2":
            xpath = f"//h2[contains(., '{expected_text}')]"
        else:
            raise ValueError(f"Tipo de busca '{search_type}' não reconhecido.")

        try:
            return wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).is_displayed()
        except:
            return False