# Project Tree

```text
.
├── .github/
│   └── workflows/
│       └── hugo.yml
├── .gitignore
├── AGENTS.md
├── README.md
├── archetypes/
│   └── default.md
├── assets/
│   └── css/
│       └── main.css
├── content/
│   ├── _index.md
│   └── posts/
│       ├── _index.md
│       └── hello-hugo.md
├── hugo.toml
├── layouts/
│   ├── _default/
│   │   ├── baseof.html
│   │   ├── list.html
│   │   └── single.html
│   ├── index.html
│   └── partials/
│       ├── footer.html
│       ├── header.html
│       └── post-card.html
├── specs/
│   ├── prd.md
│   ├── project-tree.md
│   └── tasks.md
└── static/
```

## 目录说明

- `.github/workflows/`：GitHub Actions 工作流。
- `archetypes/`：Hugo 新文章模板。
- `assets/`：会被 Hugo Pipeline 处理的样式和资源。
- `content/`：博客内容。
- `layouts/`：自定义 Hugo 模板。
- `specs/`：需求、结构和任务记录。
- `static/`：原样复制到站点根目录的静态资源。
