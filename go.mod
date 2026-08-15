// 意图：声明 Hugo Modules 的模块身份，让主题依赖由 Hugo/Go 工具链管理。
// 维护原则：主题用 module 引入，不把第三方主题源码复制进仓库，减少长期维护负担。

module github.com/billzi2016/blog

go 1.25.0
