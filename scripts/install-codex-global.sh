#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_skill="$repo_root/skills/smart-skill-user/SKILL.md"
target_skill_dir="$HOME/.agents/skills/smart-skill-user"
target_skill="$target_skill_dir/SKILL.md"
codex_dir="$HOME/.codex"
agents_file="$codex_dir/AGENTS.md"
template="$repo_root/templates/global-codex-AGENTS.md"

if [[ ! -f "$source_skill" ]]; then
  echo "Missing source skill: $source_skill" >&2
  exit 1
fi

mkdir -p "$target_skill_dir" "$codex_dir"

if [[ -f "$target_skill" ]]; then
  cp "$target_skill" "$target_skill.bak"
fi
cp "$source_skill" "$target_skill"

if [[ -f "$agents_file" ]]; then
  if ! grep -q "Smart Skill Preflight" "$agents_file"; then
    cp "$agents_file" "$agents_file.bak"
    printf "\n%s\n" "$(cat "$template")" >> "$agents_file"
  fi
else
  cp "$template" "$agents_file"
fi

echo "Installed Smart Skill User."
echo "Skill: $target_skill"
echo "Guidance: $agents_file"
echo "Restart Codex, then ask it to run Smart Skill Preflight before work."
