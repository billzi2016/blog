---
title: "博客底座搭建记录"
date: 2026-08-15T04:07:21-04:00
draft: false
slug: "20260815-040721"
tags: ["Hugo", "PaperMod", "GitHub Pages"]
categories: ["记录"]
summary: "记录这个博客从空目录到 Hugo、PaperMod 和 GitHub Pages 自动部署的基础搭建过程。"
---

这个博客的底座是一个 Hugo 项目，主题使用 PaperMod。

最初版本写过自定义模板和样式。后来改为通过 Hugo Modules 引入 PaperMod，由主题处理导航、列表页、文章页、搜索、RSS、404 和移动端适配。

当前仓库保留内容、配置、规格文档和部署工作流。文章标题用于阅读入口，URL 使用创建时生成的 slug，日期用于发布时间和排序。

本地验证使用 `hugo --gc --minify`。推送到 `main` 后，GitHub Actions 会构建并部署到 GitHub Pages。
