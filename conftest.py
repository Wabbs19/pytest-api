import json
from pytest import fixture
from test_api.config_api import set_api


# добавление парсеров
def pytest_addoption(parser):
    parser.addoption('--reqtype', action="store", help='Request type')
    parser.addoption('--country', action="store", help='Choosing country')
    parser.addoption('--crd', action="store", help='confirmed/recovered/deaths')
    parser.addoption('--datefrom', action="store", help='Date from')
    parser.addoption('--dateto', action="store", help='Date to')
    parser.addoption('--province', action="store", help='Province/State')
    parser.addoption('--city', action="store", help='City')


# получение значений из парсеров
@fixture(scope='session')
def list_of_pyt_adds(request):
    mlist = [
        request.config.getoption("--reqtype"), # sum, daily
        request.config.getoption("--country"), # e.g. russia
        request.config.getoption("--crd"), # confirmed, recovered, deaths
        request.config.getoption("--datefrom"), # e.g. 2020-04-01
        request.config.getoption("--dateto"), # e.g. 2020-04-05
        request.config.getoption("--province"), # e.g. Hubei, "New York"
        request.config.getoption("--city") # e.g. Washington
    ]
    return mlist


@fixture(scope='session')
def api_request(list_of_pyt_adds):
    return set_api(list_of_pyt_adds)
