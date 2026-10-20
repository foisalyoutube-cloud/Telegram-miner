#!/usr/bin/env python3
with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make admin button permanently visible regardless of checks
html = html.replace('style="display: none;', 'style="display: inline-block;')

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated template.html to make Admin Panel visible in Friends tab")
