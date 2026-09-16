# 借鉴来源、可选集成与分发边界

本项目主要借鉴 ASu-skills 和 Tailor Job Application。这里记录来源和集成范围，避免将上游能力误认为本项目独创。两个上游项目均作为独立、可选安装的能力使用；本仓库不包含它们的 skill 源码、简历模板、渲染器、字体、照片或页面实现。

## 1. ASu-skills

- 作者：Hisn00w。
- 上游：[Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills)。
- 本次发布时检查的本地版本：[1657fa0](https://github.com/Hisn00w/ASu-skills/tree/1657fa0d6d53a4b7b6d74c3b7722d040c75ba248)。
- 借鉴内容：专项 skill 分工、岗位要求与真实证据匹配、经历改写、可编辑简历与打印、证据驱动面试追问、申请进度管理及证据复盘。
- 本项目的交接说明：[integrations/asu-skills.md](skills/career-application-os/integrations/asu-skills.md)。执行专项任务时读取实际安装版本的指令；上游仓库保持独立，不在本项目内修改。
- 许可检查：上述版本的根目录 [LICENSE](https://github.com/Hisn00w/ASu-skills/blob/1657fa0d6d53a4b7b6d74c3b7722d040c75ba248/LICENSE) 为 MIT，版权声明为 © 2026 Hisn00w。该许可属于上游，不是本项目自动采用的许可。未来如分发其代码，应检查并保留适用的上游版权与许可声明。

## 2. Tailor Job Application

- 作者：ariasrsu。
- 上游：[ariasrsu/tailor-job-application-skill](https://github.com/ariasrsu/tailor-job-application-skill)。
- 本次发布时检查的本地版本：[9830567](https://github.com/ariasrsu/tailor-job-application-skill/tree/98305675bf276928b18b46a35e08aa1937a79398)。
- 借鉴内容：一个无运行依赖的单文件 HTML 工作台，串联岗位分析、简历、求职材料、面试准备和投递记录，以及简历模板切换与打印设计。
- 本项目的交接说明：[integrations/tailor-job-application.md](skills/career-application-os/integrations/tailor-job-application.md)。上游负责可选工作台输出，本项目提供结构化事实、申请内容和增量编辑要求。
- 许可检查：上述本地版本未发现根目录 LICENSE，GitHub API 在检查时也未识别出许可。这不应被视为允许自由复制或再分发；使用不同版本前应重新检查上游条款，必要时向作者确认。此仓库没有分发其代码或页面模板。

## 本项目的改动与范围

本项目增加持久私有 Vault、索引优先检索、完整 JD 的 APPLICATION 默认路由、非阻塞未知信息、四类证据状态、冲突清单、完整申请归档，以及可移植初始化和校验工具。更完整的改动说明见 [README](README.md#本项目新增与调整)。

确认面板、Markdown 同步、简历版本编辑、删除保留与历史备份在此公开包中以扩展规范描述。具体页面和本地写回服务须在使用者的环境中生成或扩展；原使用者的私有工作台实现和申请数据不在分发范围内。

集成说明是能力交接与设计致谢，不是对上游项目的再许可，也不表示上游作者背书。真实性与证据驱动等相近原则在上游已有体现，本项目不将这些共同原则宣称为独创。

本项目尚未选择自身 LICENSE；上游 MIT 不会自动覆盖本项目或另一个上游项目。

## 其他参考

[官方 Build skills 文档](https://learn.chatgpt.com/docs/build-skills) 仅用于 skill 结构与安装说明，不作为第三个求职功能来源。生成的个人资料、简历、证据和申请记录应保存在使用者的私有 Vault 中，而非提交到本分发仓库。
