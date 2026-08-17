$files = Get-ChildItem -Recurse -Filter *.html
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    # Remove old SVG icon line
    $content = $content -replace '<link rel="icon" href="/favicon\.svg" type="image/svg\+xml">(\r?\n)?', ''
    
    # New icon block to insert
    $iconBlock = "<link rel=`"icon`" href=`"/favicon.ico`" sizes=`"32x32`">`n<link rel=`"icon`" href=`"/favicon.svg`" type=`"image/svg+xml`">`n"
    
    # We will inject this right before our previous apple-touch-icon injection
    $content = $content -replace '<link rel="apple-touch-icon"', "$iconBlock<link rel=`"apple-touch-icon`""
    Set-Content -Path $file.FullName -Value $content -NoNewline
}
