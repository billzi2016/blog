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

验收标准：

- [x] GitHub Actions 构建成功
- [x] GitHub Pages 部署成功
- [x] 项目文件不包含本机绝对路径
- [x] 仓库当前工作区干净

## v2 - 正式内容与站点身份

状态：待做。

目标：把博客从“可运行底座”推进到“可以长期写作和公开访问”的正式状态。

范围：

- [ ] 确认正式站点名称，替换当前 `我的博客`
- [ ] 确认正式作者名，替换或保留当前 `bizi`
- [ ] 根据正式名称同步更新 `hugo.toml`、README 和 GitHub 仓库描述
- [ ] 写第一批正式文章
- [ ] 删除或改写示例文章 `content/posts/hello-hugo.md`
- [ ] 复查文章 front matter，确保标题、日期、slug、标签和摘要完整

验收标准：

- [ ] 首页不再像脚手架示例
- [ ] 第一批文章 URL 以题目 slug 为主，不使用日期路径
- [ ] Actions 构建和 Pages 部署成功

## v3 - 主题能力增强

状态：待评估。

目标：只在真实需要出现后，启用 PaperMod 已有能力；除非主题不能满足需求，否则不自写等价功能。

范围：

- [ ] 评估是否需要 About 内容页
- [ ] 评估是否启用 PaperMod 内置搜索
- [ ] 评估是否需要自定义 404
- [ ] 评估是否需要额外菜单项或社交链接

验收标准：

- [ ] 每个增强项都有明确使用场景
- [ ] 优先通过 PaperMod 配置完成
- [ ] 不新增自写模板，除非 specs 明确说明主题能力不足
