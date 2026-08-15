# Tasks

## v1 - 可发布博客底座

状态：已完成。

目标：用最少自维护代码搭建可发布的 Hugo 博客，并通过 GitHub Pages 自动部署。

范围：

- [x] 创建 Hugo 基础配置 `hugo.toml`
- [x] 创建文章内容目录 `content/posts/`
- [x] 添加新文章模板 `archetypes/default.md`
- [x] 添加示例文章 `content/posts/hello-hugo.md`
- [x] 添加 Hugo `.gitignore`
- [x] 添加 GitHub Pages 部署工作流
- [x] 添加 `specs/` 项目规格文档目录
- [x] 添加 `AGENTS.md` 项目工作规则
- [x] 添加 README
- [x] 初始化 Git 仓库并创建中文提交
- [x] 创建 GitHub 公开仓库并推送 `main`
- [x] 设置 GitHub 仓库 description、homepage 和 topics
- [x] 启用 GitHub Pages，并通过 Actions 成功部署

架构约束：

- [x] 使用 PaperMod Hugo Module，不提交第三方主题源码
- [x] 删除自写 `layouts/` 和自写 CSS，避免维护主题已有能力
- [x] 使用 `go.mod` 和 `go.sum` 锁定主题依赖
- [x] 设置 `baseURL` 为 GitHub Pages 地址
- [x] 安装本地 Hugo，并把日常验证收敛到本地构建
- [x] 添加新文章脚本，自动生成唯一文件名和 slug

验收标准：

- [x] GitHub Actions 构建成功
- [x] GitHub Pages 部署成功
- [x] 本地 `hugo --gc --minify` 构建成功
- [x] 项目文件不包含本机绝对路径
- [x] 仓库当前工作区干净

## v2 - 正式内容与站点身份

状态：已完成。

目标：把博客从“可运行底座”推进到“可以长期写作和公开访问”的正式状态。

范围：

- [x] 使用正式站点名称 `Bill's Blog`
- [x] 使用正式作者名 `bill`
- [x] 根据正式名称同步更新 `hugo.toml` 和 README
- [x] 写入第一篇正式文章
- [x] 改写示例文章 `content/posts/hello-hugo.md`
- [x] 复查文章 front matter，确保标题、日期、slug、标签和摘要完整

验收标准：

- [x] 首页不再像脚手架示例
- [x] 第一批文章 URL 以题目 slug 为主，不使用日期路径
- [x] 同题文章通过自动生成的时间戳 slug 避免 URL 冲突
- [x] 本地 Hugo 构建成功

## v3 - 主题能力增强

状态：已完成。

目标：只在真实需要出现后，启用 PaperMod 已有能力；除非主题不能满足需求，否则不自写等价功能。

范围：

- [x] 添加 About 内容页
- [x] 启用 PaperMod 内置搜索
- [x] 使用 PaperMod 默认 404，不自写等价模板
- [x] 添加 About、搜索、标签和 GitHub 菜单项

验收标准：

- [x] 每个增强项都有明确使用场景
- [x] 优先通过 PaperMod 配置完成
- [x] 不新增自写模板，除非 specs 明确说明主题能力不足
