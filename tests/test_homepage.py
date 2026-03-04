from pages.home_page import HomePage

def test_open_qabrains_homepage(driver):
    home = HomePage(driver)
    home.open()
    assert "QA Practice Site" in home.get_title()
