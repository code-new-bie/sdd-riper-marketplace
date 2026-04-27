---
description: 执行后回写 spec，记录改动摘要、验证结果、下一轮目标
---

# Sync (Light)

执行后回写 spec，记录改动摘要、验证结果、下一轮目标。

## 参数解析

从 `$ARGUMENTS` 解析：
- `summary`: 改动摘要（可选，用于补充信息）

如果 `$ARGUMENTS` 为空，从实际改动推断摘要。

## 执行步骤

1. 检查当前活跃 spec 路径
2. 收集实际改动（文件、行为）
3. 执行验证：
   - Self-check: 代码自查
   - Static checks: lint/类型检查
   - Runtime/Test: 运行测试或手动验证
   - Human confirmation: 人工确认结果
4. 判断核心目标是否已由证据证明完成：
   - 若完成：写收尾结论
   - 若未完成：写剩余差距和下一轮目标
5. 回写 spec：
   - Change Log（决策/改动摘要）
   - Validation（验证结果）
   - Resume/Handoff（当前状态、下一步）
6. 输出同步摘要

## 输出格式

- Change Log 摘要
- Validation 结果
- 核心目标完成状态
- 下一轮目标或收尾结论