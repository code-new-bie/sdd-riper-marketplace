---
description: 整理需求上下文，替用户读资料并提炼细节
---

# Build Context Bundle

整理需求上下文，替用户读资料并提炼细节。

## 参数解析

从 `$ARGUMENTS` 解析：
- `directory`: 目录路径（必填）

如果 `$ARGUMENTS` 为空，询问用户要整理哪个目录的上下文。

## 执行步骤

1. 读取指定目录下的文件（文本/文档/图片）
2. 解析策略：best effort，不可解析文件进入 `Unparsed Sources`，不阻塞产出
3. 提取需求事实和约束，附来源引用
4. 根据复杂度选择输出级别：
   - `Lite`: `Source Index + Requirement Snapshot + Open Questions + Next Actions`
   - `Standard`: 完整需求事实、业务规则、验收标准、约束、冲突与歧义
5. 落盘到 `mydocs/context/YYYY-MM-DD_hh-mm_<task>_context_bundle.md`
6. 输出文件路径和关键事实摘要

## 输出格式

- 文件路径
- 关键事实（约束、业务规则、验收标准）
- 待确认项（Open Questions）