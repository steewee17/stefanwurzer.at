$files = Get-ChildItem -Recurse -Filter *.html
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    $content = $content -replace '<meta property="og:image"[^>]*>(\r?\n)?', ''
    $content = $content -replace '<meta name="twitter:image"[^>]*>(\r?\n)?', ''
    $content = $content -replace '<link rel="apple-touch-icon"[^>]*>(\r?\n)?', ''
    $injection = "<link rel=`"apple-touch-icon`" href=`"/thumbnail_sw.jpg`">`n<meta property=`"og:image`" content=`"https://www.stefanwurzer.at/og-img_sw.jpg`">`n<meta name=`"twitter:image`" content=`"https://www.stefanwurzer.at/og-img_sw.jpg`">`n"
    $content = $content -replace '</head>', "$injection</head>"
    Set-Content -Path $file.FullName -Value $content -NoNewline
}
