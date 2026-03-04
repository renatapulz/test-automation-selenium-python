import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure

@pytest.fixture
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver

    # Teardown: tira um screenshot se o teste falhar
    if hasattr(request.node, "rep_call") and getattr(request.node.rep_call, "failed", False):
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
    driver.quit()

# Hook para registrar se o teste falhou
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)