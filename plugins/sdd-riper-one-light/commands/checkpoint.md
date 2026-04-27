---
description: 提交执行前 checkpoint，确认理解、目标、下一步、风险与验证方式
---

# Checkpoint (Light)

提交执行前 checkpoint，确认理解、目标、下一步、风险与验证方式。

## 参数解析

从 `$ARGUMENTS` 解析：
- `context`: 当前状态描述（可选，用于补充信息）

如果 `$ARGUMENTS` 为空，从当前 spec 和对话上下文推断状态。

## 执行步骤

1. 重读当前活跃 spec 的相关区块
2. 复述当前任务理解
3. 明确当前核心目标（是否变化）
4. 检查 Goal Alignment：
   - 当前动作是否仍服务于核心目标
   - 若有偏差，说明偏差在哪里
5. 输出 checkpoint summary：
   - 当前理解
   - 核心目标
   - 当前进度
   - 下一步 1-3 个动作
   - 涉及文件/模块
   - 风险
   - 验证方式
6. 等待用户明确批准（`Execution Approval: Pending` → `Approved`）

## 输出格式

- Checkpoint Summary（结构化）
- Execution Approval 状态