import pytest


@pytest.mark.usefixtures('function_fixture')
class TestClass:
    def test_noe(self):
        print('test_one')

    def test_two(self):
        print('test_two')


@pytest.fixture
def function_fixture():
    print('>>>我是一个函数级前置')
    yield
    print('我是一个函数级后置<<<')