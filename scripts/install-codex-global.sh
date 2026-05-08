#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_skill="$repo_root/skills/smart-skill-user/SKILL.md"
target_skill_dir="$HOME/.agents/skills/smart-skill-user"
target_skill="$target_skill_dir/SKILL.md"
codex_dir="$HOME/.codex"
agents_file="$codex_dir/AGENTS.md"
template="$repo_root/templates/global-codex-AGENTS.md"
verification_prompt="Before doing anything, list the instruction sources and skills you loaded. Then run Smart Skill Preflight for this task: update a mobile homepage hero. Do not edit files."

if [[ ! -f "$source_skill" ]]; then
  echo "Missing source skill: $source_skill" >&2
  exit 1
fi

mkdir -p "$target_skill_dir" "$codex_dir"

if [[ -f "$target_skill" ]]; then
  cp "$target_skill" "$target_skill.bak"
  echo "Backup created: $target_skill.bak"
fi
cp "$source_skill" "$target_skill"

if [[ -f "$agents_file" ]]; then
  if ! grep -q "Smart Skill Preflight" "$agents_file"; then
    cp "$agents_file" "$agents_file.bak"
    echo "Backup created: $agents_file.bak"
    printf "\n%s\n" "$(cat "$template")" >> "$agents_file"
  else
    echo "Smart Skill Preflight already found in $agents_file; no duplicate insertion needed."
  fi
else
  cp "$template" "$agents_file"
fi

echo "Installed Smart Skill User."
echo "Skill: $target_skill"
echo "Guidance: $agents_file"
echo "Restart Codex, then paste this verification prompt:"
echo "$verification_prompt"
