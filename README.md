# SDD-RIPER Marketplace

SDD-RIPER 方法论 Claude Code 插件集合，包含完整版与轻量版 AI Agent Harness。

## 插件列表

| 插件                    | 说明           | 适用场景                         |
| ----------------------- | -------------- | -------------------------------- |
| `sdd-riper-one`       | 完整版 Harness | 复杂重构、跨项目任务、审计、交接 |
| `sdd-riper-one-light` | 轻量版 Harness | 日常 coding、高频多轮任务        |

## 安装

### 1. 添加 Marketplace

```bash
# Add sdd-riper-marketplace
claude plugin marketplace add https://github.com/code-new-bie/sdd-riper-marketplace.git
```

### 2. 安装插件

```bash
# 安装完整版
claude plugin install sdd-riper-one@sdd-riper

# 安装轻量版
claude plugin install sdd-riper-one-light@sdd-riper
```

## 使用

### 加载 Skill（完整协议）

```text
# 完整版
/sdd-riper-one:sdd-riper-one

# 轻量版
/sdd-riper-one-light:sdd-riper-one-light
```

### 使用 Commands

#### sdd-riper-one 命令

| 命令                                          | 用途                      |
| --------------------------------------------- | ------------------------- |
| `/sdd-riper-one:create-codemap <scope>`     | 生成代码索引地图          |
| `/sdd-riper-one:build-context-bundle <dir>` | 整理需求上下文            |
| `/sdd-riper-one:sdd-bootstrap <task>`       | RIPER 启动，产出首版 spec |
| `/sdd-riper-one:review-spec`                | Spec 质量评审             |
| `/sdd-riper-one:review-execute`             | 执行后三轴评审            |
| `/sdd-riper-one:archive <targets>`          | 归档沉淀                  |

#### sdd-riper-one-light 命令

| 命令                                      | 用途                      |
| ----------------------------------------- | ------------------------- |
| `/sdd-riper-one-light:bootstrap <task>` | 轻量启动，形成 micro-spec |
| `/sdd-riper-one-light:checkpoint`       | 执行前 checkpoint         |
| `/sdd-riper-one-light:sync`             | 执行后回写 spec           |

### 推荐入口

**日常任务使用轻量版：**

```text
请使用 sdd-riper-one-light 处理这个任务。
先不要直接改代码，先给我：
- 你对任务的理解
- 本轮核心目标
- micro-spec
- Done Contract
- 下一步动作
我批准后再执行。
```

**复杂任务使用完整版：**

```text
请使用 sdd-riper-one 处理这个任务。
先运行 sdd-bootstrap 形成首版 spec，再进入 RIPER 流程。
```

## 快速测试（不安装）

```bash
# 测试完整版
claude --plugin-dir ./plugins/sdd-riper-one

# 测试轻量版
claude --plugin-dir ./plugins/sdd-riper-one-light
```

## 目录结构

```
sdd-riper-marketplace/
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   ├── sdd-riper-one/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── skills/sdd-riper-one/SKILL.md
│   │   ├── commands/ (6 files)
│   │   ├── references/ (7 files)
│   │   ├── agents/openai.yaml
│   │   ├── scripts/archive_builder.py
│   │   └── README.md
│   └── sdd-riper-one-light/
│       ├── .claude-plugin/plugin.json
│       ├── skills/sdd-riper-one-light/SKILL.md
│       ├── commands/ (3 files)
│       ├── references/ (3 files)
│       ├── examples/
│       ├── agents/openai.yaml
│       └── README.md
└── README.md
```

## 核心协议要点

### 硬约束（两个版本共有）

- `Spec is Truth`: spec 是唯一真相源
- `No Spec, No Code`: 未形成 spec 前不进入代码实现
- `No Approval, No Execute`: 未获批准不执行
- `Done by Evidence`: 完成由证据证明，不是模型宣布
- `Reverse Sync`: 执行后必须回写 spec

### 轻量版特点

- checkpoint-driven：强制校准点，不强制完整 phase 展开
- 自分解优先：模型自行拆解任务
- 短汇报：默认中文、短输出、按需加载深模块

### 完整版特点

- 显式 RIPER 状态机：Research → Innovate → Plan → Execute → Review
- 多项目支持：自动发现、作用域隔离、跨项目契约
- Debug 模式：日志驱动排查与功能验证

## 致谢

[](https://github.com/beforeload/sdd-riper-optimized#%E8%87%B4%E8%B0%A2)

* 原始仓库：[huisezhiyin/sdd-riper](https://github.com/huisezhiyin/sdd-riper/tree/main/skills)
