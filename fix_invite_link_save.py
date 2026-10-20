#!/usr/bin/env python3
with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update saveGlobalConfig to save inviteLink
old_save_config = """      appConfig.tonWallet = document.getElementById('cfgWalletAddr').value.trim() || 'UQBFoMy-deRH';

      try {"""
new_save_config = """      appConfig.tonWallet = document.getElementById('cfgWalletAddr').value.trim() || 'UQBFoMy-deRH';
      appConfig.inviteLink = document.getElementById('cfgInviteLink').value.trim() || 't.me/your_bot';

      try {"""

if old_save_config in html:
    html = html.replace(old_save_config, new_save_config, 1)
    print("1. Added inviteLink save logic")
else:
    print("1. WARNING: old_save_config not matched")

# 2. Update applyGlobalConfig to read and update user panel
# Look for applyGlobalConfig()
# It seems `applyGlobalConfig` updates symbols, but maybe not the invite link directly.
# Let's see `applyGlobalConfig`.

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated template.html")
