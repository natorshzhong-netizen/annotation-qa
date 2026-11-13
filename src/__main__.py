# -*- coding: utf-8 -*-
"""命令行入口。

    python -m src                          # 跑 data/ 下的样例
    python -m src --data-dir path/to/data  # 跑别的数据集
    python -m src --allow-missing          # 允许标注者漏标
    python -m src --llm                    # 加本地模型第三方复核
"""

import argparse
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m src", description="标注一致性 + 分歧归因报告")
    parser.add_argument("--data-dir", default=str(ROOT / "data"), help="数据目录")
    parser.add_argument("--out", default=str(ROOT / "out" / "report.md"), help="报告输出路径")
    parser.add_argument("--allow-missing", action="store_true", help="允许标注者漏标")
    parser.add_argument("--llm", action="store_true", help="启用本地模型第三方复核")
    parser.add_argument("--max-rows", type=int, default=30, help="报告里每张表最多显示多少行")
    args = parser.parse_args(argv)

    items, labels, anns = load_all(args.data_dir, allow_missing=args.allow_missing)
    if args.llm:
        print("[第三方复核] 首次运行要给每条争议问一次本地模型，约 30-60 秒/条，结果会缓存。")

    md = build_report(items, labels, anns, use_llm=args.llm, max_rows=args.max_rows)
    print(md)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding="utf-8")
    print(f"\n[已写入] {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
