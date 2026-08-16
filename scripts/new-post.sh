#!/usr/bin/env bash
# 意图：创建新文章时自动生成唯一文件名，避免同一天同题文章发生 URL 冲突。
# 维护原则：这里只处理文章文件创建，不处理主题、构建或发布逻辑。

set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "用法: scripts/new-post.sh \"文章题目\"" >&2
  exit 1
fi

title="$*"

python3 - "$title" "${2:-}" <<'PY'
import json
from pathlib import Path
import sys
from datetime import datetime

title = sys.argv[1]
slug_prefix = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else ""
posts_dir = Path("content/posts")
posts_dir.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now().astimezone().strftime("%Y%m%d-%H%M%S")
if slug_prefix:
    slug = f"{slug_prefix}-{timestamp}"
else:
    slug = timestamp

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

