import pytest


@pytest.mark.usefixtures('function_fix', 'function_class')
class TestClass:
    def test_one(self):
        print('test_one')

    def test_two(self):
        print('test_two')


@pytest.fixture()
def function_fix():
    print('>>>我是一个函数级的前置')
    assert True


@pytest.fixture(scope='class')
def function_class():
    print('>>>我是一个类级前置')
