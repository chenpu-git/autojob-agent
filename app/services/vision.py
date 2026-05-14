import base64

from openai import OpenAI

from app.core.config import settings

client = OpenAI(
    api_key=settings.MIMO_API_KEY,
    base_url=settings.MIMO_BASE_URL,
)


def analyze_screenshot(screenshot_bytes: bytes, prompt: str) -> str:
    """将 Playwright 截图发给 MiMo V2.5 进行视觉分析。"""
    b64_image = base64.b64encode(screenshot_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model=settings.MIMO_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "你是MiMo，是小米公司研发的AI智能助手。"
                    "你擅长分析网页截图，识别页面元素并给出精确的操作建议。"
                ),
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{b64_image}",
                        },
                    },
                    {
                        "type": "text",
                        "text": prompt,
                    },
                ],
            },
        ],
        max_completion_tokens=1024,
    )

    return response.choices[0].message.content
