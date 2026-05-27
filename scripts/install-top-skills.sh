#!/usr/bin/env bash
# Installs the curated top 14 Claude / Claude Code skills documented in
# docs/TOP_SKILLS.md. Idempotent. Creates .bak backups before appending
# to existing files. Run with --dry-run to print actions without executing.
set -euo pipefail

DRY_RUN=0
SKIP_NPX=0
SKIP_MCP=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --skip-npx) SKIP_NPX=1 ;;
    --skip-mcp) SKIP_MCP=1 ;;
    -h|--help)
      cat <<'EOF'
install-top-skills.sh

Installs the curated top-14 skills from docs/TOP_SKILLS.md.

Flags:
  --dry-run    Print actions without executing
  --skip-npx   Skip npx-based installs (caveman, marketingskills, claude-mem,
               graphify, obsidian-second-brain)
  --skip-mcp   Skip MCP-based installs (claude-context)
  -h, --help   Show this help

What runs automatically:
  1.  juliusbrussee/caveman              - via npx skills
  2.  thedotmack/claude-mem               - via npx claude-mem install
  3.  coreyhaines31/marketingskills       - via npx skills
  4.  karpathy nanochat read-arxiv        - sparse git fetch into ~/.claude/skills
  11. safishamsi/graphify                 - via npx skills (with manual fallback)
  14. eugeniughelbur/obsidian-second-brain - via npx skills (with manual fallback)

What is printed for manual paste into Claude Code (slash commands cannot
be issued from a shell):
  5.  anthropics/knowledge-work-plugins (marketing)
  6.  AgriciDaniel/claude-seo
  7.  multica-ai/andrej-karpathy-skills
  8.  obra/superpowers
  12. AgriciDaniel/claude-blog
  13. AgriciDaniel/claude-ads
  9.  zilliztech/claude-context           - MCP server
 10.  SurgeGraph                          - external skill, manual install only
EOF
      exit 0
      ;;
  esac
done

run() {
  if [[ "$DRY_RUN" == "1" ]]; then
    printf 'DRY-RUN: %s\n' "$*"
  else
    printf '>>> %s\n' "$*"
    "$@"
  fi
}

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    return 1
  fi
}

claude_home="${CLAUDE_HOME:-$HOME/.claude}"
skills_dir="$claude_home/skills"
mkdir -p "$skills_dir"

echo "Claude home: $claude_home"
echo "Skills dir:  $skills_dir"
echo

# --- 1. juliusbrussee/caveman --------------------------------------------
if [[ "$SKIP_NPX" == "0" ]]; then
  require_cmd npx || exit 1
  echo "[1/14] juliusbrussee/caveman (verbosity cutter)"
  run npx -y skills add juliusbrussee/caveman --copy --yes
  echo
fi

# --- 2. thedotmack/claude-mem --------------------------------------------
if [[ "$SKIP_NPX" == "0" ]]; then
  echo "[2/14] thedotmack/claude-mem (persistent compressed memory)"
  run npx -y claude-mem install
  echo
fi

# --- 3. coreyhaines31/marketingskills ------------------------------------
if [[ "$SKIP_NPX" == "0" ]]; then
  echo "[3/14] coreyhaines31/marketingskills (32 marketing skills)"
  run npx -y skills add coreyhaines31/marketingskills --copy --yes
  echo
fi

# --- 4. karpathy nanochat read-arxiv-paper -------------------------------
echo "[4/14] karpathy/nanochat read-arxiv-paper (sparse git fetch)"
arxiv_dir="$skills_dir/read-arxiv-paper"
if [[ -d "$arxiv_dir" ]]; then
  echo "Already present at $arxiv_dir - skipping fetch."
else
  tmp_dir="$(mktemp -d)"
  if [[ "$DRY_RUN" == "1" ]]; then
    echo "DRY-RUN: clone karpathy/nanochat sparse into $tmp_dir then copy .claude/skills/read-arxiv-paper to $arxiv_dir"
  else
    (
      cd "$tmp_dir"
      git init -q
      git remote add origin https://github.com/karpathy/nanochat.git
      git config core.sparseCheckout true
      echo ".claude/skills/read-arxiv-paper/*" > .git/info/sparse-checkout
      git pull -q --depth=1 origin master || git pull -q --depth=1 origin main
    )
    if [[ -d "$tmp_dir/.claude/skills/read-arxiv-paper" ]]; then
      cp -R "$tmp_dir/.claude/skills/read-arxiv-paper" "$arxiv_dir"
      echo "Installed: $arxiv_dir"
    else
      echo "Sparse fetch returned no files; install manually from https://github.com/karpathy/nanochat" >&2
    fi
    rm -rf "$tmp_dir"
  fi
fi
echo

# --- 5-8, 12-13. /plugin marketplace + install ---------------------------
cat <<'EOF'
[5-8, 12-13/14] Paste this block into Claude Code (interactive). Slash
commands cannot be issued from a shell.

----- BEGIN CLAUDE-CODE-PASTE -----
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install marketing@anthropic-knowledge-work-plugins

/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@claude-seo

/plugin marketplace add multica-ai/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills

/plugin marketplace add obra/superpowers
/plugin install superpowers@claude-plugins-official

/plugin marketplace add AgriciDaniel/claude-blog
/plugin install claude-blog@claude-blog

/plugin marketplace add AgriciDaniel/claude-ads
/plugin install claude-ads@claude-ads
----- END CLAUDE-CODE-PASTE -----

EOF

# --- 9. zilliztech/claude-context (MCP) ----------------------------------
if [[ "$SKIP_MCP" == "0" ]]; then
  echo "[9/14] zilliztech/claude-context (MCP server, AST + hybrid retrieval)"
  if command -v claude >/dev/null 2>&1; then
    # Adding via the Claude Code CLI MCP manager. Requires the package to
    # be discoverable; if this fails, follow the README at:
    # https://github.com/zilliztech/claude-context
    cat <<'EOF'
Run on each machine where you use Claude Code:

  claude mcp add claude-context -- npx -y @zilliz/claude-context-mcp

Then configure the embedding + vector backend per:
  https://github.com/zilliztech/claude-context

EOF
  else
    echo "Claude Code CLI not detected; follow https://github.com/zilliztech/claude-context"
  fi
  echo
fi

# --- 10. SurgeGraph -------------------------------------------------------
cat <<'EOF'
[10/14] SurgeGraph Claude Code Skill (AI-citation tracking)
Install via SurgeGraph's account flow:
  https://surgegraph.io/claude-code-skill

(Manual only; no verified one-line installer at time of writing.)

EOF

# --- 11. safishamsi/graphify ---------------------------------------------
if [[ "$SKIP_NPX" == "0" ]]; then
  echo "[11/14] safishamsi/graphify (local code knowledge graph; 6.8-49x token cut)"
  run npx -y skills add safishamsi/graphify --copy --yes || \
    echo "If the above failed, install manually per https://github.com/safishamsi/graphify"
  echo
fi

# --- 14. eugeniughelbur/obsidian-second-brain ----------------------------
if [[ "$SKIP_NPX" == "0" ]]; then
  echo "[14/14] eugeniughelbur/obsidian-second-brain (cross-CLI Obsidian skill)"
  run npx -y skills add eugeniughelbur/obsidian-second-brain --copy --yes || \
    echo "If the above failed, install manually per https://github.com/eugeniughelbur/obsidian-second-brain"
  echo
fi

echo "Done."
echo
echo "Verification: open Claude Code in a project and run"
echo "  /skills list"
echo "to confirm the new skills are visible."
