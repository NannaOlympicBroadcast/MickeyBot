import datetime
import time

import requests
import json

import search_online


def mickey_mouse(words):
    response = requests.post(
        'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=M8QKyhGk6KF7hDO8r0f7mqho&client_secret=fKfTP0qrQ6H4IuqzI4QvkuODrAsCgOQL',
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
    session_ticket = response.json().get('access_token')
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + session_ticket

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "你现在是米老鼠，用户向你说:" + words + "，你的回应是："
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    ret = response.json().get("result")
    print("Response Received: " + ret)
    return ret

def lucky_today():
    response = requests.post(
        'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=M8QKyhGk6KF7hDO8r0f7mqho&client_secret=fKfTP0qrQ6H4IuqzI4QvkuODrAsCgOQL',
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
    session_ticket = response.json().get('access_token')
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + session_ticket

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "你现在是米老鼠,今天的日期是" + time.asctime(time.localtime(time.time())) + "，请你依照日期，写一句今日运势"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    ret = response.json().get("result")
    print("Response Received: " + ret)
    return ret

def touch_head():
    response = requests.post(
        'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=M8QKyhGk6KF7hDO8r0f7mqho&client_secret=fKfTP0qrQ6H4IuqzI4QvkuODrAsCgOQL',
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
    session_ticket = response.json().get('access_token')
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + session_ticket

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "你现在是米老鼠,用户摸了摸你的头，你向用户说"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    ret = response.json().get("result")
    print("Response Received: " + ret)
    return ret

def mickey_ol(question):
    response = requests.post(
        'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=M8QKyhGk6KF7hDO8r0f7mqho&client_secret=fKfTP0qrQ6H4IuqzI4QvkuODrAsCgOQL',
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
    session_ticket = response.json().get('access_token')
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + session_ticket

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "用户向你提了一个问题"+question+"，给出的一个最合适的搜索关键词为（只要输出那一个关键词，不要其他内容）"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    ret = response.json().get("result")
    retstr = search_online.search(ret)
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + session_ticket
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "用户向你提了一个问题" + question + "，给出的一个最合适的搜索关键词为（只要输出那一个关键词，不要其他内容）"
            },
            {
                "role": "assistant",
                "content": ret
            },
            {
                "role": "user",
                "content": "用户搜索到了这些结果："+retstr+"，搜索结果可能有重复，并且只是导向一个结果的标题，请再次给出相应回答"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("result")

