import unittest
import unittestreport

import settings


if __name__ == '__main__':
    # unittest的测试套件——收集用例
    s = unittest.TestLoader().discover('TestCases')  # TestCases是测试用例的目录
    # 通过木森的前端测试报告，将用例进行渲染
    runner = unittestreport.TestRunner(s, **settings.MY_MAIN)
    runner.run()




