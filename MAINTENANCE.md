# 插件维护指南

本插件采用复制迁移方案，插件内容与 `sdd-riper/skills/` 源目录独立。当 SDD-RIPER 更新后，需要手动同步变更。

## 同步流程

### 自动同步（推荐）

运行同步脚本：

```bash
# Bash 环境
./scripts/sync-plugins.sh

# 或 Python 环境
python scripts/sync_plugins.py
```

### 手动同步

```bash
# 同步 sdd-riper-one
cp sdd-riper/skills/sdd-riper-one/SKILL.md sdd-riper-marketplace/plugins/sdd-riper-one/skills/sdd-riper-one/
cp sdd-riper/skills/sdd-riper-one/agents/openai.yaml sdd-riper-marketplace/plugins/sdd-riper-one/agents/
cp sdd-riper/skills/sdd-riper-one/scripts/archive_builder.py sdd-riper-marketplace/plugins/sdd-riper-one/scripts/
cp sdd-riper/skills/sdd-riper-one/references/*.md sdd-riper-marketplace/plugins/sdd-riper-one/references/
cp sdd-riper/skills/sdd-riper-one/README.md sdd-riper-marketplace/plugins/sdd-riper-one/

# 同步 sdd-riper-one-light
cp sdd-riper/skills/sdd-riper-one-light/SKILL.md sdd-riper-marketplace/plugins/sdd-riper-one-light/skills/sdd-riper-one-light/
cp sdd-riper/skills/sdd-riper-one-light/agents/openai.yaml sdd-riper-marketplace/plugins/sdd-riper-one-light/agents/
cp sdd-riper/skills/sdd-riper-one-light/references/*.md sdd-riper-marketplace/plugins/sdd-riper-one-light/references/
cp sdd-riper/skills/sdd-riper-one-light/examples/README.md sdd-riper-marketplace/plugins/sdd-riper-one-light/examples/
cp sdd-riper/skills/sdd-riper-one-light/examples/codemap/*.md sdd-riper-marketplace/plugins/sdd-riper-one-light/examples/codemap/
cp sdd-riper/skills/sdd-riper-one-light/examples/specs/*.md sdd-riper-marketplace/plugins/sdd-riper-one-light/examples/specs/
cp sdd-riper/skills/sdd-riper-one-light/README.md sdd-riper-marketplace/plugins/sdd-riper-one-light/
```

## 同步后验证

```bash
claude plugin validate sdd-riper-marketplace
```

## 变更类型与处理

| 变更类型 | 文件位置 | 处理方式 |
|---------|---------|---------|
| SKILL.md 协议变更 | skills/*/SKILL.md | 直接同步，可能需要更新版本号 |
| references 文档变更 | references/*.md | 直接同步 |
| 新增原生命令动作 | - | 需在 commands/ 创建对应 .md 文件 |
| agents 配置变更 | agents/openai.yaml | 直接同步 |
| 脚本变更 | scripts/*.py | 直接同步 |
| 示例变更 | examples/* | 直接同步 |

## 新增 Command 处理

如果 SDD-RIPER 新增了原生命令动作：

1. 参考 `sdd-riper-one/references/commands.md` 了解新命令定义
2. 在 `plugins/sdd-riper-one/commands/` 创建对应的 `.md` 文件
3. 文件格式：

```markdown
---
description: 命令用途描述
---

# 命令名称

## 参数解析

从 `$ARGUMENTS` 解析：...

## 执行步骤

1. ...
2. ...

## 输出格式

- ...
```

## 版本管理

### 版本号规则

遵循语义化版本（SemVer）：`MAJOR.MINOR.PATCH`

| 变更类型 | 版本更新 | 示例 |
|---------|---------|------|
| 核心协议重大变更 | MAJOR | 1.0.0 → 2.0.0 |
| 新增 command/reference | MINOR | 1.0.0 → 1.1.0 |
| 错误修复、文档修正 | PATCH | 1.0.0 → 1.0.1 |

### 更新版本号

编辑 `plugins/*/.claude-plugin/plugin.json`：

```json
{
  "name": "sdd-riper-one",
  "version": "1.1.0",  // 更新此字段
  ...
}
```

## 文件同步清单

### sdd-riper-one

```
源目录                                    目标目录
sdd-riper/skills/sdd-riper-one/    →    plugins/sdd-riper-one/

SKILL.md                          →    skills/sdd-riper-one/SKILL.md
agents/openai.yaml                →    agents/openai.yaml
scripts/archive_builder.py        →    scripts/archive_builder.py
references/*.md (7 files)         →    references/*.md
README.md                         →    README.md
```

### sdd-riper-one-light

```
源目录                                         目标目录
sdd-riper/skills/sdd-riper-one-light/    →    plugins/sdd-riper-one-light/

SKILL.md                          →    skills/sdd-riper-one-light/SKILL.md
agents/openai.yaml                →    agents/openai.yaml
references/*.md (3 files)         →    references/*.md
examples/README.md                →    examples/README.md
examples/codemap/*.md             →    examples/codemap/*.md
examples/specs/*.md               →    examples/specs/*.md
README.md                         →    README.md
```

## 注意事项

1. **Commands 文件不自动同步**：Commands 是根据 commands.md 手动创建的，新增命令需要手动处理
2. **plugin.json 不同步**：版本号需要手动更新
3. **marketplace.json 不同步**：描述和配置需要手动维护
4. **同步后验证**：每次同步后运行 `claude plugin validate` 确保无错误