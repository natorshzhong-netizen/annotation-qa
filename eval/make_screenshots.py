# -*- coding: utf-8 -*-
"""生成评测仪表盘、测试输出和报告预览的截图。

前置
    python eval/run_attribution_eval.py --seeds 10
    python benchmarks/prepare.py --limit 10000 --out-root benchmarks/data_full
    python eval/summarize_benchmarks.py
    python -m src --data-dir benchmarks/data_full/hatexplain --allow-missing \
        --max-rows 4 --out benchmarks/reports/hatexplain_compact.md

然后
    python eval/make_screenshots.py
"""

from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "screenshots"
OUT.mkdir(parents=True, exist_ok=True)

CHROME_CANDIDATES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]

CSS = """
:root {
  --ink: #17202a; --muted: #667085; --line: #e6e8ec;
  --bg: #f5f6f8; --card: #ffffff; --blue: #2563eb; --green: #16a34a;
  --amber: #d97706; --red: #dc2626; --violet: #7c3aed;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--ink);
  font-family: "Microsoft YaHei", "PingFang SC", "Segoe UI", sans-serif;
  -webkit-font-smoothing: antialiased;
}
.wrap { max-width: 1220px; margin: 0 auto; padding: 46px 40px 60px; }
.eyebrow {
  font-size: 12px; letter-spacing: .18em; color: var(--blue);
  font-weight: 700; margin-bottom: 12px;
}
h1 { font-size: 34px; line-height: 1.25; margin: 0 0 10px; letter-spacing: -.02em; }
.lead { color: var(--muted); font-size: 15px; margin: 0 0 18px; }
.badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 28px; }
.badge {
  border: 1px solid var(--line); background: #fff; color: #344054;
  border-radius: 999px; padding: 5px 12px; font-size: 12px; font-weight: 600;
}
.badge.green { border-color: #bbe7c7; background: #f0fdf4; color: #15803d; }
.badge.blue { border-color: #c7d7fe; background: #eef4ff; color: #1d4ed8; }
.stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 34px; }
.stat {
  background: var(--card); border: 1px solid var(--line); border-radius: 14px;
  padding: 18px 18px 16px; box-shadow: 0 1px 2px rgba(16,24,40,.04);
}
.stat .k { color: var(--muted); font-size: 12px; font-weight: 600; }
.stat .v { font-size: 30px; font-weight: 750; letter-spacing: -.02em; margin: 8px 0 4px; }
.stat .v small { font-size: 14px; font-weight: 500; color: var(--muted); }
.stat .d { color: var(--muted); font-size: 12px; }
section { margin-bottom: 34px; }
h2 { font-size: 20px; margin: 0 0 4px; display: flex; align-items: baseline; gap: 10px; }
h2 .num { color: var(--blue); font-size: 12px; letter-spacing: .12em; }
.sub { color: var(--muted); font-size: 13px; margin: 0 0 14px; }
.card {
  background: var(--card); border: 1px solid var(--line); border-radius: 14px;
  padding: 8px 18px 14px; box-shadow: 0 1px 2px rgba(16,24,40,.04);
}
table { width: 100%; border-collapse: collapse; font-size: 13.5px; }
th {
  text-align: left; color: var(--muted); font-weight: 600; font-size: 12px;
  padding: 12px 10px; border-bottom: 1px solid var(--line); white-space: nowrap;
}
td { padding: 11px 10px; border-bottom: 1px solid #f0f1f4; vertical-align: middle; }
tr:last-child td { border-bottom: none; }
.num-cell { font-variant-numeric: tabular-nums; font-family: "Cascadia Code", Consolas, monospace; }
.right { text-align: right; }
.mono { font-family: "Cascadia Code", Consolas, monospace; font-size: 12.5px; }
.green { color: var(--green); } .amber { color: var(--amber); } .red { color: var(--red); }
.pill { display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 11.5px; font-weight: 600; }
.pill.ok { background: #ecfdf3; color: #15803d; }
.pill.warn { background: #fffaeb; color: #b54708; }
.pill.high { background: #fef3f2; color: #b42318; }
.meter { height: 6px; background: #eef0f3; border-radius: 99px; overflow: hidden; width: 120px; }
.meter span { display: block; height: 100%; background: var(--blue); border-radius: 99px; }
.legend { display: flex; gap: 18px; color: var(--muted); font-size: 12px; margin: 10px 0 4px; }
.legend i { display: inline-block; width: 9px; height: 9px; border-radius: 2px; margin-right: 6px; }
.stack { display: flex; height: 10px; border-radius: 99px; overflow: hidden; background: #eef0f3; }
.stack span { display: block; height: 100%; }
.note { color: var(--muted); font-size: 12.5px; margin-top: 10px; }
footer { color: var(--muted); font-size: 12px; border-top: 1px solid var(--line); padding-top: 16px; }
"""


def _fmt(value: float, digits: int = 3) -> str:
    return f"{value:.{digits}f}"


def load_data() -> tuple[list[dict], dict, dict]:
    results = json.loads((ROOT / "benchmarks" / "results.json").read_text(encoding="utf-8"))
    eval_report = json.loads((ROOT / "eval" / "report.json").read_text(encoding="utf-8"))
    return results, eval_report["aggregate"], eval_report


def render_dashboard(results: list[dict], synthetic: dict, full_eval: dict, tests: str) -> str:
    runs = len(full_eval["runs"])
    total_items = sum(r["items"] for r in results)
    total_anns = sum(r["annotators"] for r in results)
    total_flagged = sum(r["flagged_total"] for r in results)
    passed = re.search(r"(\d+) passed", tests)
    count = passed.group(1) if passed else "?"

    stats = f"""
    <div class="stats">
      <div class="stat"><div class="k">合成归因 Macro-F1</div>
        <div class="v green">{_fmt(synthetic['macro_f1'][0])}</div>
        <div class="d">基线 {_fmt(synthetic['baseline_macro_f1'][0])} · {runs} 个随机种子</div></div>
      <div class="stat"><div class="k">测试</div>
        <div class="v">{count}</div>
        <div class="d">指标对拍 + 归因回归 + 稀疏数据</div></div>
      <div class="stat"><div class="k">公开数据集</div>
        <div class="v">{total_items:,}<small> 条</small></div>
        <div class="d">{len(results)} 份数据 · {total_anns} 个标注者/槽</div></div>
      <div class="stat"><div class="k">识别出的系统性偏差</div>
        <div class="v">{total_flagged}</div>
        <div class="d">BH 校正后 q &lt; 0.05</div></div>
    </div>
    """

    syn_rows = ""
    for cls in ["规范未覆盖", "系统性偏差", "个别错误", "无争议"]:
        m = synthetic["per_class"][cls]
        syn_rows += (
            f"<tr><td>{cls}</td><td class='right num-cell'>{m['support_total']:,}</td>"
            f"<td class='right num-cell'>{_fmt(m['precision'][0])}</td>"
            f"<td class='right num-cell'>{_fmt(m['recall'][0])}</td>"
            f"<td class='right num-cell'>{_fmt(m['f1'][0])}</td></tr>"
        )

    dataset_rows = ""
    for r in results:
        width = max(2, min(100, round(r["agreement"] * 100)))
        color = "var(--green)" if r["agreement"] >= 0.6 else ("var(--amber)" if r["agreement"] >= 0.4 else "var(--red)")
        dataset_rows += f"""
        <tr>
          <td><strong>{html.escape(r['dataset'])}</strong><br><span class="mono">{html.escape(r['license'])}</span></td>
          <td class="right num-cell">{r['items']:,}</td>
          <td class="right num-cell">{r['annotators']}</td>
          <td class="right num-cell">{r['annotations']:,}</td>
          <td>{html.escape(r['metric'])}<br><span class="mono">{_fmt(r['agreement'])}</span>
              <span class="mono">[{_fmt(r['ci'][0])}, {_fmt(r['ci'][1])}]</span></td>
          <td><div class="meter"><span style="width:{width}%;background:{color}"></span></div></td>
          <td class="right num-cell">{r['disputes']:,}</td>
          <td class="right num-cell">{r['flagged_total']}</td>
        </tr>"""

    hate = next((r for r in results if r["name"] == "hatexplain"), None)
    flagged_rows = ""
    if hate:
        for row in hate["flagged_annotators"][:5]:
            q = "&lt;0.001" if row["q_value"] < 0.001 else f"{row['q_value']:.3f}"
            flagged_rows += f"""
            <tr><td class="mono">{row['name']}</td>
              <td>{html.escape(row['label'])}</td>
              <td class="right num-cell">{row['count']} / {row['opportunities']}</td>
              <td class="right num-cell">{row['dominance']:.0%}</td>
              <td class="right num-cell">{q}</td>
              <td><span class="pill high">系统性偏差</span></td></tr>"""

    bars = ""
    for r in results:
        d = r["dispute_counts"]
        total = max(1, sum(d.values()))
        seg = "".join(
            f"<span style='width:{d[k]/total*100:.1f}%;background:{color}'></span>"
            for k, color in [("规范未覆盖", "#2563eb"), ("系统性偏差", "#d97706"), ("个别错误", "#98a2b3")]
        )
        bars += f"""
        <div style="margin:14px 0 18px">
          <div style="display:flex;justify-content:space-between;font-size:12.5px;margin-bottom:6px">
            <strong>{html.escape(r['dataset'])}</strong>
            <span class="mono">{total:,} 条争议</span>
          </div>
          <div class="stack">{seg}</div>
          <div class="legend">
            <span><i style="background:#2563eb"></i>规范未覆盖 {d['规范未覆盖']:,}</span>
            <span><i style="background:#d97706"></i>系统性偏差 {d['系统性偏差']:,}</span>
            <span><i style="background:#98a2b3"></i>个别错误 {d['个别错误']:,}</span>
          </div>
        </div>"""

    return f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<style>{CSS}</style></head><body><div class="wrap">
<header>
  <div class="eyebrow">ANNOTATION QA · EVALUATION DASHBOARD</div>
  <h1>标注质检器：把归因结论变成可验证的数字</h1>
  <p class="lead">一致性指标 + 规则归因 + 统计检验 · 合成真值回归 + 三份公开数据集实测</p>
  <div class="badges">
    <span class="badge green">{count} tests passed</span>
    <span class="badge blue">Python 3.11–3.13 CI</span>
    <span class="badge">Krippendorff's α</span>
    <span class="badge">二项检验 + BH 校正</span>
    <span class="badge">稀疏标注支持</span>
  </div>
</header>
{stats}

<section>
  <h2><span class="num">01</span>归因准确率：用已知真值反测规则</h2>
  <p class="sub">合成数据先注入「规范空白 / 系统性偏差 / 随机错误」，再看工具能否把原因认回来；{runs} 个随机种子，每组 300 条。</p>
  <div class="card"><table>
    <thead><tr><th>类别</th><th class="right">支持数</th><th class="right">Precision</th><th class="right">Recall</th><th class="right">F1</th></tr></thead>
    <tbody>{syn_rows}
      <tr><td><strong>Macro-F1</strong></td><td class="right">—</td><td class="right">—</td><td class="right">—</td>
      <td class="right num-cell green"><strong>{_fmt(synthetic['macro_f1'][0])}</strong></td></tr>
    </tbody>
  </table></div>
  <div class="note">对照基线（只按「有没有多数派」判断）：Macro-F1 {_fmt(synthetic['baseline_macro_f1'][0])}。真值来自生成器注入，不是人工标注。</div>
</section>

<section>
  <h2><span class="num">02</span>公开数据集：一致性指标</h2>
  <p class="sub">真实众包数据，标注者会漏标；不齐时自动改用 Krippendorff's α，并只统计共同标注。</p>
  <div class="card"><table>
    <thead><tr><th>数据集</th><th class="right">样本</th><th class="right">标注者</th><th class="right">标注数</th><th>一致性</th><th>水平</th><th class="right">争议</th><th class="right">偏差者</th></tr></thead>
    <tbody>{dataset_rows}</tbody>
  </table></div>
  <div class="note">GoEmotions 与 HateXplain 为 10,000 条抽样；ChaosNLI 为全部 1,599 条，每条随机抽 5 个标注槽（无跨样本身份，只用于一致性）。
  GoEmotions / ChaosNLI 是开放域标注，没有业务规范，归因计数只用于验证规则，不代表真实质检结论。</div>
</section>

<section>
  <h2><span class="num">03</span>HateXplain：被判定为系统性偏差的标注者</h2>
  <p class="sub">不是「偏离几次就算」，而是主导标签占比 ≥ 60% 且二项检验 q &lt; 0.05；166 人里识别出 {hate['flagged_total'] if hate else 0} 人。</p>
  <div class="card"><table>
    <thead><tr><th>标注者</th><th>主导标签</th><th class="right">少数派次数 / 机会</th><th class="right">主导占比</th><th class="right">q 值</th><th>判定</th></tr></thead>
    <tbody>{flagged_rows}</tbody>
  </table></div>
</section>

<section>
  <h2><span class="num">04</span>分歧构成</h2>
  <p class="sub">同一套规则在三份真实数据上的分布。</p>
  <div class="card">{bars}</div>
</section>

<footer>
  数据来源：GoEmotions (Apache-2.0) · HateXplain (MIT) · ChaosNLI (CC BY-NC 4.0) ·
  报告由 <span class="mono">annotation-qa</span> 生成 · 2026-11-13
</footer>
</div></body></html>"""


def render_tests(tests: str) -> str:
    return f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<style>
body {{ margin:0; background:#0b1020; padding:36px; font-family:"Cascadia Code", Consolas, monospace; }}
.term {{ max-width:1180px; margin:0 auto; border-radius:14px; overflow:hidden;
        box-shadow:0 30px 80px rgba(0,0,0,.45); border:1px solid #1f2a44; }}
.bar {{ background:#161d31; padding:11px 14px; display:flex; align-items:center; gap:8px; }}
.dot {{ width:11px; height:11px; border-radius:50%; display:inline-block; }}
.title {{ color:#8b98b8; font-size:12px; margin-left:8px; }}
pre {{ margin:0; padding:22px 24px; background:#0d1426; color:#c9d5f2; font-size:14px;
       line-height:1.62; white-space:pre-wrap; }}
.pass {{ color:#3ddc84; }} .dim {{ color:#6b7a99; }} .cmd {{ color:#7aa2ff; }}
</style></head><body><div class="term">
<div class="bar"><span class="dot" style="background:#ff5f56"></span>
<span class="dot" style="background:#ffbd2e"></span>
<span class="dot" style="background:#27c93f"></span>
<span class="title">annotation-qa — python -m pytest -v</span></div>
<pre><span class="cmd">$ .venv/Scripts/python.exe -m pytest -v</span>
{tests}</pre></div></body></html>"""


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("|"):
            header = [c.strip() for c in line.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in header) + "</tr></thead><tbody>")
            for row in rows:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
            out.append("</tbody></table>")
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            out.append(f"<h{level}>{inline(line.lstrip('# ').strip())}</h{level}>")
            i += 1
            continue
        if line.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip("> ").strip())
                i += 1
            out.append("<blockquote>" + inline(" ".join(buf)) + "</blockquote>")
            continue
        if re.match(r"^\d+\.\s", line):
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i]):
                out.append(f"<li>{inline(re.sub(r'^\\d+\\.\\s', '', lines[i]))}</li>")
                i += 1
            out.append("</ol>")
            continue
        out.append(f"<p>{inline(line)}</p>")
        i += 1
    return "\n".join(out)


def inline(text: str) -> str:
    text = html.escape(text).replace("&lt;br&gt;", "<br>")
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def render_report(md: str) -> str:
    body = md_to_html(md)
    return f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<style>
body {{ margin:0; background:#eef0f4; font-family:"Microsoft YaHei","PingFang SC",sans-serif; color:#1f2937; }}
.paper {{ max-width:980px; margin:34px auto; background:#fff; border-radius:10px;
         box-shadow:0 18px 50px rgba(15,23,42,.12); padding:44px 54px 54px; }}
h1 {{ font-size:30px; margin:0 0 6px; }}
h2 {{ font-size:20px; margin:30px 0 10px; padding-top:18px; border-top:1px solid #e5e7eb; }}
h3 {{ font-size:15px; margin:20px 0 8px; color:#374151; }}
p, li {{ font-size:13.5px; line-height:1.7; }}
hr {{ display:none; }}
table {{ width:100%; border-collapse:collapse; margin:10px 0 14px; font-size:12.5px; }}
th {{ text-align:left; background:#f8fafc; color:#475569; font-weight:600; padding:8px 9px; border-bottom:1px solid #e2e8f0; }}
td {{ padding:7px 9px; border-bottom:1px solid #f1f5f9; vertical-align:top; }}
tr:nth-child(even) td {{ background:#fcfdff; }}
blockquote {{ margin:12px 0; padding:10px 14px; background:#f8fafc; border-left:3px solid #93c5fd; color:#475569; font-size:12.5px; }}
code {{ background:#f1f5f9; padding:1px 5px; border-radius:4px; font-family:Consolas,monospace; font-size:12px; }}
ul, ol {{ padding-left:22px; }}
</style></head><body><div class="paper">{body}</div></body></html>"""


def screenshot(html_path: Path, png_path: Path, width: int, height: int) -> None:
    chrome = next((p for p in CHROME_CANDIDATES if p.exists()), None)
    if chrome is None:
        raise SystemExit("找不到 Chrome / Edge，无法截图")
    cmd = [
        str(chrome), "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=2", f"--window-size={width},{height}",
        f"--screenshot={png_path}", html_path.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"[screenshot] {png_path.name}")


def main() -> None:
    venv_python = ROOT / ".venv" / "Scripts" / "python.exe"
    python = str(venv_python) if venv_python.exists() else sys.executable
    pytest = subprocess.run(
        [python, "-m", "pytest", "-v", "--color=no"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    tests_text = pytest.stdout + pytest.stderr
    match = re.search(r"(\d+) passed", tests_text)
    if not match:
        raise SystemExit("pytest 没有通过，先修测试再截图")
    print(f"[tests] {match.group(1)} passed")

    results, synthetic, full_eval = load_data()

    dashboard = OUT / "dashboard.html"
    dashboard.write_text(render_dashboard(results, synthetic, full_eval, tests_text), encoding="utf-8")
    screenshot(dashboard, OUT / "dashboard.png", 1400, 2050)

    tests_html = OUT / "tests.html"
    tests_html.write_text(render_tests(tests_text), encoding="utf-8")
    screenshot(tests_html, OUT / "tests.png", 1200, 500)

    compact = ROOT / "benchmarks" / "reports" / "hatexplain_compact.md"
    if compact.exists():
        report_html = OUT / "report.html"
        report_html.write_text(render_report(compact.read_text(encoding="utf-8")), encoding="utf-8")
        screenshot(report_html, OUT / "report.png", 1200, 2100)


if __name__ == "__main__":
    main()
