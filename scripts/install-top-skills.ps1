param(
    [switch]$DryRun,
    [switch]$SkipNpx,
    [switch]$SkipMcp
)

$ErrorActionPreference = "Stop"

function Invoke-Step($command) {
    if ($DryRun) {
        Write-Host "DRY-RUN: $command"
    } else {
        Write-Host ">>> $command"
        Invoke-Expression $command
    }
}

$claudeHome = if ($env:CLAUDE_HOME) { $env:CLAUDE_HOME } else { Join-Path $HOME ".claude" }
$skillsDir = Join-Path $claudeHome "skills"
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null

Write-Host "Claude home: $claudeHome"
Write-Host "Skills dir:  $skillsDir"
Write-Host ""

# npx skills add writes to the cwd's .claude/skills/ — switch to $HOME so
# installs land globally, not scoped to whatever repo you launched from.
Set-Location $HOME

# 1. caveman
if (-not $SkipNpx) {
    Write-Host "[1/13] juliusbrussee/caveman (verbosity cutter)"
    Invoke-Step "npx -y skills add juliusbrussee/caveman --copy --yes"
    Write-Host ""
}

# 2. claude-mem
if (-not $SkipNpx) {
    Write-Host "[2/13] thedotmack/claude-mem (persistent compressed memory)"
    Invoke-Step "npx -y claude-mem install"
    Write-Host ""
}

# 3. marketingskills
if (-not $SkipNpx) {
    Write-Host "[3/13] coreyhaines31/marketingskills (32 marketing skills)"
    Invoke-Step "npx -y skills add coreyhaines31/marketingskills --copy --yes"
    Write-Host ""
}

# 4. karpathy nanochat read-arxiv-paper
Write-Host "[4/13] karpathy/nanochat read-arxiv-paper (sparse git fetch)"
$arxivDir = Join-Path $skillsDir "read-arxiv-paper"
if (Test-Path $arxivDir) {
    Write-Host "Already present at $arxivDir - skipping fetch."
} else {
    $tmpDir = Join-Path ([System.IO.Path]::GetTempPath()) ("nanochat-" + [guid]::NewGuid().ToString("N").Substring(0,8))
    if ($DryRun) {
        Write-Host "DRY-RUN: clone karpathy/nanochat sparse to $tmpDir then copy read-arxiv-paper to $arxivDir"
    } else {
        New-Item -ItemType Directory -Force -Path $tmpDir | Out-Null
        Push-Location $tmpDir
        try {
            git init -q
            git remote add origin https://github.com/karpathy/nanochat.git
            git config core.sparseCheckout true
            ".claude/skills/read-arxiv-paper/*" | Out-File -FilePath ".git/info/sparse-checkout" -Encoding ascii
            $pullOk = $false
            try { git pull -q --depth=1 origin master; $pullOk = $true } catch {}
            if (-not $pullOk) { git pull -q --depth=1 origin main }
        } finally {
            Pop-Location
        }
        $src = Join-Path $tmpDir ".claude\skills\read-arxiv-paper"
        if (Test-Path $src) {
            Copy-Item -Recurse $src $arxivDir
            Write-Host "Installed: $arxivDir"
        } else {
            Write-Warning "Sparse fetch returned no files; install manually from https://github.com/karpathy/nanochat"
        }
        Remove-Item -Recurse -Force $tmpDir
    }
}
Write-Host ""

# 5-8, 12-13. plugin marketplace block
Write-Host "[5-8, 12-13/13] Paste into Claude Code (interactive). Slash commands cannot be issued from a shell."
Write-Host ""
Write-Host "----- BEGIN CLAUDE-CODE-PASTE -----"
Write-Host "/plugin marketplace add anthropics/knowledge-work-plugins"
Write-Host "/plugin install marketing@anthropic-knowledge-work-plugins"
Write-Host ""
Write-Host "/plugin marketplace add AgriciDaniel/claude-seo"
Write-Host "/plugin install claude-seo@claude-seo"
Write-Host ""
Write-Host "/plugin marketplace add multica-ai/andrej-karpathy-skills"
Write-Host "/plugin install andrej-karpathy-skills@karpathy-skills"
Write-Host ""
Write-Host "/plugin marketplace add obra/superpowers"
Write-Host "/plugin install superpowers@claude-plugins-official"
Write-Host ""
Write-Host "/plugin marketplace add AgriciDaniel/claude-blog"
Write-Host "/plugin install claude-blog@claude-blog"
Write-Host ""
Write-Host "/plugin marketplace add AgriciDaniel/claude-ads"
Write-Host "/plugin install claude-ads@claude-ads"
Write-Host "----- END CLAUDE-CODE-PASTE -----"
Write-Host ""

# 9. claude-context MCP
if (-not $SkipMcp) {
    Write-Host "[9/13] zilliztech/claude-context (MCP server)"
    Write-Host "Run on each machine where you use Claude Code:"
    Write-Host "  claude mcp add claude-context -- npx -y @zilliz/claude-context-mcp"
    Write-Host "Then configure embedding + vector backend per:"
    Write-Host "  https://github.com/zilliztech/claude-context"
    Write-Host ""
}

# 10. SurgeGraph
Write-Host "[10/13] SurgeGraph Claude Code Skill (AI-citation tracking)"
Write-Host "Install via SurgeGraph's account flow:"
Write-Host "  https://surgegraph.io/claude-code-skill"
Write-Host "(Manual only; no verified one-line installer at time of writing.)"
Write-Host ""

# 11. safishamsi/graphify
if (-not $SkipNpx) {
    Write-Host "[11/13] safishamsi/graphify (local code knowledge graph; 6.8-49x token cut)"
    try {
        Invoke-Step "npx -y skills add safishamsi/graphify --copy --yes"
    } catch {
        Write-Warning "If the above failed, install manually per https://github.com/safishamsi/graphify"
    }
    Write-Host ""
}

Write-Host "Done."
Write-Host "Verification: open Claude Code in a project and run /skills list."
