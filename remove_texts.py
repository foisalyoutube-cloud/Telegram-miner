#!/usr/bin/env python3
with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove "Live Config" badge
html = html.replace('<span class="badge-chip verified" style="font-size: 11px;">Live Config</span>', '')

# 2. Update error message text in PIN modal
html = html.replace("errorMsg.innerText = '❌ Incorrect PIN! Please enter master PIN (115414)';", "errorMsg.innerText = '❌ Incorrect PIN!';")

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated template.html by removing specified texts")
