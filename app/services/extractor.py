from openai import OpenAI

from app.core.config import settings

client = OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url=settings.DEEPSEEK_BASE_URL,
)

EXTRACTION_PROMPT = """请将以下招聘网页文本清洗为标准 JSON 数组。
每个职位包含以下字段：
- title: 职位名称
- company: 公司名称
- salary: 薪资范围（如 "150-200元/天"）
- location: 工作地点
- link: 职位链接（如有）

只返回 JSON 数组，不要额外解释。如果没有有效职位信息，返回空数组 []。

原始文本：
"""


def extract_jobs(raw_text: str) -> list[dict]:
    """使用 DeepSeek 将网页纯文本提取为结构化职位数据。"""
    response = client.chat.completions.create(
        model=settings.DEEPSEEK_MODEL,
        messages=[
            {"role": "user", "content": EXTRACTION_PROMPT + raw_text},
        ],
        max_completion_tokens=4096,
        temperature=0.1,
    )

    import json

    content = response.choices[0].message.content.strip()
    if content.startswith("```"):
        content = content.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    return json.loads(content)
