import requests


def search(key):
    returns = "";
    response = requests.get("https://v.api.aa1.cn/api/baidu-search/?msg=" + key)
    result_list = response.json()["data"]
    for var in result_list:
        returns += key
    return returns


