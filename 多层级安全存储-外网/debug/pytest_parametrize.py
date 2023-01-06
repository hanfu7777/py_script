import pytest

data = ["小红", "小明"]


@pytest.mark.parametrize("name1", data)
# parametrize(self,names, values, indirect=False, ids=None, scope=None)
# names：参数名。
# values：参数对应值，类型必须为list。如果只有一个参数，里面则是值的列表：
# indirect：如果设置成True，则把传进来的参数当函数执行，而不是一个参数。
# ids：用例的ID，传一个字符串列表，用来标识每一个测试用例，自定义测试数据结果，增加可读性。
def test_demo(name1):
    print("测试数据为{}".format(name1))
