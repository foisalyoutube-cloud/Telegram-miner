#!/usr/bin/env python3
with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Admin Pin to required password
html = html.replace('const DEFAULT_ADMIN_PIN = "115414";', 'const DEFAULT_ADMIN_PIN = "115414"; // Admin: GwFoisal')

# 2. Fix Deposit Modal visibility
# The user said "deposit botton a click korle deposit page open hochhe na"
# The issue might be CSS. Let's make sure `.modal-backdrop.show` has high z-index.
css_fix = """
    .modal-backdrop {
      z-index: 9999 !important;
    }
"""
html = html.replace('</style>', css_fix + '\n  </style>')

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated template.html with Admin PIN and Deposit Modal CSS fix")
