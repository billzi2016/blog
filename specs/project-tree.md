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
├── content/
│   ├── about.md
│   ├── _index.md
│   ├── search.md
│   └── posts/
│       ├── _index.md
│       └── hello-hugo.md
├── go.mod
├── hugo.toml
├── specs/
│   ├── prd.md
│   ├── project-tree.md
│   └── tasks.md
├── scripts/
│   └── new-post.sh
```

## 目录说明

- `.github/workflows/`：GitHub Actions 工作流。
- `archetypes/`：Hugo 新文章模板。
- `content/`：博客内容。
- `go.mod`：Hugo Modules 入口，用来引入 PaperMod 主题。
- `specs/`：需求、结构和任务记录。
