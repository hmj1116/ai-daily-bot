import requests
from datetime import datetime

# ----------------------------
# 配置
# ----------------------------
DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=0b6d7a2af6a1768be7285e2a8c5f6de05bbe685677cfc3115f841b76cb285e66"
NEWS_LIST = [
    {"title": "OpenAI 发布 GPT-5", "link": "https://xxx.com/news1"},
    {"title": "百度文心大模型更新", "link": "https://xxx.com/news2"},
]

DICTIONARY = {
    "GPT": "生成式预训练模型，可以生成文字内容",
    "大模型": "拥有海量参数的人工智能模型",
}

# ----------------------------
# 生成日报内容
# ----------------------------
today = datetime.now().strftime("%Y-%m-%d")
message = f"📅 AI 每日新闻日报 - {today}\n\n"

for news in NEWS_LIST:
    title = news["title"]
    link = news["link"]
    for word in DICTIONARY:
        if word in title:
            title += f"（{DICTIONARY[word]}）"
    message += f"- {title}\n  {link}\n\n"

# ----------------------------
# 发送到钉钉
# ----------------------------
data = {
    "msgtype": "text",
    "text": {"content": message}
}
requests.post(DINGTALK_WEBHOOK, json=data)
print("日报发送完成！")
