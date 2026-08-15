---
title: "博客底座搭建记录"
date: 2026-08-15T04:07:21-04:00
draft: false
slug: "20260815-040721"
tags: ["Hugo", "PaperMod", "GitHub Pages"]
categories: ["记录"]
summary: "记录这个博客从空目录到 Hugo、PaperMod 和 GitHub Pages 自动部署的基础搭建过程。"
---

这个博客的底座已经整理成一个尽量少自维护代码的 Hugo 项目。

最初版本曾经写过自定义模板和样式，但这会把导航、列表页、文章页、搜索、RSS、404 和移动端适配都变成长期维护成本。现在项目改为通过 Hugo Modules 引入 PaperMod，主题源码不进入仓库。

当前仓库只保留内容、配置、规格文档和部署工作流。文章 URL 以题目 slug 为主，日期只负责发布时间和排序。

本地验证使用 `hugo --gc --minify`。推送到 `main` 后，GitHub Actions 会构建并部署到 GitHub Pages。
