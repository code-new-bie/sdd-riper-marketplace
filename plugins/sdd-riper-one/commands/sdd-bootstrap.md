---
description: RIPER 启动命令，进入 Research 第一步并产出首版 spec
---

# SDD Bootstrap

RIPER 启动命令，进入 Research 第一步，同时完成 Pre-Research 收口。

## 参数解析

从 `$ARGUMENTS` 解析：
- `task`: 任务描述/需求（可以是口述、文档路径、聊天记录）

如果 `$ARGUMENTS` 为空，询问用户要处理的任务是什么。

## 执行步骤

1. 汇总用户输入 + 代码事实 + 历史资产（codemap/context/spec）
2. 检查是否存在 codemap 和 context bundle，如有则加载
3. 分析需求，识别冲突与歧义
4. 冲突处理：先落首版 spec 标记冲突，再给 `Option A/B` 和推荐决策
5. 形成首版研究结论：
   - Context Sources
   - Codemap Used
   - Research Findings
   - Open Questions
   - Next Actions
6. 落盘到 `mydocs/specs/YYYY-MM-DD_hh-mm_<TaskName>.md`
7. 输出 spec 摘要，等待用户下一步指令

## 输出格式

- Spec 文件路径
- 当前核心目标
- 待确认项
- 下一步动作建议