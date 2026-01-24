# 反重力技能

[中文](README.zh-CN.md)\|[英语](README.md)

通过模块化的方式，赋予坐席特定领域的专业能力（如全栈开发、复杂逻辑规划、多媒体处理等）**技能**定义，使智能体能够像人类专家一样系统地解决复杂问题。

## 📂 目录结构

    .
    ├── .claude-plugin/    # Claude plugin configuration files (plugin.json, marketplace.json)
    ├── skills/             # Antigravity Skills library
    │   ├── skill-name/     # Individual skill directory
    │   │   ├── SKILL.md    # Core skill definition and Prompt (Required)
    │   │   ├── scripts/    # Scripts relied upon by the skill (Optional)
    │   │   ├── examples/   # Skill usage examples (Optional)
    │   │   └── resources/  # Templates and resources relied upon by the skill (Optional)
    ├── docs/               # User manual and documentation guides
    │   └── Antigravity_Skills_Manual.md  # User manual
    ├── spec/               # Specification documents
    ├── template/           # New skill template
    └── README.md

## 🔌兼容性

反重力技能遵循通用**SKILL.md**格式，并且可以与任何支持 Agentic Skills 的 AI 编码助手无缝协作：

| 工具名称（代理）       | 类型    | 兼容性  | 项目路径                | 全局路径                            |
| :------------- | :---- | :--- | :------------------ | :------------------------------ |
| **反重力**        | GOES  | ✅ 饱满 | `.agent/skills/`    | `~/.gemini/antigravity/skills/` |
| **克劳德·科德**     | 命令行界面 | ✅ 饱满 | `.claude/skills/`   | `~/.claude/skills/`             |
| **双子座命令行界面**   | 命令行界面 | ✅ 饱满 | `.gemini/skills/`   | `~/.gemini/skills/`             |
| **法典**         | 命令行界面 | ✅ 饱满 | `.codex/skills/`    | `~/.codex/skills/`              |
| **光标**         | GOES  | ✅ 饱满 | `.cursor/skills/`   | `~/.cursor/skills/`             |
| **GitHub 副驾驶** | 扩大    | ⚠️部分 | `.github/skills/`   | `~/.copilot/skills/`            |
| **开放代码**       | 命令行界面 | ✅ 饱满 | `.opencode/skills/` | `~/.config/opencode/skills/`    |
| **风帆冲浪**       | GOES  | ✅ 饱满 | `.windsurf/skills/` | `~/.codeium/windsurf/skills/`   |
| **带来**         | GOES  | ✅ 饱满 | `.trae/skills/`     | `~/.trae/skills/`               |

> [！提示!]大多数工具会自动发现以下方面的技能`.agent/skills/`。为了获得最大的兼容性，请克隆/复制到此目录中。

## 📖 快速入门

### 1. 准备技能库

首先，在本地克隆此存储库（建议将其放置在固定位置以供全局参考）：

```bash
git clone https://github.com/guanyang/antigravity-skills.git ~/antigravity-skills
```

### 2.安装技巧（Symlink法）

我们强烈建议使用**符号链接（Symlink）**用于安装，以便当您通过更新此存储库时`git pull`，所有工具都会自动同步最新功能。

#### 🔹方法A：项目级安装

仅启用当前项目的技能。在项目根目录中运行：

```bash
mkdir -p .agent/skills
ln -s ~/antigravity-skills/skills/* .agent/skills/
```

#### 🔹方法B：全局级别安装

默认情况下在所有项目中启用技能。根据工具运行相应的命令；常见示例：

| 工具名称       | 全局安装命令 (macOS/Linux)                                                                                         |
| :--------- | :----------------------------------------------------------------------------------------------------------- |
| **一般的**    | `mkdir -p ~/.agent/skills && ln -s ~/antigravity-skills/skills/* ~/.agent/skills/`                           |
| **克劳德·科德** | `mkdir -p ~/.claude/skills && ln -s ~/antigravity-skills/skills/* ~/.claude/skills/`                         |
| **反重力**    | `mkdir -p ~/.gemini/antigravity/skills && ln -s ~/antigravity-skills/skills/* ~/.gemini/antigravity/skills/` |
| **双子座**    | `mkdir -p ~/.gemini/skills && ln -s ~/antigravity-skills/skills/* ~/.gemini/skills/`                         |
| **法典**     | `mkdir -p ~/.codex/skills && ln -s ~/antigravity-skills/skills/* ~/.codex/skills/`                           |

#### 🔹方法C：Claude插件安装（仅限Claude代码）

如果您主要使用**克劳德·科德**，您可以通过插件市场一键安装（此方法会自动处理技能加载）：

```bash
# 1. Start Claude Code
# 2. Add the plugin marketplace
/plugin marketplace add guanyang/antigravity-skills

# 3. Install the plugin from the marketplace
/plugin install antigravity-skills@antigravity-skills
```

### 3. 使用技巧

进入`@[skill-name]`或者`/skill-name`在聊天框中调用它们，例如：

```text
/canvas-design Help me design a 16:9 blog cover about "Deep Learning"
```

### 4. 更多信息

-   **查看手册**：详细使用方法请参考[文档/Antigravity_Skills_Manual.en.md](docs/Antigravity_Skills_Manual.en.md).
-   **环境依赖**：部分技能依赖Python环境；请确保您的系统安装了必要的库（例如，`pdf2docx`,`pandas`， ETC。）。

## 🚀 综合技能

### 🎨 创意与设计

这些技能侧重于视觉表达、UI/UX 设计和艺术创作。

-   **`@[algorithmic-art]`**：使用 p5.js 代码创建算法和生成艺术。
-   **`@[canvas-design]`**：根据设计理念创建海报和艺术品（PNG/PDF 输出）。
-   **`@[frontend-design]`**：创建高质量、生产级的前端界面和 Web 组件。
-   **`@[ui-ux-pro-max]`**：专业的UI/UX设计智能，提供颜色、字体、布局等完整的设计方案。
-   **`@[web-artifacts-builder]`**：构建复杂的现代 Web 应用程序（基于 React、Tailwind、Shadcn/ui）。
-   **`@[theme-factory]`**：为文档、幻灯片、HTML 等生成匹配的主题。
-   **`@[brand-guidelines]`**：应用 Anthropic 的官方品牌设计规范（颜色、排版等）。
-   **`@[slack-gif-creator]`**：创建专为 Slack 优化的高品质动画 GIF。

### 🛠️ 开发与工程

这些技能涵盖了编码、测试、调试和代码审查的整个生命周期。

-   **`@[test-driven-development]`**：测试驱动开发（TDD）——在实现代码之前编写测试。
-   **`@[systematic-debugging]`**：用于解决错误、测试失败或异常行为的系统调试。
-   **`@[webapp-testing]`**：使用 Playwright 对本地 Web 应用程序进行交互式测试和验证。
-   **`@[receiving-code-review]`**：使用技术验证而不是盲目修改来处理代码审查反馈。
-   **`@[requesting-code-review]`**：在合并或完成之前主动启动代码审查以验证代码质量。
-   **`@[finishing-a-development-branch]`**：指导开发分支的完成（合并、PR、清理等）。
-   **`@[subagent-driven-development]`**：协调多个子代理并行执行独立的开发任务。

### 📄 文档和办公室

这些技能用于处理各种格式的专业文档和办公需求。

-   **`@[doc-coauthoring]`**：指导用户协作撰写结构化文档（提案、技术规范等）。
-   **`@[docx]`**：创建、编辑和分析 Word 文档。
-   **`@[xlsx]`**：创建、编辑和分析 Excel 电子表格（支持公式和图表）。
-   **`@[pptx]`**：创建和修改 PowerPoint 演示文稿。
-   **`@[pdf]`**：处理PDF文档，包括提取文本/表格、合并/拆分、填写表格。
-   **`@[internal-comms]`**：起草各类企业内部沟通文件（周报、公告、常见问题解答等）。
-   **`@[notebooklm]`**：查询 Google NotebookLM 笔记本以获得明确的、基于文档的答案。

### 📅 规划和工作流程

这些技能有助于优化工作流程、任务规划和执行效率。

-   **`@[brainstorming]`**：在开始任何工作之前进行头脑风暴，以澄清需求和设计。
-   **`@[writing-plans]`**：为复杂的多步骤任务编写详细的执行计划（规格）。
-   **`@[planning-with-files]`**：基于文件的计划系统（Manus 风格），适合复杂任务。
-   **`@[executing-plans]`**：通过检查点和审查机制执行现有的实施计划。
-   **`@[using-git-worktrees]`**：创建隔离的 Git 工作树以进行并行开发或任务切换。
-   **`@[verification-before-completion]`**：在宣布任务完成之前，运行验证命令以确保有具体证据。
-   **`@[using-superpowers]`**：引导用户发现并使用这些高级技能。

### 🧠 核心认知与架构

这些技能构建了代理的心理模型、记忆系统和上下文管理能力。

-   **`@[bdi-mental-states]`**：模拟智能体的信念-欲望-意图 (BDI) 模型。
-   **`@[memory-systems]`**：基于知识图或向量构建长期记忆和实体跟踪系统。
-   **`@[context-fundamentals]`**：理解和调试上下文窗口和注意力机制等基本问题。
-   **`@[context-optimization]`**：通过 KV 缓存或分区优化上下文效率以降低 Token 成本。
-   **`@[context-compression]`**：实施上下文压缩和摘要以处理长窗口限制。
-   **`@[context-degradation]`**：诊断并修复上下文退化问题，例如“迷失在中间”。
-   **`@[filesystem-context]`**：利用文件系统进行动态上下文卸载和管理。

### 📐系统设计与评估

这些技能侧重于人工智能系统的架构设计、工具构建和质量评估。

-   **`@[project-development]`**：LLM项目的全生命周期设计，包括任务模型匹配和管道架构。
-   **`@[tool-design]`**：设计高效、清晰的代理工具接口和MCP协议。
-   **`@[evaluation]`**：建立多维度的代理绩效评价体系和质量关卡。
-   **`@[advanced-evaluation]`**：实施先进的评估方法，例如法学硕士法官和成对比较。

### 🧩 系统扩展

这些技能使我能够扩展自己的能力边界。

-   **`@[mcp-builder]`**：构建MCP（模型上下文协议）服务器来连接外部工具和数据。
-   **`@[skill-creator]`**：创建新技能或更新现有技能以扩展我的知识库和工作流程。
-   **`@[writing-skills]`**：协助编写、编辑和验证技能文件的工具子集。
-   **`@[dispatching-parallel-agents]`**：将并行任务分派给多个智能体进行处理。
-   **`@[multi-agent-patterns]`**：设计先进的多代理协作模式，例如 Supervisor 或 Swarm。
-   **`@[hosted-agents]`**：构建和部署沙盒、持续运行的后台代理。

## 🌟 鸣谢与来源

本项目集成了以下优秀开源项目的核心思想或技能实现。尊重原作者：

-   **[人择技能](https://github.com/anthropic/skills)**：Anthropic 提供的官方 API 使用范例和技能定义参考。
-   **[UI/UX Pro Max 技能](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**：顶级UI/UX设计智能，提供色彩、布局等完整设计方案。
-   **[超能力](https://github.com/obra/superpowers)**：旨在为法学硕士提供“超能力”的工具包和工作流程灵感。
-   **[使用文件进行规划](https://github.com/OthmanAdi/planning-with-files)**：实现了 Manus 风格的基于文件的任务规划系统，以增强复杂任务的持久内存。
-   **[笔记本LM](https://github.com/PleasePrompto/notebooklm-skill)**：基于Google NotebookLM的知识检索和问答技能实现。
-   **[情境工程代理技能](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)**：深入的上下文工程技能，涵盖压缩、优化和降级处理。

## 📄 许可证

该项目是开源的[我的许可证](LICENSE).
