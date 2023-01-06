class Test_Class:
    def __init__(self, x, y):
        self.x = x + 1
        self.y = y + 1

    def test_tow(self):
        assert self.x == 5

    def test_th(self):
        assert self.y == 5


a = Test_Class(3, 3)
a.test_tow()
a.test_th()
