import pytest
from pages.home_page import HomePage

menu_links = [
    ("QA Topics", "https://qabrains.com/topics"),
    ("Discussion", "https://qabrains.com/discussion"),
    ("Tags", "https://qabrains.com/tags"),
    ("Jobs", "https://qabrains.com/jobs"),
    ("Practice Site", "https://qabrains.com/practice-site"),
    ("About Us", "https://qabrains.com/about"),
]

@pytest.mark.parametrize("link_text, expected_url", menu_links)
def test_menu_links(driver, link_text, expected_url):
    home = HomePage(driver)
    home.open()
    home.go_to_menu(link_text)

    assert home.url_matches(expected_url), f"{link_text} não redirecionou corretamente: {home.get_current_url()}"