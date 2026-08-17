$files = Get-ChildItem -Recurse -Filter *.html
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    # Remove the SVG favicon
    $content = $content -replace '<link rel="icon" href="/favicon\.svg" type="image/svg\+xml">(\r?\n)?', ''
    
    # We already have <link rel="icon" href="/favicon.ico" sizes="32x32">
    # Let's check if we have the PNG one. If not, add it right after the ICO one.
    if ($content -notmatch '<link rel="icon" type="image/png" sizes="192x192" href="/favicon.png">') {
        $pngLink = "`n<link rel=`"icon`" type=`"image/png`" sizes=`"192x192`" href=`"/favicon.png`">"
        $content = $content -replace '<link rel="icon" href="/favicon.ico" sizes="32x32">', "<link rel=`"icon`" href=`"/favicon.ico`" sizes=`"32x32`">$pngLink"
    }

    Set-Content -Path $file.FullName -Value $content -NoNewline
}
