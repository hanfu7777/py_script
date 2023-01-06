import requests
import json


def login(username, password, url):
    res = requests.post(url=url, json=
    {
        "password": password,
        "username": username
    },
                        headers={'Content-Type': 'application/json'}).text
    res = json.loads(res)
    # 反序列化  json -> dict
    return res


if __name__ == '__main__':
    token = login("hanfu", "hanfu123456", "http://192.168.0.250:14000/login")['data']['token']
    # 获取响应消息中data中的token
    print(token, type(token))
