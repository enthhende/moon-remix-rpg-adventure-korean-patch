[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$Bin,

    [Parameter(Position = 1)]
    [string]$Cue
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)

$ExpectedBinName = "Moon - Remix RPG Adventure (Japan) (Rev 1).bin"
$ExpectedCueName = "Moon - Remix RPG Adventure (Japan) (Rev 1).cue"
$ExpectedInputSize = 640491936
$ExpectedInputSha256 = "828189dd7cba0211585c9e06a99936924f0fb883da428525f1fc73790fb403f2"
$ExpectedCueSize = 108
$ExpectedCueSha256 = "031a35316b96460c474e3a6a99bd2dfb98e6408dedd8ceadffc49faf20d77482"
$PatchName = "moon_ps1_kr_v1.0_rev1_70a8a7d2.xdelta"
$ExpectedPatchSize = 277452
$ExpectedPatchSha256 = "1c4c54c63e944ed0b5baabc0d8bc759568e2d7ab400554945b16f81e0257de10"
$ExpectedOutputSize = 640491936
$ExpectedOutputSha256 = "70a8a7d27ff38e0dba186fd88e9040d44c06221086d7d44dba633b6deeb661b3"
$ExpectedXdeltaSize = 336896
$ExpectedXdeltaSha256 = "53d90226615f217d3380c39892833311b4e24acd863e1ca01f14b5e772e2e6d0"

function Normalize-UserPath {
    param([string]$Value)
    if ([string]::IsNullOrWhiteSpace($Value)) {
        return $null
    }
    return $Value.Trim().Trim('"')
}

function Get-RequiredPath {
    param(
        [string]$CurrentValue,
        [string]$Prompt
    )
    $Value = Normalize-UserPath $CurrentValue
    if ([string]::IsNullOrWhiteSpace($Value)) {
        $Value = Normalize-UserPath (Read-Host $Prompt)
    }
    if ([string]::IsNullOrWhiteSpace($Value)) {
        throw "A required file path was not provided."
    }
    return [System.IO.Path]::GetFullPath($Value)
}

function Assert-ExactFile {
    param(
        [string]$Path,
        [string]$Label,
        [long]$ExpectedSize,
        [string]$ExpectedSha256
    )
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "${Label} was not found: $Path"
    }
    $File = Get-Item -LiteralPath $Path
    if ($File.Length -ne $ExpectedSize) {
        throw "${Label} size mismatch. Expected $ExpectedSize bytes, got $($File.Length) bytes."
    }
    $ActualSha256 = (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($ActualSha256 -ne $ExpectedSha256) {
        throw "${Label} SHA-256 mismatch.`nExpected: $ExpectedSha256`nActual:   $ActualSha256"
    }
}

function Find-BundledFile {
    param(
        [string[]]$Candidates,
        [string]$Label
    )
    foreach ($Candidate in $Candidates) {
        if (Test-Path -LiteralPath $Candidate -PathType Leaf) {
            return [System.IO.Path]::GetFullPath($Candidate)
        }
    }
    throw "${Label} was not found in the patch folder. Re-extract the Windows Portable ZIP."
}

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$TempDir = $null

try {
    Write-Host "moon PS1 Korean Patch v1.0 - Windows Portable"
    Write-Host "No Python installation is required."
    Write-Host ""

    $SourceBin = Get-RequiredPath $Bin "Drag the original Rev 1 BIN here, then press Enter"
    if ([string]::IsNullOrWhiteSpace($Cue)) {
        $AutomaticCue = [System.IO.Path]::ChangeExtension($SourceBin, ".cue")
        if (Test-Path -LiteralPath $AutomaticCue -PathType Leaf) {
            $SourceCue = [System.IO.Path]::GetFullPath($AutomaticCue)
        } else {
            $SourceCue = Get-RequiredPath $null "Drag the original Rev 1 CUE here, then press Enter"
        }
    } else {
        $SourceCue = Get-RequiredPath $Cue "Drag the original Rev 1 CUE here, then press Enter"
    }

    $Xdelta = Find-BundledFile @(
        (Join-Path $Root "xdelta3.exe"),
        (Join-Path $Root "tools\xdelta3.exe")
    ) "xdelta3.exe"
    $Patch = Find-BundledFile @(
        (Join-Path $Root "patches\$PatchName"),
        (Join-Path $Root $PatchName)
    ) "xdelta patch"

    Write-Host "Checking the original BIN, CUE, patch, and xdelta3..."
    Assert-ExactFile $SourceBin "Original BIN" $ExpectedInputSize $ExpectedInputSha256
    Assert-ExactFile $SourceCue "Original CUE" $ExpectedCueSize $ExpectedCueSha256
    Assert-ExactFile $Patch "xdelta patch" $ExpectedPatchSize $ExpectedPatchSha256
    Assert-ExactFile $Xdelta "xdelta3.exe" $ExpectedXdeltaSize $ExpectedXdeltaSha256

    $OutputParent = Split-Path -Parent $SourceBin
    $OutputDir = Join-Path $OutputParent "Moon_Korean_v1.0"
    if (Test-Path -LiteralPath $OutputDir) {
        throw "Output folder already exists: $OutputDir`nMove or rename it before trying again."
    }

    $TempDir = Join-Path $OutputParent (".Moon_Korean_v1.0.tmp-" + [Guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Path $TempDir | Out-Null
    $OutputBin = Join-Path $TempDir $ExpectedBinName
    $OutputCue = Join-Path $TempDir $ExpectedCueName

    Write-Host "Applying the xdelta patch. Please wait..."
    & $Xdelta -d -s $SourceBin $Patch $OutputBin
    if ($LASTEXITCODE -ne 0) {
        throw "xdelta3 failed with exit code $LASTEXITCODE."
    }

    Write-Host "Checking the completed BIN..."
    Assert-ExactFile $OutputBin "Completed BIN" $ExpectedOutputSize $ExpectedOutputSha256
    Copy-Item -LiteralPath $SourceCue -Destination $OutputCue
    Assert-ExactFile $OutputCue "Completed CUE" $ExpectedCueSize $ExpectedCueSha256
    Move-Item -LiteralPath $TempDir -Destination $OutputDir
    $TempDir = $null

    Write-Host ""
    Write-Host "Patch completed successfully." -ForegroundColor Green
    Write-Host "Output folder: $OutputDir"
    Write-Host "BIN SHA-256: $ExpectedOutputSha256"
    Write-Host "Open the CUE file in your emulator."
    Write-Host "Do not reuse savestates made with a different game image."
    exit 0
} catch {
    if ($null -ne $TempDir -and (Test-Path -LiteralPath $TempDir)) {
        Remove-Item -LiteralPath $TempDir -Recurse -Force
    }
    Write-Host ""
    Write-Host "ERROR: $($_.Exception.Message)" -ForegroundColor Red
    exit 2
}
