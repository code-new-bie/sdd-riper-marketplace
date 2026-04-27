---
description: 生成代码索引地图，用于后续按需加载代码上下文
---

# Create CodeMap

生成代码索引地图（CodeMap）。CodeMap 是代码上下文索引，用于后续按需加载，而不是每轮全仓扫描。

## 参数解析

从 `$ARGUMENTS` 解析：
- `scope`: 代码范围（建议明确，如功能名、模块名）
- `mode`: `feature`（默认）或 `project`

如果 `$ARGUMENTS` 为空，询问用户要生成哪个范围的 CodeMap。

## 执行步骤

1. 确定扫描范围（scope）
2. 选择模式：
   - `feature`: 关注入口、核心链路、依赖、风险
   - `project`: 关注架构层、核心模块、跨模块流程、外部依赖
3. 扫描指定范围的代码文件
4. 提取关键信息：
   - 入口点 / 核心逻辑
   - 数据模型 / 状态
   - 依赖关系
   - 风险点 / 复杂点
5. 生成索引文档，图示建议优先 Mermaid（受限可降级为结构化文字图）
6. 落盘到 `mydocs/codemap/YYYY-MM-DD_hh-mm_<scope>功能.md` 或 `mydocs/codemap/YYYY-MM-DD_hh-mm_<scope>项目总图.md`
7. 输出文件路径和摘要

## 输出格式

- 文件路径
- 关键索引摘要（入口、核心模块、依赖、风险）