# Career Application OS

一个可复用、证据驱动的 Codex 求职 skill。先建立私有 Personal Evidence Vault，再复用证据完成职业探索、岗位分析、定制申请与面试准备。

本仓库只包含通用 skill 指令、空白模板和校验工具，不包含任何使用者的简历、联系方式、照片、公司内部资料或真实申请记录。

## 借鉴来源与致谢

本项目主要借鉴两个上游项目。它们已有的求职流程、事实约束和工作台设计不应被描述为本项目独创。

| 来源 | 借鉴与可选复用的内容 | 本仓库的集成方式 |
| --- | --- | --- |
| [ASu-skills](https://github.com/Hisn00w/ASu-skills)，作者 Hisn00w | 这是一组专项 skill，而非单一 skill：`job-match` 的岗位匹配，`great-resume` 的真实经历改写，`make-resume` 的可编辑简历与打印，`interview` 的证据驱动追问，`offer` 的进度管理，以及 `evidence-recap` 的证据复盘。 | 用 [ASu 集成映射](skills/career-application-os/integrations/asu-skills.md) 交接给已独立安装的专项 skill；不复制其完整流程或分发其源码、模板。 |
| [Tailor Job Application](https://github.com/ariasrsu/tailor-job-application-skill)，作者 ariasrsu | 单文件、无运行依赖的 HTML 求职工作台：集中呈现岗位分析、简历、求职材料、面试准备和投递记录，支持简历模板与打印。 | 用 [Tailor 集成映射](skills/career-application-os/integrations/tailor-job-application.md) 将整理好的事实与申请内容交给可选输出 skill；不分发上游渲染器、页面源码或资源。 |

Career Application OS 是围绕这些能力增加的持久知识层和工作流编排，不是两个上游项目的官方产品，也不表示上游作者为本项目背书。来源版本、许可检查结果与分发边界详见 [THIRD_PARTY.md](THIRD_PARTY.md)。

## 本项目新增与调整

以下是本项目相对于上述借鉴内容所做的组织、规则与发布调整，不表示上游完全没有相近能力：

1. **从单次求职任务变成可复用 Career OS。** 增加私有 Evidence Vault、证据索引、岗位卡、公司知识和申请目录；保留来源链接，多个 JD 复用同一条事实，不把每次简历改写存成一份新经历。
2. **调整默认路由和完成条件。** 完整 JD 默认 APPLICATION；只有明确“只分析 / 只研究”等才进入只读模式。岗位匹配是中间步骤，后续继续完成简历策略、简历、ATS、面试准备、决策和申请归档。
3. **把未知信息变成非阻塞确认清单。** 毕业时间、证书、地点意愿等未知信息标为 NEED_CONFIRMATION；可安全完成的部分继续，不用未知值冒充事实，也不因为一个字段缺失停止整个流程。
4. **细化事实与推断的使用边界。** 在上游真实性原则基础上，明确 VERIFIED / REFRAMED / INFERRED / PROJECT_TO_COMPLETE 四种状态、Conflict List 和责任边界；正式简历不自动采用推断或未完成项目。
5. **补充可编辑工作台的扩展规范。** 规定确认一次同步多处，以 Profile + 当前申请确认 + 简历版本为事实源，写回 Markdown 并先备份；手动删除自动填充 bullet 后不能在保存时重新补回。公开包提供的是 [扩展规范](skills/career-application-os/references/workspace-editing.md)，不是已经实现这些功能的完整网页服务。
6. **改成去个人化、可移植的发布包。** 使用中性的 skill 名称与运行时路径配置，提供不覆盖已有资料的空白 Vault 初始化、环境检查、隐私扫描，以及 11 项路由和 Vault 测试；不携带原使用者的数据、机器路径或历史授权。

## 核心行为

- 完整或明显可识别的 JD 默认进入 APPLICATION；用户明确要求“只分析 / 只研究 / 只是看看”时才进入只读模式。
- 未知候选人信息标为 NEED_CONFIRMATION，继续可以安全完成的步骤，不在 Job Match 后默认停止。
- 工作流覆盖 Role Analysis → Evidence Mapping → Resume Strategy → Tailored Resume → ATS Review → Interview Preparation → Application Decision → Application Folder。
- 使用 VERIFIED 和安全的 REFRAMED；INFERRED 只进入明确标记的增强草案，不虚构指标或夸大 ownership。
- 复用新鲜的岗位 / 公司分析，不重复研究；记录事实冲突而不自行选版本。
- 可选调用已安装的 ASu、Tailor 专项 skill。没有可选依赖时，披露限制并继续安全的本地步骤。
- 编辑器扩展规范支持集中确认、Markdown 写回、简历版本与备份；手动删除自动同步字段后，不得在保存时重新补回。

## 安装与开始使用

技能目录为 `skills/career-application-os/`。通过 Codex 的 skill-installer 从该仓库安装此路径，或将该文件夹放入当前运行环境支持的 skills 目录。结构参考 [官方 Build skills 文档](https://learn.chatgpt.com/docs/build-skills)。

调用名称：

```text
$career-application-os
初始化我的私有 Personal Evidence Vault。先整理证据，不生成简历。
```

仓库中的空白初始化工具也可单独运行（Python 3.10+）：

```text
python skills/career-application-os/scripts/init_vault.py --vault <your-private-vault>
python skills/career-application-os/scripts/check_career_os.py doctor --vault <your-private-vault>
```

Vault 位置按用户明确指定路径、`CAREER_OS_VAULT` 环境变量、当前项目的 `Career-OS` 目录依次解析。初始化只创建缺失文件，不覆盖已有内容。

## 编辑工作台与依赖

这是 skill 包，不是预装了候选人数据的求职网站。可编辑页面由当前环境中的输出能力生成或扩展。需要本地文件写回时，必须使用受约束的本地服务或明确支持的文件访问机制，不能把 localStorage 冒充为 Markdown 同步。

编辑器规范见 `references/workspace-editing.md`。ASu 和 Tailor 是可选独立依赖，不随此仓库分发；来源与范围见 [THIRD_PARTY.md](THIRD_PARTY.md)。当前项目未添加 LICENSE，许可条款可后续由维护者选择。

## 隐私与验证

建议将私有 Vault 放在本仓库之外。不要将真实应用、附件、证据、简历、照片、备份、凭据或机器专属配置提交到 Git。`.gitignore` 只是保护层之一，发布前仍需检查待提交文件和 Git 历史。

```text
python -m unittest discover -s skills/career-application-os/tests -v
python scripts/audit_public_package.py
```

公开发布包不携带旧用户的授权、姓名、电脑路径或历史记录；外部投递、提交表单、招聘方联系与发布仍以当前用户的具体请求为准。
