from pages.home_page import HomePage;

def test_open_qabrains_homepage(driver):
    home = HomePage(driver)
    home.open()
    assert "Automation Testing Practice Website for QA" in home.get_title()
