# Hugo 个人博客

这个仓库放我的 Hugo 博客。

文章按题目来组织，日期只用来排序和记录时间，不放进文章 URL。

[站点仓库](https://github.com/billzi2016/blog)  
[GitHub Actions](https://github.com/billzi2016/blog/actions)

## 目录

```text
.
├── .github/workflows/     # Pages 部署
├── archetypes/            # 新文章模板
├── assets/                # 样式
├── content/               # 文章
├── layouts/               # 页面模板
├── specs/                 # 需求、结构和任务记录
├── static/                # 原样发布的静态文件
├── AGENTS.md              # 协作规则
├── hugo.toml              # Hugo 配置
└── README.md
```

## 写文章

文章放在 `content/posts/`。文件名用清楚的 slug，别用日期当主结构。

```bash
hugo new posts/example-topic.md
```

每篇文章保留这些字段：

```yaml
title: "文章题目"
date: "2026-08-15T04:00:00+08:00"
draft: true
slug: "example-topic"
tags: []
categories: []
summary: ""
```

## 本地预览

需要先安装 Hugo Extended。

```bash
hugo server -D
```

## 部署

推送到 `main` 后，Actions 会构建并发布到 GitHub Pages。
