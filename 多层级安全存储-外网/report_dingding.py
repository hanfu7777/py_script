import unittest
from unittestreport import TestRunner
import settings


def report_dingding(access_token, TestCases_dir, key):
    """
    :param access_token: 钉钉的token值
    :param TestCases_dir: 收集用例的套件地址
    :param key: 钉钉机器人设置的关键字
    :return:
    """
    suite = unittest.defaultTestLoader.discover(TestCases_dir)
    runner = TestRunner(suite, **settings.MY_MAIN)
    # 执行用例
    runner.run()
    url = "https://oapi.dingtalk.com/robot/send?" + access_token
    # 发送钉钉通知
    runner.dingtalk_notice(url=url, key=key)


if __name__ == '__main__':
    report_dingding('access_token=9938ba2c6ce89594a0241efdf09470183e4d38f2274b915a1f860540339556c8', 'TestCases',
                    '测试')
