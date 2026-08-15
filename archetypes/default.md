---
# 意图：新文章默认模板；通过 `hugo new posts/文章名.md` 创建内容时自动填充这些字段。
# 维护原则：字段应和 specs/prd.md 的内容模型保持一致，不随意增加平行字段。
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: "{{ .Date }}"
draft: true
slug: "{{ .File.ContentBaseName }}"
tags: []
categories: []
summary: ""
---
