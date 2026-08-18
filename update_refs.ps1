$files = @(
    "index.html",
    "ki-mitarbeiter/index.html",
    "ki-mitarbeiter/propstack-agent/index.html"
)

foreach ($file in $files) {
    $content = Get-Content $file -Raw -Encoding UTF8
    
    # URL changes
    $content = $content -replace '/ki-mitarbeiter/digitale-akquise/', '/ki-mitarbeiter/b2b-lead-pipeline/'
    
    # Text changes
    $content = $content -replace 'Ist der KI-Sales-Researcher nur ein', 'Ist die B2B-Lead-Pipeline nur ein'
    $content = $content -replace 'Der KI-Sales-Researcher\.', 'Die B2B-Lead-Pipeline.'
    $content = $content -replace 'Der KI-Sales-Researcher:', 'Die B2B-Lead-Pipeline:'
    $content = $content -replace 'Der KI-Sales-Researcher', 'Die B2B-Lead-Pipeline'
    $content = $content -replace 'KI-Sales-Researcher \(Akquise\)', 'B2B-Lead-Pipeline'
    
    Set-Content -Path $file -Value $content -NoNewline -Encoding UTF8
}
