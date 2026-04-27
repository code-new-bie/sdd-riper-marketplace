---
description: 对指定 spec/codemap 做归档沉淀，将中间产物提炼为可复用知识
---

# Archive

对指定 spec/codemap（或目录）做归档沉淀，将"中间产物"提炼为可复用知识。

## 参数解析

从 `$ARGUMENTS` 解析：
- `targets`: 文件或目录路径（支持多个，用空格或逗号分隔）
- `kind`: `spec` / `codemap` / `mixed`（默认 `mixed`）
- `audience`: `human` / `llm` / `both`（默认 `both`）
- `mode`: `snapshot`（单任务归档，默认）/ `thematic`（跨任务主题归档）
- `topic`: 归档主题名（可选，默认从 targets 推断）

如果 `$ARGUMENTS` 为空，询问用户要归档哪些文件。

## 执行步骤

1. 收集目标文件（扫描目录下的 .md 文件）
2. 按 kind 过滤：
   - `spec`: 仅 specs 目录或文件名含 spec
   - `codemap`: 仅 codemap 目录或文件名含 codemap/项目总图/功能
3. 检查活跃 spec 门禁：
   - 如有未完成 Review 的 spec，警告并要求用户确认
4. 加载所有目标文档内容
5. 提取关键内容：
   - `human` 输出：决策、成果、风险、汇报视角
   - `llm` 输出：约束、接口契约、代码触点、模式、后续参考视角
6. 合并重复点，标记冲突（不静默解决）
7. 附加 Trace to Sources 表格
8. 落盘归档文件：
   - `mydocs/archive/YYYY-MM-DD_hh-mm_<topic>_human.md`
   - `mydocs/archive/YYYY-MM-DD_hh-mm_<topic>_llm.md`
9. 输出归档文件路径

## 约束

- 默认只归档不删除原文件
- 删除/移动需用户显式授权
- 活跃 spec 需用户确认后才可归档

## 输出格式

- 归档文件路径（human/llm）
- 来源文件数量
- 关键结论摘要