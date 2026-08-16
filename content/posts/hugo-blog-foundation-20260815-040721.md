---
title: "博客底座搭建记录"
date: 2026-08-15T04:07:21-04:00
draft: false
slug: "20260815-040721"
tags: ["Hugo", "PaperMod", "GitHub Pages"]
categories: ["记录"]
summary: "记录这个博客从空目录到 Hugo、PaperMod 和 GitHub Pages 自动部署的基础搭建过程。"
---

博客基于 Hugo 搭建，主题采用 PaperMod。

最初尝试过手写模板与样式，后改为通过 Hugo Modules 引入 PaperMod，将导航、列表页、文章页、搜索、RSS、404 与移动端适配交由主题维护。仓库内仅保留文章内容、配置文件、项目规格文档与 GitHub Actions 工作流。

在内容组织上，文章标题作为阅读入口，URL 标识由自动生成的 slug 保证唯一性，日期用于发布时间标识与排序。

开发流程中，本地构建验证采用 `hugo --gc --minify`。代码推送到 `main` 分支后，由 GitHub Actions 自动编译并部署至 GitHub Pages。

