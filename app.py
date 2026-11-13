# -*- coding: utf-8 -*-
"""标注质检台 · 网页版

运行：
    python app.py
然后浏览器打开终端里显示的地址（通常 http://127.0.0.1:7860）。

界面只做三件事：收文件、调 build_report、把结果给出去。
所有算法都在 src/ 里，这里不写任何计算逻辑。
"""

import hashlib
import json
from pathlib import Path

import gradio as gr

from src.load_csv import labels_of, load_from_csv
from src.report import build_report

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
OUT.mkdir(exist_ok=True)


def run(csv_file, spec_file, use_llm, allow_missing):
    if not csv_file:
        return "⚠ 请先上传标注结果 CSV", None

    try:
        items, anns = load_from_csv(csv_file, allow_missing=allow_missing)
    except Exception as e:
        return f"⚠ 读数据失败：{e}", None

    labels = labels_of(anns)
    spec = ""
    if spec_file:
        spec = Path(spec_file).read_text(encoding="utf-8", errors="replace")

    # 不同数据集用不同缓存文件，避免结果串味
    fingerprint = hashlib.md5(
        json.dumps(
            [sorted(items), {k: sorted(v.items()) for k, v in anns.items()}],
            ensure_ascii=False,
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()[:8]

    try:
        md = build_report(
            items, labels, anns,
            use_llm=bool(use_llm),
            spec=spec,
            cache_path=OUT / f"llm_cache_{fingerprint}.json",
        )
    except Exception as e:
        return f"⚠ 分析失败：{e}", None

    out_file = OUT / "report_ui.md"
    out_file.write_text(md, encoding="utf-8")

    summary = (
        f"✅ 完成：{len(items)} 条样本、{len(anns)} 个标注者、{len(labels)} 个类别\n\n"
        f"报告已保存到 `{out_file}`\n\n---\n\n"
    )
    return summary + md, str(out_file)


with gr.Blocks(title="标注质检台") as demo:
    gr.Markdown(
        "# 标注质检台\n"
        "上传同一批样本的多人标注结果，看分歧到底出在**规范**还是**人**。"
    )

    with gr.Row():
        csv_in = gr.File(label="标注结果 CSV", file_types=[".csv"])
        spec_in = gr.File(label="标注规范（可选）", file_types=[".md", ".txt"])

    llm_in = gr.Checkbox(
        label="启用第三方复核（本地模型，每条 30-60 秒）", value=False
    )
    missing_in = gr.Checkbox(
        label="允许标注者漏标（真实众包数据建议勾选）", value=False
    )
    btn = gr.Button("开始分析", variant="primary")

    preview = gr.Markdown()
    file_out = gr.File(label="下载报告")

    btn.click(run, [csv_in, spec_in, llm_in, missing_in], [preview, file_out])

    gr.Markdown(
        "**CSV 格式**：`id, text, annotator, label`，一行代表一个人对一条样本的标注。\n\n"
        "可以参考 `data/sample.csv`。"
    )

if __name__ == "__main__":
    demo.launch()
