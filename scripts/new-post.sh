#!/usr/bin/env bash
# 意图：创建新文章时自动生成唯一文件名，避免同一天同题文章发生 URL 冲突。
# 维护原则：这里只处理文章文件创建，不处理主题、构建或发布逻辑。

set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "用法: scripts/new-post.sh \"文章题目\"" >&2
  exit 1
fi

title="$*"

python3 - "$title" <<'PY'
import json
from pathlib import Path
import sys
from datetime import datetime

title = sys.argv[1]
posts_dir = Path("content/posts")
posts_dir.mkdir(parents=True, exist_ok=True)

# 秒级时间戳用于区分同一天的同题文章；标题仍只负责展示。
slug = datetime.now().astimezone().strftime("%Y%m%d-%H%M%S")
path = posts_dir / f"{slug}.md"

now = datetime.now().astimezone().isoformat(timespec="seconds")

# JSON 字符串也是合法 YAML 标量；用标准库转义标题，避免引号、冒号等字符破坏 front matter。
content = f"""---
title: {json.dumps(title, ensure_ascii=False)}
date: {json.dumps(now)}
draft: true
slug: {json.dumps(slug)}
tags: []
categories: []
summary: ""
---

"""

with open(path, "x", encoding="utf-8") as file:
    file.write(content)

print(path)
PY
