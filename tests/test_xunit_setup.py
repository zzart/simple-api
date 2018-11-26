
def test1():
    print('test1 run')
    assert True


def test2():
    print('test2 run')
    assert True


def setup_function(function):
    if function == test1:
        print('setup run for test1')
    elif function == test2:
        print('setup run for test2')


def teardown_function(function):
    if function == test1:
        print('teardown run for test1')
    elif function == test2:
        print('teardown run for test2')


def setup_module():
    print('setup module')


def teardown_module():
    print('teardown module')


class TestClass:

    @classmethod
    def setup_class(cls):
        print('setup class')

    @classmethod
    def teardown_class(cls):
        print('teardown class')

    def test3(self):
        print('test3 run')
        assert True

    def test4(self):
        print('test4 run')
        assert True
