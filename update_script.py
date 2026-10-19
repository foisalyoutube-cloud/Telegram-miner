import re

with open('generate_html.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add History CSS
history_css = """
    /* Transaction History Styles */
    .history-filter-row {{
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: none;
    }}
    .history-filter-row::-webkit-scrollbar {{ display: none; }}
    .history-filter-chip {{
      background: #172233;
      border: 1px solid #23334a;
      color: var(--text-gray);
      padding: 6px 14px;
      border-radius: 16px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }}
    .history-filter-chip.active {{
      background: var(--accent-blue);
      color: #ffffff;
      border-color: var(--accent-blue);
      box-shadow: 0 2px 8px rgba(41, 151, 255, 0.3);
    }}

    .tx-item-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 13px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
      cursor: pointer;
      transition: background 0.15s ease, transform 0.1s ease;
    }}
    .tx-item-card:active {{
      background: var(--card-bg-light);
      transform: scale(0.99);
    }}
    .tx-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .tx-icon-box {{
      width: 40px;
      height: 40px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
    }}
    .tx-icon-box.claim {{ background: rgba(244, 182, 56, 0.15); color: var(--accent-gold); }}
    .tx-icon-box.withdraw {{ background: rgba(255, 71, 87, 0.15); color: var(--danger-red); }}
    .tx-icon-box.deposit {{ background: rgba(0, 201, 128, 0.15); color: var(--accent-green); }}
    .tx-icon-box.reward {{ background: rgba(168, 85, 247, 0.15); color: #a855f7; }}

    .tx-title {{
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 2px;
    }}
    .tx-meta {{
      font-size: 11px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .tx-badge-status {{
      font-size: 10px;
      padding: 1px 6px;
      border-radius: 8px;
      font-weight: 600;
    }}
    .tx-badge-status.completed {{
      background: rgba(0, 201, 128, 0.12);
      color: var(--accent-green);
    }}
    .tx-badge-status.pending {{
      background: rgba(244, 182, 56, 0.12);
      color: var(--accent-gold);
    }}

    .tx-right {{
      text-align: right;
    }}
    .tx-amount {{
      font-size: 14px;
      font-weight: 800;
      font-variant-numeric: tabular-nums;
    }}
    .tx-amount.positive {{
      color: var(--accent-green);
    }}
    .tx-amount.negative {{
      color: #ffffff;
    }}
    .tx-sub {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 1px;
    }}
    .empty-history-box {{
      text-align: center;
      padding: 28px 16px;
      color: var(--text-muted);
      font-size: 13px;
      background: var(--card-bg);
      border: 1px dashed var(--card-border);
      border-radius: 16px;
    }}
"""

content = content.replace("    /* Bottom Navigation Bar */", history_css + "\n    /* Bottom Navigation Bar */")

# 2. Add History markup in Wallet tab
history_html = """
      <div class="section-header">
        <span class="section-title">TRANSACTION HISTORY</span>
        <span class="section-badge" id="txCountBadge">5 entries</span>
      </div>

      <div class="history-filter-row">
        <div class="history-filter-chip active" onclick="setTxFilter('all', this)">All</div>
        <div class="history-filter-chip" onclick="setTxFilter('claim', this)">Claims</div>
        <div class="history-filter-chip" onclick="setTxFilter('withdraw', this)">Withdrawals</div>
        <div class="history-filter-chip" onclick="setTxFilter('deposit', this)">Deposits</div>
      </div>

      <div id="txHistoryContainer"></div>
"""

# Insert history before ACCOUNT section in wallet tab
content = content.replace(
    '      <div class="section-header">\n        <span class="section-title">ACCOUNT</span>\n      </div>',
    history_html + '\n      <div class="section-header">\n        <span class="section-title">ACCOUNT</span>\n      </div>'
)

# 3. Add Details Modal
tx_detail_modal = """
  <!-- Transaction Details Modal -->
  <div class="modal-backdrop" id="txDetailModal">
    <div class="modal-sheet">
      <div class="modal-title" id="modalTxTitle">Transaction Details</div>
      <div class="modal-desc" id="modalTxDesc">Confirmed on TON Network</div>
      <div style="background: #101724; border-radius: 14px; padding: 14px; margin-bottom: 16px; border: 1px solid #23344d;">
        <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 10px;">
          <span style="color: var(--text-gray);">Amount:</span>
          <strong id="modalTxAmount" style="color: var(--accent-green);">+0.00 MRG</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 10px;">
          <span style="color: var(--text-gray);">Type:</span>
          <strong id="modalTxType" style="color: #fff;">Mining Claim</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 10px;">
          <span style="color: var(--text-gray);">Status:</span>
          <strong id="modalTxStatus" style="color: var(--accent-green);">Completed ✓</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 10px;">
          <span style="color: var(--text-gray);">Date &amp; Time:</span>
          <span id="modalTxTime" style="color: #fff; font-size: 13px;">Today</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 13px;">
          <span style="color: var(--text-gray);">Hash / ID:</span>
          <span id="modalTxHash" style="color: var(--accent-blue); font-family: monospace;">ton_tx_91823</span>
        </div>
      </div>
      <button class="modal-btn-confirm" onclick="viewOnExplorer()">View on TonScan</button>
      <button class="modal-btn-confirm" style="background: transparent; color: var(--text-muted); margin-top: 8px;" onclick="closeTxModal()">Close</button>
    </div>
  </div>
"""

content = content.replace("  <!-- Withdraw Modal -->", tx_detail_modal + "\n  <!-- Withdraw Modal -->")

with open('generate_html.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML template updated with CSS and markup!")
