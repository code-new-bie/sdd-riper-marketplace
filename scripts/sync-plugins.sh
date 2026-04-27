#!/bin/bash
# 同步 SDD-RIPER skills 到插件目录
#
# 用法:
#   ./scripts/sync-plugins.sh [--validate]
#
# 选项:
#   --validate  同步后运行 claude plugin validate

set -e

# 项目根目录
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SRC_SKILLS="$ROOT/sdd-riper/skills"
PLUGINS="$ROOT/sdd-riper-marketplace/plugins"

echo "=============================================="
echo "Syncing SDD-RIPER plugins"
echo "=============================================="

# sdd-riper-one
echo ""
echo "[sdd-riper-one]"

SRC_ONE="$SRC_SKILLS/sdd-riper-one"
DST_ONE="$PLUGINS/sdd-riper-one"

cp "$SRC_ONE/SKILL.md" "$DST_ONE/skills/sdd-riper-one/" && echo "[OK] SKILL.md"
cp "$SRC_ONE/agents/openai.yaml" "$DST_ONE/agents/" && echo "[OK] agents/openai.yaml"
cp "$SRC_ONE/scripts/archive_builder.py" "$DST_ONE/scripts/" && echo "[OK] scripts/archive_builder.py"
cp "$SRC_ONE/references/"*.md "$DST_ONE/references/" && echo "[OK] references/*.md"
cp "$SRC_ONE/README.md" "$DST_ONE/" && echo "[OK] README.md"

# sdd-riper-one-light
echo ""
echo "[sdd-riper-one-light]"

SRC_LIGHT="$SRC_SKILLS/sdd-riper-one-light"
DST_LIGHT="$PLUGINS/sdd-riper-one-light"

cp "$SRC_LIGHT/SKILL.md" "$DST_LIGHT/skills/sdd-riper-one-light/" && echo "[OK] SKILL.md"
cp "$SRC_LIGHT/agents/openai.yaml" "$DST_LIGHT/agents/" && echo "[OK] agents/openai.yaml"
cp "$SRC_LIGHT/references/"*.md "$DST_LIGHT/references/" && echo "[OK] references/*.md"
cp "$SRC_LIGHT/examples/README.md" "$DST_LIGHT/examples/" && echo "[OK] examples/README.md"
cp "$SRC_LIGHT/examples/codemap/"*.md "$DST_LIGHT/examples/codemap/" && echo "[OK] examples/codemap/*.md"
cp "$SRC_LIGHT/examples/specs/"*.md "$DST_LIGHT/examples/specs/" && echo "[OK] examples/specs/*.md"
cp "$SRC_LIGHT/README.md" "$DST_LIGHT/" && echo "[OK] README.md"

echo ""
echo "[Done] Sync complete"

# 验证
if [ "$1" == "--validate" ]; then
    echo ""
    echo "[Validation]"
    claude plugin validate "$ROOT/sdd-riper-marketplace"
fi