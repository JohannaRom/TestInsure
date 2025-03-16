import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    user_name = "jrom@kesset.ca"
    password = "rom123"
    return [user_name, password]


# @pytest.fixture(scope="module")
# def driver():
#    _driver = webdriver.Chrome()
#   yield _driver
#   _driver.quit()

#@pytest.fixture(params=["Edge","Firefox"],scope='module')
@pytest.fixture(scope="module")
def driver(request):
    #if request.param=="Edge":
    _driver=webdriver.Edge()
    #if request.param=="Firefox":
    #    _driver = webdriver.Firefox()
    yield _driver
    _driver.quit()
