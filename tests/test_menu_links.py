import pytest
from pages.home_page import HomePage

top_menu_links = [
    ("QA Topics", "https://qabrains.com/topics"),
    ("Discussion", "https://qabrains.com/discussion"),
    ("Tags", "https://qabrains.com/tags"),
    ("Jobs", "https://qabrains.com/jobs"),
    ("Practice Site", "https://qabrains.com/practice-site"),
    ("About Us", "https://qabrains.com/about"),
]

side_menu_data = [
    ("Login", "Login", "button"),
    ("Registration", "Signup", "button"),
    ("Forgot Password", "Reset Password", "button"),
    ("Form Submission", "Submit", "button"),
    ("Drag and Drop List", "Drag & Drop", "h2"),
    ("E-Commerce Site", "E-Commerce Demo Site", "title_div"),
]

@pytest.mark.parametrize("link_text, expected_url", top_menu_links)
def test_top_menu_links(driver, link_text, expected_url):
    home = HomePage(driver)
    home.open()
    home.go_to_menu(link_text)

    assert home.url_matches(expected_url), f"{link_text} não redirecionou corretamente: {home.get_current_url()}"

@pytest.mark.parametrize("menu_label, expected_text, search_type", side_menu_data)
def test_side_menu_navigation(driver, menu_label, expected_text, search_type):
    home = HomePage(driver)
    home.open()
    home.click_side_menu(menu_label)
    
    # Valida o conteúdo baseado no tipo definido na lista
    assert home.validate_page_content(expected_text, search_type), \
        f"Erro: A tela '{menu_label}' não carregou o elemento '{expected_text}' corretamente."
