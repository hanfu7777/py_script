import os

# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 日志配置
LOG_CONFIG = {
    'name': os.path.join(BASE_DIR, 'duo_ceng'),
    'filename': os.path.join(BASE_DIR, 'logs/多层级自动化日志.log'),
    'debug': False
}

# 测试数据配置
TSET_DATA_FILE = {
    'file': os.path.join(BASE_DIR, 'TestData/TestCases.xlsx'),
    'sheet_OSB': 'OSB'
}
# 测试报告
# REPORT_CONFIG = {
#     'filename': os.path.join(BASE_DIR, 'reports/芯煜测试报告.html')
# }
# 鉴权    注意换环境更改TestCases.xlsx用例中的url和TOKEN信息
# 主要的账号   这里一般使用账号  hanfu/hanfu123456
TOKEN = {
    'username': 'hanfu',
    'password': 'hanfu123456',
    'url': 'http://124.70.179.141:9701/login'
}
# 辅助账号 一般测试权限的时候用的到
TOKEN_AD = {
    'username': 'test7',
    'password': 'test7123456',
    'url': 'http://124.70.179.141:9701/login'
}

MY_MAIN = {
    'filename': "多层级测试报告.html",  # 测试报告文件名
    'report_dir': 'reports',  # 测试报告输出路径
    # 'report_dir': os.path.join(BASE_DIR, 'reports'),
    'title': "多层级安全存储测试报告",  # 测试报告标题
    'tester': "韩同学",  # 测试人员名称
    'desc': "接口自动化测试报告飞起来吧",  # 测试报告描述
    'templates': 2  # 测试报告模板  1比较古风、2最帅、3是简版的
}

if __name__ == '__main__':
    print(BASE_DIR)
    print(LOG_CONFIG.get('name'))
    print(LOG_CONFIG.get('filename'))
    print(TSET_DATA_FILE.get('file'))
    print(MY_MAIN.get('report_dir'))
