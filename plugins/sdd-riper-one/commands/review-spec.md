---
description: 在 Plan 完成后进行 spec 质量评审（建议性，不阻塞执行）
---

# Review Spec

在 `Plan` 完成后、`Execute` 前进行 spec 质量评审。

## 参数解析

从 `$ARGUMENTS` 解析：
- `spec`: spec 文件路径（可选，默认当前活跃 spec）
- `scope`: `plan_only`（默认）或 `full`

如果未指定 spec 路径，查找 `mydocs/specs/` 下最近更新的 spec。

## 执行步骤

1. 读取指定的 spec 文件
2. 评审重点（分阶段原则）：
   - 目标/范围/验收标准是否清晰且可验证
   - `Plan` 是否可执行（文件、签名、checklist 是否原子化）
   - 风险、回滚、跨项目契约（如有）是否充分
3. 对尚未到阶段的章节只做 `Reminder`，不计入 `NO-GO`
4. 输出评审矩阵：
   - Spec Review Matrix（逐项 `PASS/FAIL/PARTIAL` + 证据）
   - Readiness Verdict: `GO/NO-GO`（**建议性结论**）
   - Risks & Suggestions
   - Phase Reminders
5. 如为 `NO-GO` 且用户坚持执行，在 spec 记录 `User Decision: Proceed despite NO-GO`

## 约束

- `NO-GO` 不构成硬阻塞
- 用户选择继续时，必须记录决策

## 输出格式

- Review Matrix 表格
- Readiness Verdict
- Risks & Suggestions