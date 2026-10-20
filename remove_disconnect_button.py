#!/usr/bin/env python3
with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the "Disconnect" row
old_row = """        <div class="wallet-info-row" style="cursor: pointer;" onclick="openTonConnectModal()">
          <div class="wallet-info-left">
            <div class="wallet-icon-box red">🚪</div>
            <div>
              <div class="wallet-info-title" style="color: var(--danger-red);" id="walletStatusText">Disconnect</div>
              <div class="wallet-info-sub">TON Connect v2</div>
            </div>
          </div>
        </div>"""

new_row = """<!-- Disconnect row removed as requested -->"""

if old_row in html:
    html = html.replace(old_row, new_row, 1)
    print("1. Successfully removed Disconnect row")
else:
    print("1. WARNING: Disconnect row not found")

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated template.html")
