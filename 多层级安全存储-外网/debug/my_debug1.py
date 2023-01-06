import datetime
import requests
import uuid
import os


def downFile(url, mkdir='temp', fileExt='xlsx'):
    """
        url: 文件地址url
        mkdir: 文件存放文件夹
        fileExt: 下载的文件后缀
        返回 文档地址
    """
    # \\ 转义
    defaultDir = r'E:\多层级安全存储\debug' + mkdir + '\\'
    # 路径添加当前年月日
    defaultDir += datetime.datetime.now().strftime('%Y-%m-%d')
    # 如果不存在就创建
    if not os.path.exists(defaultDir):
        os.makedirs(defaultDir)
    filePath = defaultDir + '\\' + str(uuid.uuid4()).replace('-', '') + '.' + fileExt
    # 文件下载
    res = requests.get(url, stream=True)
    with open(r'' + filePath, "wb") as pyFile:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                pyFile.write(chunk)
    return filePath


if __name__ == '__main__':
    downFile('http://124.70.179.141:81/obs/object/download', 'E:\多层级安全存储\debug\down_mkdir', fileExt='txt')
