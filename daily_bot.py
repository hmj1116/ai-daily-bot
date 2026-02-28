import requests
import datetime
from bs4 import BeautifulSoup

# 1️⃣ 钉钉 Webhook
DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=0b6d7a2af6a1768be7285e2a8c5f6de05bbe685677cfc3115f841b76cb285e66"

# 2️⃣ 小词典
glossary = {
    "大模型": "训练参数非常多的人工智能模型，如GPT、Claude等",
    "强化学习": "机器通过试错和奖励机制学习最佳策略的算法",
    "生成式AI": "能自动生成文本、图片、音频等内容的人工智能",
}

# 3️⃣ 日期
today = datetime.date.today()

# 4️⃣ 抓取新闻（36氪 AI 频道示例）
url = "https://36kr.com/information/web_news?category=ai"
try:
    resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    
    # 找到新闻列表（示例解析，可能需要根据实际网页调整）
    news_items = soup.find_all("a", class_="article-item-title")[:5]  # 取前5条新闻
    news_list = []
    for item in news_items:
        title = item.get_text(strip=True)
        link = item['href']
        if link.startswith("/"):
            link = "https://36kr.com" + link
        news_list.append({"title": title, "link": link})
except Exception as e:
    print("新闻抓取失败:", e)
    news_list = []

# 5️⃣ 构造日报内容
content_lines = [f"【日报】 {today}\n新闻："]

if news_list:
    for idx, news in enumerate(news_list, start=1):
        title = news["title"]
        link = news["link"]
        # 查找小词典解释
        terms = [glossary[word] for word in glossary if word in title]
        term_text = "\n   小词典：" + "; ".join(terms) if terms else ""
        content_lines.append(f"{idx}. 标题：{title}\n   链接：{link}{term_text}")
else:
    content_lines.append("今天没有抓到新闻。")

content = "\n".join(content_lines)

# 6️⃣ 发送到钉钉
data = {"msgtype": "text", "text": {"content": content}}

try:
    response = requests.post(DINGTALK_WEBHOOK, json=data, timeout=10)
    print(f"发送状态码: {response.status_code}")
    print(f"返回内容: {response.text}")
    if response.status_code == 200 and response.json().get("errcode") == 0:
        print("日报发送成功！")
    else:
        print("发送失败，请检查Webhook地址或钉钉安全设置！")
except requests.exceptions.RequestException as e:
    print("发送请求失败！")
    print(e)
