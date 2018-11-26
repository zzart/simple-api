import pytest


@pytest.fixture()
def setup():
    print('\nsetup run')


@pytest.fixture(autouse=True)
def another_setup():
    print('\nanother setup run')
    yield
    print('teardown another setup called')


@pytest.fixture(autouse=True)
def another_setup_with_finalizer(request):
    print('\nfinalizer ')

    def teardown_a():
        print('teardown a')

    def teardown_b():
        print('teardown b')

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup):
    print('test1 run')
    assert True


@pytest.mark.usefixtures('setup')
def test2(setup):
    print('test2 run')
    assert True


