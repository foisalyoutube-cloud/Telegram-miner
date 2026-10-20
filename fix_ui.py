#!/usr/bin/env python3
with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Pagination (Add missing onclick handlers)
# The current pagination buttons are using onclick="soundTap(); ... renderMinerLevelsGrid();"
# They need to be parsed and handled correctly. They look syntactically correct in the file.
# Maybe the issue is the variable `minerLevelPageStart` scope or `renderMinerLevelsGrid` itself.

# 2. Add robust event delegation or ensure functions are global
# The issue might be that `renderMinerLevelsGrid` is redefined or scope issues.
# Let's ensure the pagination buttons work by wrapping the logic properly.

# Let's look for the pagination markup in the HTML
old_pagination = """        <div style="grid-column: span 2; display: flex; justify-content: space-between; align-items: center; background: #131d2d; padding: 10px 14px; border-radius: 14px; border: 1px solid #233852; margin-top: 6px;">
          <button class="admin-btn" style="padding: 6px 12px; font-size: 12px; background: #192a3e;" onclick="soundTap(); minerLevelPageStart = Math.max(1, minerLevelPageStart - 6); renderMinerLevelsGrid();">◀ Prev Rigs</button>
          <span style="font-size: 12px; color: var(--text-gray);">Showing Lv ${minerLevelPageStart} - ${endLvl} (Max 1050+)</span>
          <button class="admin-btn" style="padding: 6px 12px; font-size: 12px; background: #192a3e;" onclick="soundTap(); minerLevelPageStart = Math.min(1045, minerLevelPageStart + 6); renderMinerLevelsGrid();">Next Rigs ▶</button>
        </div>"""

# Ensure the JS functions are accessible.
# The pagination is inside a template literal, and onclick strings must be valid JS in the global scope.

# 3. Deposit modal issue: Ensure it's not being hidden by CSS or other issues.
# The user says "deposit button a click korle deposit page open hochhe na"
# The deposit button in `template.html` usually looks like `<button class="btn-buy-mrg" onclick="openDepositModal()">`
# It might be an issue with `onclick` if another element is overlaying it.

# 4. Remove marked functions:
# Based on the image, the user wants to remove the 'Close' button at top left 
# and the menu icon '⋮' at the top right.

old_close_btn = """    <div class="tg-close-btn" onclick="handleTgClose()">
      <span>✕</span>
      <span>Close</span>
    </div>"""
new_close_btn = """<!-- Removed Close Button -->"""

# The menu icon ⋮ often comes from a library or a specific markup.
# Looking at the image, it's just standard UI. I need to find the ⋮ icon markup.
# It might be in the `<div class="tg-topbar">` or similar.

# Let's start with cleaning up the markup.
html = html.replace(old_close_btn, new_close_btn)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated template.html")
