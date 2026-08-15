# Hugo 个人博客

这个仓库放 Hugo 博客项目。

文章以题目作为主要阅读入口，日期用于排序和记录时间。URL 由创建时生成的唯一 ID 决定，同一天的同题文章也会得到不同地址。

主题用 PaperMod，通过 Hugo Modules 引入；仓库主要保存内容、配置和写作辅助脚本。

[博客站点](https://billzi2016.github.io/blog/)

## 目录

```text
.
├── .github/workflows/     # Pages 部署
├── archetypes/            # 新文章模板
├── content/               # 文章
├── specs/                 # 需求、结构和任务记录
├── scripts/               # 写作辅助脚本
├── static/                # 原样发布的静态文件
├── AGENTS.md              # 协作规则
├── go.mod                 # Hugo Modules
├── hugo.toml              # Hugo 配置
└── README.md
```

## 写文章

文章放在 `content/posts/`。脚本会根据标题创建文章，并生成带时间戳的文件名和 slug。

```bash
scripts/new-post.sh "文章题目"
```

每篇文章保留这些字段：

```yaml
title: "文章题目"
date: "2026-08-15T04:00:00+08:00"
draft: true
slug: "20260815-040000"
tags: []
categories: []
summary: ""
```

同一天写两篇相同题目时，URL 由脚本处理；脚本会生成不同文件名和不同 slug。

## 本地预览

本地预览依赖 Hugo Extended 和 Go。

```bash
hugo server -D
```

提交前先跑一次本地构建：

```bash
hugo --gc --minify
```

## 部署

推送到 `main` 后，Actions 会构建并发布到 GitHub Pages。
