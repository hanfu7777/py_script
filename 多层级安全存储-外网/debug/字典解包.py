MY_MAIN = {
    'filename': "多层级测试报告.html",  # 测试报告文件名
    'report_dir': 'reports',  # 测试报告输出路径
    # 'report_dir': os.path.join(BASE_DIR, 'reports'),
    'title': "多层级安全存储测试报告",  # 测试报告标题
    'tester': "韩同学",  # 测试人员名称
    'desc': "接口自动化测试报告飞起来吧",  # 测试报告描述
    'templates': 2  # 测试报告模板  1比较古风、2最帅、3是简版的
}


def dict_Unpack(filename, report_dir, title, tester, desc, templates):
    print(filename, report_dir, title, tester, desc, templates)


dict_Unpack(**MY_MAIN)
