def test_open_qabrains_homepage(driver):
    driver.get("https://qabrains.com/practice-site")
    
    assert "Automation Testing Practice Website for QA" in driver.title