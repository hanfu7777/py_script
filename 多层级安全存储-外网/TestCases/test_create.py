import json
import re
import unittest
import settings
import time
from common.make_requests import send_http_requests
from common.Test_data_handler import get_test_data_from_excel, replace_args_by_re
from common.myddt import ddt, data
from common import logger, get_token
from common.my_random import generate_random_str

# 直接导入了__init__中实例好的模块

cases = get_test_data_from_excel(settings.TSET_DATA_FILE['file'], settings.TSET_DATA_FILE['sheet_OSB'])


# 直接导入配置文件的库，就可以直接用配置文件的大字典了。配置文件已经封装好了大字典，所以可以直接参数化

@ddt
class Test_config(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 实例化logger
        cls.logger = logger
        # 随机生成的类属性
        cls.logger.warning(
            "====================================多层级存储开始执行==============================================")
        cls.bucketName = str(generate_random_str(10, 'int'))
        cls.long_bk = str(generate_random_str(63, 'random'))
        cls.in_bk = str(generate_random_str(20, 'random'))
        cls.short_bk = str(generate_random_str(3, 'random'))
        cls.in_int_bk = str(generate_random_str(25, 'int'))
        cls.in_str_bk = str(generate_random_str(25, 'str'))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.logger.warning(
            "====================================多层级存储执行结束==============================================")

    @data(*cases)    #相当于for case in cases:
    def test_(self, case):
        # 字典判断不了VALUE,只能判断KEY
        if "#token#" in case["headers"]:
            # 获取全新的token------具体项目具体分析
            token = get_token.login(**settings.TOKEN)['data']['token']
            # 替换槽位
            case['headers'] = case['headers'].replace("#token#", token)
        if '#token_AD#' in case["headers"]:
            token = get_token.login(**settings.TOKEN_AD)['data']['token']
            case['headers'] = case['headers'].replace("#token_AD#", token)
            # print(f'token替换成功,新请求头是{case["headers"]}')
        if re.findall('#.*?#', case['json']):
            # 如果json中有##包裹的字段,就要进行替换
            case['json'] = replace_args_by_re(case['json'], self)
        if re.findall('#.*?#', case['expected']):
            # 如果expected中有##包裹的字段,就要进行替换
            case['expected'] = replace_args_by_re(case['expected'], self)
        self.logger.info(f"用例【{case['title']}】开始测试,这是第【{case['case_id']}】条用例")
        self.logger.info(f"发起请求的地址是：{case['url']}")
        #  先替换,在进行反序列化
        case['json'] = json.loads(case['json'])
        case['expected'] = json.loads(case['expected'])
        case['headers'] = json.loads(case['headers'])
        case['files'] = json.loads(case['files'])
        if case['files'].get('path', 0):  # 上传文件
            files = {
                "file": (case['files']['filename'], open(case['files']['path'], "rb"), 'application/json')
            }
            response = send_http_requests(url=case['url'], method=case["method"], headers=case['headers'],
                                          data=case['json'], files=files)
            response_data = response.json()
        else:
            response = send_http_requests(url=case['url'], method=case["method"], headers=case['headers'],
                                          json=case['json'])
            response_data = response.json()
        # 断言
        try:
            # 状态码断言
            self.assertEqual(case['expected']['code'], int(response_data['code']))
            print(f"测试【{case['title']}】请求成功,响应状态码为{response_data['code']}响应消息为{response_data}")
            # 公共框架代码，一般的项目都可以用得到(case是个字典)
            if case['expected']['data'].get('total', None):
                if case['json']['pageSize'] * case['json']['pageNum'] <= response_data['data']['total']:
                    self.assertEqual(case['json']['pageSize'], len(response_data['data']['buckets']))
                elif case['json']['pageSize'] * case['json']['pageNum'] > response_data['data']['total'] and \
                        case['json']['pageSize'] > case['json']['pageSize'] * case['json']['pageNum'] - \
                        response_data['data']['total']:
                    self.assertEqual(
                        case['json']['pageSize']-(case['json']['pageSize'] * case['json']['pageNum'] - response_data['data']['total']),
                        len(response_data['data']['buckets']))
                else:
                    self.assertEqual(0, len(response_data['data']['buckets']))
                # excel中的#unknown#没有替换,没有用到,只是占了个位置
            elif case['expected']['data'].get('data', None):
                # 如果data中填写了'data'就要进行信息的断言
                self.assertEqual(case['expected']['data']['data']['bucketName'],
                                 response_data['data']['data']['bucketName'])
                self.assertEqual(case['expected']['data']['data']['bucketPolicy'],
                                 response_data['data']['data']['bucketPolicy'])
                self.assertEqual(case['expected']['data']['data']['createdUser'],
                                 response_data['data']['data']['createdUser'])
            elif case['json'].get('time', 0):
                # 如果有分享的用例，那么就访问这个分享的链接
                if case['json']['time'] >= 2:
                    Share_url = response_data['data']
                    # print('分享成功,url为{}'.format(Share_url))
                    res = send_http_requests(Share_url, 'get').text
                    self.assertIn('中文会乱码', res)
                else:
                    Share_url = response_data['data']
                    time.sleep(1)
                    res = send_http_requests(Share_url, 'get').status_code
                    self.assertNotEqual(res, 200)

        except AssertionError as e:
            self.logger.warning(f"断言失败!响应消息为{response_data['message']}")
            self.logger.warning(f"期望结果是{case['expected']['code']}")
            self.logger.warning(f"响应结果是{response_data['code']}")
            # 写入日志
            print(f"×××××××××××××××××××××××断言失败!响应消息为{response_data}×××××××××××××××××××××")
            print(f"期望结果是{case['expected']}")
            print(f"响应结果是{response_data}")
            # print可以写入测试报告中
            raise e
        else:
            self.logger.info(f"√√√√√√√√√√√√√√√√√√√√用例【{case['title']}】测试通过√√√√√√√√√√√√√√√√√√√√")
        finally:
            self.logger.info(f"--------------------用例【{case['title']}】测试结束--------------------")
