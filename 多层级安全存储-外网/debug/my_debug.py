from requests_toolbelt import MultipartEncoder
import requests


def qtest():
    m = MultipartEncoder(fields={'upload': open('../TestData/excel.xlsx', 'rb')},
                         )
    params = {'path': 'test.txt',
              'token': '123456',
              'num': 0, 'offset': 0,
              'limit': 8}
    response = requests.post('http://httpbin.org/post',
                             params=params,
                             data=m,
                             headers={'Content-Type': m.content_type})
    print(m.content_type, type(m.content_type))


if __name__ == '__main__':
    qtest()
