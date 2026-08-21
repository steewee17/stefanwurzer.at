import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'rb') as f:
    content = f.read()

# Replace common mojibake
replacements = {
    b"f\xc3\x87\xc2\xac\xc3\x82\xc2\xadr": b"f\xc3\xbcr",
    b"f\xef\xbf\xbdr": b"f\xc3\xbcr",
    b"ben\xef\xbf\xbdtigt": b"ben\xc3\xb6tigt",
    b"Langzeitged\xef\xbf\xbdchtnisse": b"Langzeitged\xc3\xa4chtnisse",
    b"europ\xef\xbf\xbdischen": b"europ\xc3\xa4ischen",
    b"Unabh\xef\xbf\xbdngigkeit": b"Unabh\xc3\xa4ngigkeit",
    b"\xef\xbf\xbd ": b"\xe2\x80\x93 ", # en dash
    b"\xc3\x83\xc2\xbc": b"\xc3\xbcr",
}

for bad, good in replacements.items():
    content = content.replace(bad, good)

with open(f_path, 'wb') as f:
    f.write(content)
