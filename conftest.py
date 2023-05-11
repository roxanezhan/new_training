import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    user = request.config.getoption("--user")
    userpassword = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, user=user, userpassword=userpassword)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url, user=user, userpassword=userpassword)
    fixture.session.ensure_login(username=user, password=userpassword)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--user", action="store")
    parser.addoption("--password", action="store")