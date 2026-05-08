$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$sourceSkill = Join-Path $repoRoot "skills\smart-skill-user\SKILL.md"
$targetSkillDir = Join-Path $HOME ".agents\skills\smart-skill-user"
$targetSkill = Join-Path $targetSkillDir "SKILL.md"
$codexDir = Join-Path $HOME ".codex"
$agentsFile = Join-Path $codexDir "AGENTS.md"
$template = Join-Path $repoRoot "templates\global-codex-AGENTS.md"

if (!(Test-Path $sourceSkill)) {
    throw "Missing source skill: $sourceSkill"
}

New-Item -ItemType Directory -Force -Path $targetSkillDir | Out-Null
New-Item -ItemType Directory -Force -Path $codexDir | Out-Null

if (Test-Path $targetSkill) {
    Copy-Item $targetSkill "$targetSkill.bak" -Force
}
Copy-Item $sourceSkill $targetSkill -Force

$templateText = Get-Content -Raw -LiteralPath $template
if (Test-Path $agentsFile) {
    $existing = Get-Content -Raw -LiteralPath $agentsFile
    if ($existing -notmatch "Smart Skill Preflight") {
        Copy-Item $agentsFile "$agentsFile.bak" -Force
        Add-Content -LiteralPath $agentsFile -Value "`n$templateText"
    }
} else {
    Set-Content -LiteralPath $agentsFile -Value $templateText -NoNewline
}

Write-Host "Installed Smart Skill User."
Write-Host "Skill: $targetSkill"
Write-Host "Guidance: $agentsFile"
Write-Host "Restart Codex, then ask it to run Smart Skill Preflight before work."
