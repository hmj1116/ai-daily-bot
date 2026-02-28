import requests
import datetime

# ✅ 这里换成你的钉钉机器人Webhook
DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=0b6d7a2af6a1768be7285e2a8c5f6de05bbe685677cfc3115f841b76cb285e66"

# 当前日期
today = datetime.date.today()

# 消息内容（一定包含钉钉关键词“日报”）
content = f"【日报】\n日期：{today}\n今天的AI新闻和小词典内容更新完成！"

# 请求数据
data = {
    "msgtype": "text",
    "text": {"content": content}
}

try:
    response = requests.post(DINGTALK_WEBHOOK, json=data, timeout=10)
    print(f"发送状态码: {response.status_code}")
    print(f"返回内容: {response.text}")

    # 判断是否成功
    if response.status_code == 200 and response.json().get("errcode") == 0:
        print("日报发送成功！")
    else:
        print("发送失败，请检查Webhook地址或钉钉安全设置！")

except requests.exceptions.RequestException as e:
    print("发送请求失败！")
    print(e)
