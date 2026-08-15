---
# 意图：新文章默认模板；通过脚本或 `hugo new` 创建内容时自动填充这些字段。
# 维护原则：slug 默认带创建时间，避免同一天写同题文章时 URL 冲突。
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: "{{ .Date }}"
draft: true
slug: "{{ .Date.Format "20060102-150405" }}-{{ .File.ContentBaseName }}"
tags: []
categories: []
summary: ""
---
