# Career Application OS

一个可复用、证据驱动的 Codex 求职 skill。先建立私有 Personal Evidence Vault，再复用证据完成职业探索、岗位分析、定制申请与面试准备。

本仓库只包含通用 skill 指令、空白模板和校验工具，不包含任何使用者的简历、联系方式、照片、公司内部资料或真实申请记录。

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
