# 更新日志

本项目的所有重要变更都将记录在此文件中。

## [v2.0.2] - 2026-01-23
### 变更 (Changed)
- **目录结构优化**: 将技能库从 `.agent/skills` 移至根目录 `skills/`，并重新组织了 `docs/`、`spec/` 和 `template/` 目录。
- **文档全面改版**:
  - 更新 `README.md` 以匹配新的目录结构。
  - 在“快速开始”中引入 **Symlink (符号链接)** 安装方案，支持项目级与全局级安装。
  - 完善 **兼容性 (Compatibility)** 模块，支持多款 AI 工具（Claude, Gemini, Cursor, Windsurf, Trae 等）的路径规范。
  - 更新致谢部分 (Credits & Sources) 并增加描述说明。

### 新增 (Added)
- **技能索引文件**: 自动生成 `skills_index.json`，汇总全量 46 个技能的元数据（ID、路径、名称、描述）。
- **多工具支持**: 显式支持 GitHub Copilot、Windsurf、Trae 等 IDE 的技能加载。

### 修复 (Fixed)
- 更新了 `.gitignore`，防止 AI 助手运行目录（如 `.agent`, `.claude` 等）被误提交。

## [v2.0.1] - 2026-01-15
### 新增 (Added)
- **13 个高级认知与系统技能**:
  - **核心认知**: `bdi-mental-states` (BDI认知模型), `memory-systems` (记忆系统), `filesystem-context` (文件系统上下文)
  - **上下文工程**: `context-fundamentals` (基础), `context-optimization` (优化), `context-compression` (压缩), `context-degradation` (退化处理)
  - **高级代理**: `multi-agent-patterns` (多Agent模式), `hosted-agents` (托管Agent)
  - **系统设计与评估**: `tool-design` (工具设计), `project-development` (项目开发), `evaluation` (基础评估), `advanced-evaluation` (高级评估)

## [v2.0.0] - 2026-01-14
### 发布 (Released)
- **Antigravity 原生技能支持**: 建立 Antigravity 原生技能架构的重大版本发布。
- **核心库**: 确立了 33 个基础技能，覆盖创意设计、工程开发、文档处理和任务规划四大领域。

## [v1.0.0] - 2026-01-14
### 发布 (Released)
- **工作流标准支持**: 基于 Antigravity 工作流标准建立的初步技能支持。
- **核心库**: 确立了 33 个基础技能，覆盖创意设计、工程开发、文档处理和任务规划四大领域。