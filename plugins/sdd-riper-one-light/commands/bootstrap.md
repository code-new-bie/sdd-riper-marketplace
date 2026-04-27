---
description: 轻量启动，快速形成 micro-spec 并明确核心目标
---

# Bootstrap (Light)

轻量启动，快速形成 micro-spec 并明确核心目标。

## 参数解析

从 `$ARGUMENTS` 解析：
- `task`: 任务描述（必填）

如果 `$ARGUMENTS` 为空，询问用户要处理的任务是什么。

## 执行步骤

1. 用模型自己的话复述任务理解
2. 明确本轮阶段性核心目标
3. 判断任务深度：
   - `zero`: 纯机械性改动，跳过 micro-spec
   - `fast`: 写 1-3 句 micro-spec
   - `standard`: 维护轻量 spec
   - `deep`: 补充分析与方案比较
4. 建立或更新最小 spec 并落盘到 `mydocs/micro_specs/` 或 `mydocs/specs/`
5. 写清 Done Contract（1-3 行）：
   - 什么算完成
   - 由什么证明
   - 哪些情况仍算未完成
6. 输出 checkpoint summary：
   - 当前理解
   - 核心目标
   - 下一步动作
   - 风险
   - 验证方式
7. 等待用户批准后再进入执行

## 输出格式

- Spec 文件路径
- Done Contract
- Checkpoint Summary
- Execution Approval: `Pending`