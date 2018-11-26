import pytest


@pytest.fixture(scope="class", autouse=True)
def setupClass():
    print('\nsetupClass run')


class TestClass:

    def test1(self):
        print('test class run')
        assert True

