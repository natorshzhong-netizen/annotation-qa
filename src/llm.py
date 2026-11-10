# -*- coding: utf-8 -*-
"""让本地大模型做「第三方裁定」。

为什么需要它：
    规则分类只看三个人的投票分布，看不见规范文本。
    而模型可以只读规范、**不看人类标签**，独立判一遍——
    它像个没参与讨论的第三方，能打破「大家都这么标」的共谋。

为什么不让它看人类标签：
    看了就会被锚定，倾向于附和多数派。
    盲判才有独立价值。
"""

import json
import os
import urllib.error
import urllib.request

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434")
MODEL = os.environ.get("QA_MODEL", "qwen3:8b")
TIMEOUT = int(os.environ.get("QA_TIMEOUT", "200"))
UNDECIDED = "无法确定"

PROMPT = """下面是客服工单的标注规范。

【规范】
{spec}

【样本】{item}

任务：只根据规范，给这条样本打一个类别。
- 规范里有类别定义能覆盖它 → 填那个类别名，并原样引用规范里的支撑原文。
- 规范里没有任何一个类别能覆盖它 → label 填「{undecided}」。
不许使用规范以外的常识来推断。

只输出 JSON，不要解释：
{{"label": "类别名或{undecided}", "quote": "规范原文", "reason": "一句话"}}"""


def _post(prompt: str) -> str:
    payload = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {"temperature": 0},
    }).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.load(resp).get("response", "")


def _parse(text: str) -> dict:
    text = text.strip()
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"模型没返回 JSON：{text[:120]}")
    data = json.loads(text[start:end + 1])
    return {
        "label": str(data.get("label", "")).strip(),
        "quote": str(data.get("quote", "")).strip(),
        "reason": str(data.get("reason", "")).strip(),
    }


def judge(spec: str, item_text: str) -> dict:
    """盲判：只给规范和样本，不给人类标签。"""
    return _parse(_post(PROMPT.format(spec=spec, item=item_text, undecided=UNDECIDED)))


def available() -> bool:
    try:
        with urllib.request.urlopen(f"{OLLAMA_URL}/api/tags", timeout=3) as r:
            return r.status == 200
    except (urllib.error.URLError, OSError):
        return False
