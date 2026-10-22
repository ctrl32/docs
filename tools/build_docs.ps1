# =============================================================================
#  build_docs.ps1 - local preview / link check of the documentation
#
#  The PUBLIC site is rendered by the web renderer from the bundle that
#  tools\docs_export.py produces. This script is only for us while
#  writing:
#
#    - without switches it builds site\ with --strict, so a dead
#      cross-link or a page missing from the nav FAILS. Nothing else
#      checks that.
#    - -Serve gives a live preview on http://127.0.0.1:8000
#
#  Do not tune the appearance here; how the web looks is the web renderer's
#  business.
#
#  WHEN IT FAILS AND WHAT STAYS: mkdocs cleans site\ before writing, so a
#  failed run can leave it empty - site\ is a build output (gitignored)
#  and nothing else is touched. Needs: pip install mkdocs-material
# =============================================================================
param([switch]$Serve)

$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)

python -c "import material" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Error "mkdocs-material is missing: python -m pip install mkdocs-material"
}

if ($Serve) {
    Write-Host "preview: http://127.0.0.1:8000  (Ctrl+C ends it)"
    python -m mkdocs serve --strict
    exit $LASTEXITCODE
}

python -m mkdocs build --strict
if ($LASTEXITCODE -ne 0) { Write-Error "mkdocs build failed" }
Write-Host "OK - links hold and every page is in the nav."
