import requests

DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxxxxxx"

data = {
    "msgtype": "text",
    "text": {
        "content": "【测试】如果你看到这条消息，说明Webhook可以正常使用！"
    }
}

response = requests.post(DINGTALK_WEBHOOK, json=data)
print("状态码:", response.status_code)
print("返回内容:", response.text)
