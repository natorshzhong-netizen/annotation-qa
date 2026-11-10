# -*- coding: utf-8 -*-
"""入口：在项目根目录执行 `python -m src`

会打印报告，并写一份到 out/report.md。
"""
import sys
from pathlib import Path

from .load import load_all
from .report import build_report

# Windows 控制台默认 GBK，中文报告和报错信息会变乱码，这里强制 UTF-8
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent


def main():
    items, labels, anns = load_all(ROOT / "data")
    use_llm = "--llm" in sys.argv
    if use_llm:
        print("[第三方复核] 首次运行要给每条争议问一次本地模型，约 30-60 秒/条，结果会缓存。")
    md = build_report(items, labels, anns, use_llm=use_llm)
    print(md)

    out_dir = ROOT / "out"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "report.md").write_text(md, encoding="utf-8")
    print(f"\n[已写入] {out_dir / 'report.md'}")


if __name__ == "__main__":
    main()
