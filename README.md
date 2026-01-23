# Antigravity Skills

通过模块化的 **Skills** 定义，赋予 Agent 在特定领域的专业能力（如全栈开发、复杂逻辑规划、多媒体处理等），让 Agent 能够像人类专家一样系统性地解决复杂问题。

## 📂 目录结构 (Directory Structure)

```
.
├── skills/             # Antigravity Skills 技能库
│   ├── skill-name/     # 独立技能目录
│   │   ├── SKILL.md    # 技能核心定义与Prompt（必须）
│   │   ├── scripts/    # 技能依赖的脚本（可选）
│   │   ├── examples/   # 技能使用示例（可选）
│   │   └── resources/  # 技能依赖的模板与资源（可选）
├── docs/               # 用户手册与文档指南
│   └── Antigravity_Skills_Manual_CN.md  # 中文使用手册
├── spec/               # 规范文档
├── template/           # 新技能模板
└── README.md
```

## 🔌 兼容性 (Compatibility)

Antigravity Skills 遵循通用的 **SKILL.md** 格式，可与任何支持 Agentic Skills 的 AI 编码助手协同工作：

| 工具名称 (Agent) | 类型 | 兼容性 | 项目路径 (Project Path) | 全局路径 (Global Path) |
| :--- | :--- | :--- | :--- | :--- |
| **Antigravity** | IDE | ✅ Full | `.agent/skills/` | `~/.gemini/antigravity/skills/` |
| **Claude Code** | CLI | ✅ Full | `.claude/skills/` | `~/.claude/skills/` |
| **Gemini CLI** | CLI | ✅ Full | `.gemini/skills/` | `~/.gemini/skills/` |
| **Codex** | CLI | ✅ Full | `.codex/skills/` | `~/.codex/skills/` |
| **Cursor** | IDE | ✅ Full | `.cursor/skills/` | `~/.cursor/skills/` |
| **GitHub Copilot** | Extension| ⚠️ Partial | `.github/skills/` | `~/.copilot/skills/` |
| **OpenCode** | CLI | ✅ Full | `.opencode/skills/` | `~/.config/opencode/skills/` |
| **Windsurf** | IDE | ✅ Full | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| **Trae** | IDE | ✅ Full | `.trae/skills/` | `~/.trae/skills/` |

> [!TIP]
> 大多数工具都会自动发现 `.agent/skills/` 中的技能。为了获得最大兼容性，请克隆/复制到此目录。

## 📖 快速开始 (Quick Start)

### 1. 准备技能库
首先将本仓库克隆到本地（建议放在一个固定位置以便全局引用）：
```bash
git clone https://github.com/guanyang/antigravity-skills.git ~/antigravity-skills
```

### 2. 安装技能 (Symlink 方式)
我们强烈建议使用 **符号链接 (Symlink)** 进行安装，这样当你通过 `git pull` 更新本仓库时，所有工具都能自动同步最新功能。

#### 🔹 方案 A：项目级安装 (Project Level)
仅在当前项目启用技能。在你的项目根目录下运行：
```bash
mkdir -p .agent/skills
ln -s ~/antigravity-skills/skills/* .agent/skills/
```

#### 🔹 方案 B：全局安装 (Global Level)
在所有项目中默认启用技能。根据不同工具运行对应命令，给出部分示例：

| 工具名称 | 全局安装命令 (macOS/Linux) |
| :--- | :--- |
| **通用** | `mkdir -p ~/.agent/skills && ln -s ~/antigravity-skills/skills/* ~/.agent/skills/` |
| **Claude Code** | `mkdir -p ~/.claude/skills && ln -s ~/antigravity-skills/skills/* ~/.claude/skills/` |
| **Antigravity** | `mkdir -p ~/.gemini/antigravity/skills && ln -s ~/antigravity-skills/skills/* ~/.gemini/antigravity/skills/` |
| **Gemini** | `mkdir -p ~/.gemini/skills && ln -s ~/antigravity-skills/skills/* ~/.gemini/skills/` |
| **Codex** | `mkdir -p ~/.codex/skills && ln -s ~/antigravity-skills/skills/* ~/.codex/skills/` |

#### 🔹 方案 C：Claude Plugin 安装 (Claude Code 专用)
如果你主要使用 **Claude Code**，可以通过插件市场一键安装（该方式会自动处理技能加载）：

```bash
# 1. 启动 Claude Code
# 2. 添加插件市场
/plugin marketplace add guanyang/antigravity-skills

# 3. 从市场安装插件
/plugin install antigravity-skills@antigravity-skills
```

### 3. 使用技能
在对话框中输入 `@[skill-name]` 或 `/skill-name` 即可调用，例如：
```text
/canvas-design 帮我设计一张关于“Deep Learning”的博客封面，尺寸 16:9
```

### 4. 更多信息
- **查看手册**: 详细用法请查阅 [docs/Antigravity_Skills_Manual_CN.md](docs/Antigravity_Skills_Manual_CN.md)。
- **环境依赖**: 部分技能依赖 Python 环境，请确保系统已安装必要的库（如 `pdf2docx`, `pandas` 等）。


## 🚀 已集成的 Skills

### 🎨 创意与设计 (Creative & Design)
这些技能专注于视觉表现、UI/UX 设计和艺术创作。
- **`@[algorithmic-art]`**: 使用 p5.js 代码创作算法艺术、生成艺术
- **`@[canvas-design]`**: 基于设计哲学创建海报、艺术作品（输出 PNG/PDF）
- **`@[frontend-design]`**: 创建高质量、生产级的各种前端界面和 Web 组件
- **`@[ui-ux-pro-max]`**: 专业的 UI/UX 设计智能，提供配色、字体、布局等全套设计方案
- **`@[web-artifacts-builder]`**: 构建复杂、现代化的 Web 应用（基于 React, Tailwind, Shadcn/ui）
- **`@[theme-factory]`**: 为文档、幻灯片、HTML 等生成配套的主题风格
- **`@[brand-guidelines]`**: 应用 Anthropic 官方品牌设计规范（颜色、排版等）
- **`@[slack-gif-creator]`**: 制作专用于 Slack 的高质量 GIF 动图

### 🛠️ 开发与工程 (Development & Engineering)
这些技能涵盖了编码、测试、调试和代码审查的全生命周期。
- **`@[test-driven-development]`**: 测试驱动开发（TDD），在编写实现代码前先编写测试
- **`@[systematic-debugging]`**: 系统化调试，用于解决 Bug、测试失败或异常行为
- **`@[webapp-testing]`**: 使用 Playwright 对本地 Web 应用进行交互测试和验证
- **`@[receiving-code-review]`**: 处理代码审查反馈，进行技术验证而非盲目修改
- **`@[requesting-code-review]`**: 主动发起代码审查，在合并或完成任务前验证代码质量
- **`@[finishing-a-development-branch]`**: 引导开发分支的收尾工作（合并、PR、清理等）
- **`@[subagent-driven-development]`**: 协调多个子 Agent 并行执行独立的开发任务

### 📄 文档与办公 (Documentation & Office)
这些技能用于处理各种格式的专业文档和办公需求。
- **`@[doc-coauthoring]`**: 引导用户进行结构化文档（提案、技术规范等）的协作编写
- **`@[docx]`**: 创建、编辑和分析 Word 文档
- **`@[xlsx]`**: 创建、编辑和分析 Excel 电子表格（支持公式、图表）
- **`@[pptx]`**: 创建和修改 PowerPoint 演示文稿
- **`@[pdf]`**: 处理 PDF 文档，包括提取文本、表格，合并/拆分及填写表单
- **`@[internal-comms]`**: 起草各类企业内部沟通文档（周报、通告、FAQ 等）
- **`@[notebooklm]`**: 查询 Google NotebookLM 笔记本，提供基于文档的确切答案

### 📅 计划与流程 (Planning & Workflow)
这些技能帮助优化工作流、任务规划和执行效率。
- **`@[brainstorming]`**: 在开始任何工作前进行头脑风暴，明确需求和设计
- **`@[writing-plans]`**: 为复杂的多步骤任务编写详细的执行计划（Spec）
- **`@[planning-with-files]`**: 适用于复杂任务的文件式规划系统（Manus-style）
- **`@[executing-plans]`**: 执行已有的实施计划，包含检查点和审查机制
- **`@[using-git-worktrees]`**: 创建隔离的 Git 工作树，用于并行开发或任务切换
- **`@[verification-before-completion]`**: 在声明任务完成前运行验证命令，确保证据确凿
- **`@[using-superpowers]`**: 引导用户发现和使用这些高级技能

### 🧠 核心认知与架构 (Core Cognition & Architecture)
这些技能构建了 Agent 的思维模型、记忆系统和上下文管理能力。
- **`@[bdi-mental-states]`**: 模拟 Agent 的信念(Belief)、愿望(Desire)和意图(Intention)模型
- **`@[memory-systems]`**: 构建基于知识图谱或向量的长期记忆与实体追踪系统
- **`@[context-fundamentals]`**: 理解和调试上下文窗口、注意力机制等基础问题
- **`@[context-optimization]`**: 优化上下文效率，通过 KV-cache 或分区降低 Token 成本
- **`@[context-compression]`**: 实施上下文压缩与摘要，应对长窗口限制
- **`@[context-degradation]`**: 诊断和修复"迷失中间"等上下文退化问题
- **`@[filesystem-context]`**: 利用文件系统进行动态上下文卸载与管理

### 📐 系统设计与评估 (System Design & Evaluation)
这些技能专注于 AI 系统的架构设计、工具构建和质量评估。
- **`@[project-development]`**: LLM 项目全生命周期设计，包括任务-模型匹配与管道架构
- **`@[tool-design]`**: 设计高效、清晰的 Agent 工具接口与 MCP 协议
- **`@[evaluation]`**: 建立多维度的 Agent 性能评估体系与质量门禁
- **`@[advanced-evaluation]`**: 实施 LLM-as-a-Judge、成对比较等高阶评估方法

### 🧩 系统扩展 (System Extension)
这些技能允许我扩展自身的能力边界。
- **`@[mcp-builder]`**: 构建 MCP (Model Context Protocol) 服务器，连接外部工具和数据
- **`@[skill-creator]`**: 创建新技能或更新现有技能，扩展我的知识库和工作流
- **`@[writing-skills]`**: 辅助编写、编辑和验证技能文件的工具集
- **`@[dispatching-parallel-agents]`**: 分发并行任务给多个 Agent 处理
- **`@[multi-agent-patterns]`**: 设计 Supervisor、Swarm 等高级多 Agent 协作模式
- **`@[hosted-agents]`**: 构建和部署沙盒化、持久运行的后台 Agent

## 🌟 致谢与来源 (Credits & Sources)

本项目集成了以下优秀开源项目的核心思想或 Skill 实现，向原作者致敬：

- **[Anthropic Skills](https://github.com/anthropic/skills)**: Anthropic 官方提供的 API 使用范式与技能定义参考。
- **[UI/UX Pro Max Skills](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**: 顶级的 UI/UX 设计智能，提供配色、布局等全套设计方案参考。
- **[Superpowers](https://github.com/obra/superpowers)**: 旨在赋予 LLM "超能力" 的工具集与工作流启发。
- **[Planning with Files](https://github.com/OthmanAdi/planning-with-files)**: 实现类似 Manus 的文件式任务规划系统，提升复杂任务的持久化记忆。
- **[NotebookLM](https://github.com/PleasePrompto/notebooklm-skill)**: 基于 Google NotebookLM 的知识检索与问答技能实现。
- **[Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)**: 深入的上下文工程（Context Engineering）技能，涵盖压缩、优化与降级处理。

## 📄 开源协议 (License)

本项目采用 [MIT License](LICENSE) 协议开源。

