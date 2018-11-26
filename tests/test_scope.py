import pytest


@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print('\nsetupSession run')


@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print('\nsetupModule run')


@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print('\nsetupFunction run')


def test1():
    print('test1 run')
    assert True


def test2():
    print('test2 run')
    assert True


