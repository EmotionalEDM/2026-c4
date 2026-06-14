# 启动展示后端
chcp 65001 > $null
$OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"

$HERE = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $HERE

if (-not $env:SKILLCODER_DATA_DIR) {
    $env:SKILLCODER_DATA_DIR = Join-Path (Split-Path $HERE -Parent) "data"
}
Write-Host "[demo] 数据目录: $env:SKILLCODER_DATA_DIR"

if (-not $env:HOST) { $env:HOST = "0.0.0.0" }
if (-not $env:PORT) { $env:PORT = "8000" }

# 使用 py -3 调用 uvicorn
py -3 -m uvicorn app.main:app --host $env:HOST --port $env:PORT --reload