# Hugo 个人博客

这是一个 Hugo 静态博客项目，内容组织方式是“题目为主，日期为辅”。

[站点仓库](https://github.com/billzi2016/blog)  
[GitHub Actions](https://github.com/billzi2016/blog/actions)

## 项目结构

```text
.
├── .github/workflows/     # GitHub Pages 构建部署工作流
├── archetypes/            # Hugo 新文章模板
├── assets/                # 样式和可被 Hugo Pipeline 处理的资源
├── content/               # 博客正文内容
├── layouts/               # Hugo 页面模板
├── specs/                 # PRD、项目结构和任务清单
├── static/                # 原样复制到站点根目录的静态资源
├── AGENTS.md              # 项目协作与质量规则
├── hugo.toml              # Hugo 站点配置
└── README.md              # 项目说明
```

## 写作方式

新文章放在 `content/posts/` 下，文件名使用清晰的英文或拼音 slug。

```bash
hugo new posts/example-topic.md
```

文章 front matter 保持以下字段：

```yaml
title: "文章题目"
date: "2026-08-15T04:00:00+08:00"
draft: true
slug: "example-topic"
tags: []
categories: []
summary: ""
```

## 本地运行

需要先安装 Hugo Extended。

```bash
hugo server -D
```

## 部署

推送到 `main` 分支后，GitHub Actions 会构建 Hugo 并部署到 GitHub Pages。
