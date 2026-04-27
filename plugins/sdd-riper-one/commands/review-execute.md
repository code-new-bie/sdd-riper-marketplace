---
description: 在 Execute 后执行结构化三轴评审
---

# Review Execute

在 `Execute` 后执行结构化评审，输出可回写 spec 的审查结论。

## 参数解析

从 `$ARGUMENTS` 解析：
- `spec`: spec 文件路径（可选，默认当前活跃 spec）
- `scope`: `changed_only`（默认）或 `full`（全量评审）

如果未指定 spec 路径，查找 `mydocs/specs/` 下最近更新的 spec。

## 执行步骤

1. 读取 spec 和相关代码文件
2. 评审三轴（必须全部输出）：

   **轴 1: Spec 质量与目标达成**
   - spec 是否写清目标、范围、验收标准
   - 需求是否完成

   **轴 2: Spec-代码一致性**
   - 代码是否忠实执行 `Plan`（文件、签名、checklist、行为）
   - 检查未授权偏差

   **轴 3: 代码自身质量**
   - 正确性、鲁棒性、可维护性
   - 测试覆盖、关键风险

3. 输出 Review Matrix
4. 判断 Overall Verdict: `PASS/FAIL`
5. 记录 Blocking Issues 和 Plan-Execution Diff
6. 回写结论到 spec 的 `## 6. Review Verdict` 和 `## 7. Plan-Execution Diff`

## 门禁规则

- 轴 1 或轴 2 任一 `FAIL` → `Review FAIL`，回到 `Research/Plan`
- 轴 3 存在高风险问题 → `Review FAIL`，回到 `Plan`

## 输出格式

- Review Matrix 表格（三轴）
- Overall Verdict
- Blocking Issues
- Plan-Execution Diff