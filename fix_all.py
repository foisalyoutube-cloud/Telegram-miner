#!/usr/bin/env python3
with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Topbar Close Button and ⋮ Menu Icon
old_topbar = """    <div class="tg-close-btn" onclick="handleTgClose()">
      <span>✕</span>
      <span>Close</span>
    </div>

    <div class="tg-top-pills">
      <div class="user-avatar-small" title="GW Foisal">GW</div>
      <div class="balance-capsule" onclick="openDepositModal()">
        <img class="coin-icon token-logo-img" src="data:image/jpeg;base64,__COIN_B64__" alt="Coin">
        <span class="val" id="topBalance">0.00</span>
        <span class="currency token-sym">MRG</span>
        <div class="plus-btn">+</div>
      </div>
      <div class="level-capsule" onclick="switchTab('miners')">
        <span class="bolt">⚡</span>
        <span id="topbarLevelSpan">Level 1</span>
      </div>
    </div>

    <div class="tg-right-actions">
      <span onclick="toggleLanguage()">⌵</span>
      <span onclick="openAdminMenu()">⋮</span>
    </div>"""

new_topbar = """    <div class="tg-top-pills" style="margin-left: 0; width: 100%; justify-content: space-between;">
      <div class="user-avatar-small" title="GW Foisal">GW</div>
      <div class="balance-capsule" onclick="openDepositModal()">
        <img class="coin-icon token-logo-img" src="data:image/jpeg;base64,__COIN_B64__" alt="Coin">
        <span class="val" id="topBalance">0.00</span>
        <span class="currency token-sym">MRG</span>
        <div class="plus-btn">+</div>
      </div>
      <div class="level-capsule" onclick="switchTab('miners')">
        <span class="bolt">⚡</span>
        <span id="topbarLevelSpan">Level 1</span>
      </div>
    </div>"""

if old_topbar in html:
    html = html.replace(old_topbar, new_topbar, 1)
    print("1. Removed Close button and menu icon")

# 2. Fix pagination buttons in renderMinerLevelsGrid
# Ensure variables are in scope.
# Adding `window.` prefix might help if scope is an issue, or ensure it's in global scope.
# The issue might be that renderMinerLevelsGrid is calling itself and losing scope of `minerLevelPageStart`.
# Let's put `minerLevelPageStart` in the `state` or `window` object.
html = html.replace("let minerLevelPageStart = 1;", "window.minerLevelPageStart = 1;")
html = html.replace("minerLevelPageStart", "window.minerLevelPageStart")

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated template.html")
