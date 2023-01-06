"""
需求:
1、能够根据用例发送对应的方法
2、能够动态接收不同的请求参数json，params，data，headers，cookies
解释：
1、发送一个请求有两个必传参数，method、url。其他参数可以动态生产，使用**kwargs来接收
（**kwargs参数用=的方式传入，如headers=case[headers],此时调用kwargs就是一个python字典）
"""
import requests


def send_http_requests(url, method, **kwargs) -> requests.Response:
    """
    发送http请求
    :param url: 请求的url
    :param method: 请求的方法
    :param kwargs: 请求的其他参数 ，如data、json、headers  使用的时候这样用：
    send_http_requests(url=case['url'], method=case["method"], headers=case['headers'],json=case['json'])
    :return: 返回这个请求结果，默认是状态码
    """
    # 把方法名小写化,防止误传
    method = method.lower()
    # getattr 反射机制
    return getattr(requests, method)(url=url, **kwargs)


if __name__ == '__main__':
    res = send_http_requests('https://www.baidu.com/', 'get')
    res.encoding = 'utf-8'
    print(res.status_code, type(res.status_code), res.text)
