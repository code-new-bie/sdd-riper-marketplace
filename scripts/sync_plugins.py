#!/usr/bin/env python3
"""
同步 SDD-RIPER skills 到插件目录。

用法:
    python scripts/sync_plugins.py [--validate]

选项:
    --validate  同步后运行 claude plugin validate
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


# 项目根目录
ROOT = Path(__file__).parent.parent.parent

# 源目录
SRC_SKILLS = ROOT / "sdd-riper" / "skills"

# 目标目录
PLUGINS = ROOT / "sdd-riper-marketplace" / "plugins"


def sync_file(src: Path, dst: Path) -> bool:
    """同步单个文件"""
    if not src.exists():
        print(f"[WARN] Source not found: {src}")
        return False

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"[OK] {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")
    return True


def sync_sdd_riper_one() -> int:
    """同步 sdd-riper-one 插件"""
    plugin_dir = PLUGINS / "sdd-riper-one"
    src_dir = SRC_SKILLS / "sdd-riper-one"

    count = 0

    # SKILL.md
    if sync_file(
        src_dir / "SKILL.md",
        plugin_dir / "skills" / "sdd-riper-one" / "SKILL.md"
    ):
        count += 1

    # agents
    if sync_file(
        src_dir / "agents" / "openai.yaml",
        plugin_dir / "agents" / "openai.yaml"
    ):
        count += 1

    # scripts
    if sync_file(
        src_dir / "scripts" / "archive_builder.py",
        plugin_dir / "scripts" / "archive_builder.py"
    ):
        count += 1

    # references (7 files)
    refs_src = src_dir / "references"
    refs_dst = plugin_dir / "references"
    for ref_file in refs_src.glob("*.md"):
        if sync_file(ref_file, refs_dst / ref_file.name):
            count += 1

    # README
    if sync_file(
        src_dir / "README.md",
        plugin_dir / "README.md"
    ):
        count += 1

    return count


def sync_sdd_riper_one_light() -> int:
    """同步 sdd-riper-one-light 插件"""
    plugin_dir = PLUGINS / "sdd-riper-one-light"
    src_dir = SRC_SKILLS / "sdd-riper-one-light"

    count = 0

    # SKILL.md
    if sync_file(
        src_dir / "SKILL.md",
        plugin_dir / "skills" / "sdd-riper-one-light" / "SKILL.md"
    ):
        count += 1

    # agents
    if sync_file(
        src_dir / "agents" / "openai.yaml",
        plugin_dir / "agents" / "openai.yaml"
    ):
        count += 1

    # references (3 files)
    refs_src = src_dir / "references"
    refs_dst = plugin_dir / "references"
    for ref_file in refs_src.glob("*.md"):
        if sync_file(ref_file, refs_dst / ref_file.name):
            count += 1

    # examples/README.md
    if sync_file(
        src_dir / "examples" / "README.md",
        plugin_dir / "examples" / "README.md"
    ):
        count += 1

    # examples/codemap
    codemap_src = src_dir / "examples" / "codemap"
    codemap_dst = plugin_dir / "examples" / "codemap"
    for example_file in codemap_src.glob("*.md"):
        if sync_file(example_file, codemap_dst / example_file.name):
            count += 1

    # examples/specs
    specs_src = src_dir / "examples" / "specs"
    specs_dst = plugin_dir / "examples" / "specs"
    for example_file in specs_src.glob("*.md"):
        if sync_file(example_file, specs_dst / example_file.name):
            count += 1

    # README
    if sync_file(
        src_dir / "README.md",
        plugin_dir / "README.md"
    ):
        count += 1

    return count


def validate() -> bool:
    """运行 claude plugin validate"""
    marketplace_path = ROOT / "sdd-riper-marketplace"

    try:
        result = subprocess.run(
            ["claude", "plugin", "validate", str(marketplace_path)],
            capture_output=True,
            text=True,
            cwd=str(ROOT)
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result.returncode == 0
    except FileNotFoundError:
        print("[WARN] claude command not found, skipping validation")
        return True


def main() -> int:
    parser = argparse.ArgumentParser(description="同步 SDD-RIPER skills 到插件目录")
    parser.add_argument("--validate", action="store_true", help="同步后运行验证")
    args = parser.parse_args()

    print("=" * 50)
    print("Syncing SDD-RIPER plugins")
    print("=" * 50)

    # 同步 sdd-riper-one
    print("\n[sdd-riper-one]")
    count1 = sync_sdd_riper_one()
    print(f"Synced {count1} files")

    # 同步 sdd-riper-one-light
    print("\n[sdd-riper-one-light]")
    count2 = sync_sdd_riper_one_light()
    print(f"Synced {count2} files")

    # 总计
    total = count1 + count2
    print(f"\nTotal: {total} files synced")

    # 验证
    if args.validate:
        print("\n[Validation]")
        if validate():
            print("[OK] Validation passed")
        else:
            print("[FAIL] Validation failed")
            return 1

    print("\n[Done] Sync complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())