#!/usr/bin/env python3
import os
import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original template length:", len(html))

# ========================================================
# 1. REMOVE CLEAN BUTTON FROM FRIENDS TAB
# ========================================================
# Look for the clean button in tab-friends
friends_clean_pattern = r'<div style="display: flex; gap: 6px; flex-shrink: 0;">\s*<button class="badge-chip" onclick="openTgSyncModal\(\)"[^>]*>🔄 Sync</button>\s*<button class="badge-chip" onclick="openCleanDataModal\(\)"[^>]*>🧹 Clean</button>\s*</div>'

friends_clean_replacement = '''<div style="display: flex; gap: 6px; flex-shrink: 0;">
            <button class="badge-chip" onclick="openTgSyncModal()" style="background: #0098ea; color: #fff; border: none; font-size: 11px; padding: 6px 12px; cursor: pointer; font-weight: 700; border-radius: 8px;">🔄 Sync Telegram</button>
          </div>'''

if re.search(friends_clean_pattern, html):
    html = re.sub(friends_clean_pattern, friends_clean_replacement, html, count=1)
    print("✓ Successfully removed clean button from friends tab")
else:
    # Try alternate pattern
    html = html.replace('<button class="badge-chip" onclick="openCleanDataModal()" style="background: rgba(255, 75, 75, 0.18); color: #ff6b6b; border: 1px solid rgba(255, 75, 75, 0.4); font-size: 11px; padding: 6px 8px; cursor: pointer; font-weight: 600; border-radius: 8px;" title="Clean all app data">🧹 Clean</button>', '')
    print("✓ Removed clean button via direct match")

# ========================================================
# 2. ADD HOME SCREEN TOTAL BALANCE CARD & CLASS token-logo-img
# ========================================================
# In Tab 1 (Mine tab), right below the btn-claim, add the animated home-balance-card
old_claim_block = '''        <button class="btn-claim" id="btnClaim" onclick="claimMiningReward()">
          <span>Claim Reward · <span id="btnClaimVal">0.00</span> <span class="token-sym">MRG</span></span>
        </button>
      </div>'''

new_claim_block = '''        <button class="btn-claim" id="btnClaim" onclick="claimMiningReward()">
          <span>Claim Reward · <span id="btnClaimVal">0.00</span> <span class="token-sym">MRG</span></span>
        </button>

        <!-- Live Home Balance Display Card -->
        <div class="home-balance-card" id="homeBalanceCard" onclick="switchTab('wallet')">
          <div class="home-bal-icon-wrap">
            <img class="coin-icon token-logo-img" src="data:image/jpeg;base64,__COIN_B64__" alt="Token">
          </div>
          <div class="home-bal-content">
            <div class="home-bal-sub-label">TOTAL WALLET BALANCE (HOME)</div>
            <div class="home-bal-row">
              <span class="home-bal-val" id="homeWalletBalance">0.00</span>
              <span class="home-bal-sym token-sym">MRG</span>
            </div>
            <div class="home-bal-sub" id="homeWalletSub">≈ $0.00 USD · Tap to View Wallet</div>
          </div>
          <div class="home-bal-chevron">›</div>
        </div>
      </div>'''

if old_claim_block in html:
    html = html.replace(old_claim_block, new_claim_block, 1)
    print("✓ Successfully added home-balance-card to Home Screen (Tab 1)")
else:
    print("! Could not find exact old_claim_block, searching with regex...")
    pattern = r'(<button class="btn-claim" id="btnClaim"[^>]*>[\s\S]*?<\/button>\s*<\/div>)'
    replacement = r'''<button class="btn-claim" id="btnClaim" onclick="claimMiningReward()">
          <span>Claim Reward · <span id="btnClaimVal">0.00</span> <span class="token-sym">MRG</span></span>
        </button>

        <!-- Live Home Balance Display Card -->
        <div class="home-balance-card" id="homeBalanceCard" onclick="switchTab('wallet')">
          <div class="home-bal-icon-wrap">
            <img class="coin-icon token-logo-img" src="data:image/jpeg;base64,__COIN_B64__" alt="Token">
          </div>
          <div class="home-bal-content">
            <div class="home-bal-sub-label">TOTAL WALLET BALANCE (HOME)</div>
            <div class="home-bal-row">
              <span class="home-bal-val" id="homeWalletBalance">0.00</span>
              <span class="home-bal-sym token-sym">MRG</span>
            </div>
            <div class="home-bal-sub" id="homeWalletSub">≈ $0.00 USD · Tap to View Wallet</div>
          </div>
          <div class="home-bal-chevron">›</div>
        </div>
      </div>'''
    html = re.sub(pattern, replacement, html, count=1)
    print("✓ Added home-balance-card via regex")

# Add token-logo-img class to coin icons and mascot coin
html = html.replace('<img class="coin-icon" src="data:image/jpeg;base64,__COIN_B64__"', '<img class="coin-icon token-logo-img" src="data:image/jpeg;base64,__COIN_B64__"')
html = html.replace('<img class="mascot-coin" id="mascotCoin" src="data:image/jpeg;base64,__COIN_B64__"', '<img class="mascot-coin token-logo-img" id="mascotCoin" src="data:image/jpeg;base64,__COIN_B64__"')

# ========================================================
# 3. CLEAN DEMO TOKEN HOLD RECORD, DEMO MINER LEVEL, DEMO MINING SPEED
# ========================================================
# In HTML:
html = html.replace('<span class="val" id="topBalance">2.1K</span>', '<span class="val" id="topBalance">0.00</span>')
html = html.replace('<span id="topbarLevelSpan">Level 83</span>', '<span id="topbarLevelSpan">Level 1</span>')
html = html.replace('<div class="mine-level-tag" id="mineLevelTag">Level 83 Miner</div>', '<div class="mine-level-tag" id="mineLevelTag">Level 1 Miner</div>')
html = html.replace('<span id="unclaimedVal">0.002938</span>', '<span id="unclaimedVal">0.000000</span>')
html = html.replace('<div class="unclaimed-subrate">≈ $0.0000 · 3.19 TH/s</div>', '<div class="unclaimed-subrate">≈ $0.0000 · 1.00 MH/s</div>')
html = html.replace('<div class="miner-stat-val" id="mineStatHashrate">3.19 TH/s</div>', '<div class="miner-stat-val" id="mineStatHashrate">1.00 MH/s</div>')
html = html.replace('<div class="miner-stat-val" id="mineStatLevel">Level 83</div>', '<div class="miner-stat-val" id="mineStatLevel">Level 1</div>')

# In Tab 3 Miners Store:
html = html.replace('<div class="stat-trio-val" id="minersTabLevelVal">83</div>', '<div class="stat-trio-val" id="minersTabLevelVal">1</div>')
html = html.replace('<div class="stat-trio-val" id="minersTabPeakVal">103</div>', '<div class="stat-trio-val" id="minersTabPeakVal">1</div>')
html = html.replace('<div class="stat-trio-val green" id="minersTabPnlVal">+71.5</div>', '<div class="stat-trio-val green" id="minersTabPnlVal">+0.00</div>')
html = html.replace('<span class="next" id="minersTabNextLevel">Level 84</span>', '<span class="next" id="minersTabNextLevel">Level 2</span>')
html = html.replace('<div class="action-nav-text-sub" id="minersAllTimeMinedSub">All-Time Mined: 2.3K <span class="token-sym">MRG</span></div>', '<div class="action-nav-text-sub" id="minersAllTimeMinedSub">All-Time Mined: 0.00 <span class="token-sym">MRG</span></div>')
html = html.replace('<div class="action-nav-text-sub" id="minersPeakLevelSub">Peak Level 103</div>', '<div class="action-nav-text-sub" id="minersPeakLevelSub">Peak Level 1</div>')
html = html.replace('<strong style="color: var(--accent-blue);" id="minersActiveRigTitle">Level 83 Miner (3.19 TH/s)</strong>', '<strong style="color: var(--accent-blue);" id="minersActiveRigTitle">Level 1 Miner (1.00 MH/s)</strong>')
html = html.replace('Maintain on-chain holdings to stay at Level 83.', 'Hold tokens or upgrade to unlock higher miner levels.')

# In Tab 5 Wallet:
html = html.replace('<span id="walletMRGBalance">94.0</span>', '<span id="walletMRGBalance">0.00</span>')
html = html.replace('<div class="miner-stat-val" style="color: #fff;" id="walletTotalHolding">2.1K <span class="token-sym">MRG</span></div>', '<div class="miner-stat-val" style="color: #fff;" id="walletTotalHolding">0.00 <span class="token-sym">MRG</span></div>')

# In Admin Panel default inputs:
html = html.replace('<input type="number" class="modal-input" id="userCtrlMinerLevel" placeholder="e.g. 83" value="83"', '<input type="number" class="modal-input" id="userCtrlMinerLevel" placeholder="e.g. 1" value="1"')
html = html.replace('<input type="number" class="modal-input" id="userCtrlPeakLevel" placeholder="e.g. 103" value="103"', '<input type="number" class="modal-input" id="userCtrlPeakLevel" placeholder="e.g. 1" value="1"')
html = html.replace('<input type="text" class="modal-input" id="userCtrlTodaysPnl" placeholder="e.g. +71.5" value="+71.5"', '<input type="text" class="modal-input" id="userCtrlTodaysPnl" placeholder="e.g. +0.00" value="+0.00"')
html = html.replace('<input type="text" class="modal-input" id="userCtrlAllTimeMined" placeholder="e.g. 2.3K" value="2.3K"', '<input type="text" class="modal-input" id="userCtrlAllTimeMined" placeholder="e.g. 0.00" value="0.00"')
html = html.replace('<input type="text" class="modal-input" id="userCtrlHashrate" placeholder="e.g. 3.19 TH/s" value="3.19 TH/s"', '<input type="text" class="modal-input" id="userCtrlHashrate" placeholder="e.g. 1.00 MH/s" value="1.00 MH/s"')
html = html.replace('<input type="text" class="modal-input" id="cfgHashrate" placeholder="e.g. 3.19 TH/s" value="3.19 TH/s"', '<input type="text" class="modal-input" id="cfgHashrate" placeholder="e.g. 1.00 MH/s" value="1.00 MH/s"')
html = html.replace('<input type="text" class="modal-input" id="userCtrlTotalHolding" placeholder="e.g. 2.1K" value="2.1K"', '<input type="text" class="modal-input" id="userCtrlTotalHolding" placeholder="e.g. 0.00" value="0.00"')

print("✓ Cleaned demo token hold, miner level, and mining speed in HTML")

# ========================================================
# 4. ADD CHANGE TOKEN LOGO CARD TO ADMIN TAB 0 (BRANDING)
# ========================================================
token_logo_card_html = '''
        <!-- 🪙 CHANGE TOKEN LOGO CARD (UNIVERSAL APP-WIDE SYNC) -->
        <div class="admin-card" style="margin-top: 14px; border: 1px solid rgba(244, 182, 56, 0.4); background: linear-gradient(135deg, rgba(22, 34, 52, 0.95), rgba(16, 25, 40, 0.95));">
          <div class="admin-card-title">
            <span>🪙 Change Token Logo (টোকেন লোগো পরিবর্তন)</span>
            <span class="badge-chip verified" style="font-size: 11px; background: rgba(244, 182, 56, 0.2); color: #f4b638;">Universal Sync</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 14px; line-height: 1.5;">
            Change the token logo here to dynamically update ALL token logos and coin icons across the entire app (top bar balance, mascot mining stage, wallet balance, home screen, DEX swap, and task rewards).
          </p>

          <!-- Current Logo Live Preview -->
          <div style="display: flex; align-items: center; gap: 16px; background: #0c1420; padding: 14px; border-radius: 16px; border: 1px solid #1c2b42; margin-bottom: 14px;">
            <div style="position: relative; width: 62px; height: 62px; border-radius: 50%; background: radial-gradient(circle, rgba(244, 182, 56, 0.25), transparent); display: flex; align-items: center; justify-content: center; border: 2px solid #f4b638; box-shadow: 0 0 16px rgba(244, 182, 56, 0.35); flex-shrink: 0;">
              <img id="adminTokenLogoPreview" class="token-logo-img" src="data:image/jpeg;base64,__COIN_B64__" alt="Token Logo" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover; transition: transform 0.4s ease;">
            </div>
            <div>
              <div style="font-size: 15px; font-weight: 800; color: #fff;">Active Token: <span class="token-sym">MRG</span></div>
              <div style="font-size: 12px; color: var(--accent-gold); font-weight: 700; margin-top: 2px;" id="adminTokenLogoStatus">Active Logo Synced</div>
              <div style="font-size: 11px; color: var(--text-muted); margin-top: 3px;">Instant real-time update on all screens</div>
            </div>
          </div>

          <!-- Quick Logo Presets -->
          <div style="margin-bottom: 14px;">
            <label class="admin-label" style="display: block; margin-bottom: 6px; font-size: 12px;">Choose From Popular Presets:</label>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;">
              <button class="admin-btn" style="padding: 10px 4px; font-size: 11px; display: flex; flex-direction: column; align-items: center; gap: 4px; background: #141f30;" onclick="adminSelectPresetLogo('gold')">
                <span style="font-size: 22px;">🟡</span>
                <span style="font-size: 10px;">MRG Gold</span>
              </button>
              <button class="admin-btn" style="padding: 10px 4px; font-size: 11px; display: flex; flex-direction: column; align-items: center; gap: 4px; background: #141f30;" onclick="adminSelectPresetLogo('ton')">
                <span style="font-size: 22px;">💎</span>
                <span style="font-size: 10px;">TON Gem</span>
              </button>
              <button class="admin-btn" style="padding: 10px 4px; font-size: 11px; display: flex; flex-direction: column; align-items: center; gap: 4px; background: #141f30;" onclick="adminSelectPresetLogo('btc')">
                <span style="font-size: 22px;">₿</span>
                <span style="font-size: 10px;">Bitcoin</span>
              </button>
              <button class="admin-btn" style="padding: 10px 4px; font-size: 11px; display: flex; flex-direction: column; align-items: center; gap: 4px; background: #141f30;" onclick="adminSelectPresetLogo('eth')">
                <span style="font-size: 22px;">Ξ</span>
                <span style="font-size: 10px;">Ethereum</span>
              </button>
              <button class="admin-btn" style="padding: 10px 4px; font-size: 11px; display: flex; flex-direction: column; align-items: center; gap: 4px; background: #141f30;" onclick="adminSelectPresetLogo('fire')">
                <span style="font-size: 22px;">🔥</span>
                <span style="font-size: 10px;">Fire Token</span>
              </button>
              <button class="admin-btn" style="padding: 10px 4px; font-size: 11px; display: flex; flex-direction: column; align-items: center; gap: 4px; background: #141f30;" onclick="adminSelectPresetLogo('star')">
                <span style="font-size: 22px;">⭐</span>
                <span style="font-size: 10px;">Star Gold</span>
              </button>
              <button class="admin-btn" style="padding: 10px 4px; font-size: 11px; display: flex; flex-direction: column; align-items: center; gap: 4px; background: #141f30;" onclick="adminSelectPresetLogo('rocket')">
                <span style="font-size: 22px;">🚀</span>
                <span style="font-size: 10px;">Rocket</span>
              </button>
              <button class="admin-btn" style="padding: 10px 4px; font-size: 11px; display: flex; flex-direction: column; align-items: center; gap: 4px; background: #141f30;" onclick="adminSelectPresetLogo('original')">
                <span style="font-size: 22px;">🐱</span>
                <span style="font-size: 10px;">Original</span>
              </button>
            </div>
          </div>

          <!-- Custom Image Upload & URL/Emoji Input -->
          <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 12px;">
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Upload Custom Image (From Device)</label>
              <input type="file" id="adminTokenLogoFileInput" accept="image/*" style="display: none;" onchange="handleAdminTokenLogoUpload(event)">
              <button class="admin-btn" style="width: 100%; padding: 12px; background: #18253a; border: 1px dashed #304a75; color: #6db1ff; font-weight: 700; display: flex; align-items: center; justify-content: center; gap: 8px;" onclick="document.getElementById('adminTokenLogoFileInput').click()">
                <span>📁</span>
                <span>Upload Logo From Device (PNG / JPG / WebP / SVG)</span>
              </button>
            </div>

            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Or Enter Custom Image URL / Emoji</label>
              <div style="display: flex; gap: 8px;">
                <input type="text" class="modal-input" id="cfgTokenLogoUrl" placeholder="https://... or Emoji (e.g. 🪙, 💎, 🚀)" style="margin-bottom: 0; flex: 1;">
                <button class="admin-btn" style="padding: 10px 16px; background: #233754; font-weight: 700;" onclick="applyCustomTokenLogoUrl()">Apply</button>
              </div>
            </div>
          </div>

          <!-- Universal Apply Action -->
          <div style="display: flex; gap: 8px;">
            <button class="admin-btn green" style="flex: 1; padding: 12px; font-size: 13px; font-weight: 800; box-shadow: 0 4px 14px rgba(0, 201, 128, 0.3);" onclick="adminApplyAllTokenLogos(currentSelectedTokenLogo)">
              ✨ Save &amp; Change All Token Logos Across App
            </button>
          </div>
        </div>
'''

# Insert token_logo_card right after the first admin-card in admin-sec-branding
branding_sec_marker = '<div class="admin-tab-section active" id="admin-sec-branding">'
if branding_sec_marker in html:
    # Find the end of the first admin-card in this section
    first_card_end = html.find('</div>\n        </div>\n\n        <!-- TELEGRAM AUTO-SYNC', html.find(branding_sec_marker))
    if first_card_end != -1:
        html = html[:first_card_end + 15] + token_logo_card_html + html[first_card_end + 15:]
        print("✓ Successfully inserted Change Token Logo card in Admin Tab 0")
    else:
        # Fallback search
        html = html.replace('<!-- TELEGRAM AUTO-SYNC & CLEAN APP DATA CARD -->', token_logo_card_html + '\n        <!-- TELEGRAM AUTO-SYNC & CLEAN APP DATA CARD -->')
        print("✓ Inserted Change Token Logo card before Telegram Auto-Sync card")

# ========================================================
# 5. CSS ANIMATIONS & STYLING FOR ALL FUNCTIONS
# ========================================================
animations_css = '''
    /* ===================================================
       ALL FUNCTIONS ANIMATED SUITE (FLUID M3 ANIMATIONS)
       =================================================== */
    
    /* 1. Fluid Tab Transitions */
    .tab-content {
      display: none;
      opacity: 0;
      transform: translateY(12px) scale(0.985);
      transition: opacity 0.28s cubic-bezier(0.16, 1, 0.3, 1), transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .tab-content.active {
      display: block;
      opacity: 1;
      transform: translateY(0) scale(1);
      animation: tabEnterAnim 0.32s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes tabEnterAnim {
      0% { opacity: 0; transform: translateY(16px) scale(0.98); }
      100% { opacity: 1; transform: translateY(0) scale(1); }
    }

    /* 2. Interactive Navigation Bar Animation */
    .nav-tab {
      transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), color 0.2s ease;
      cursor: pointer;
    }
    .nav-tab:active {
      transform: scale(0.86);
    }
    .nav-tab.active .nav-tab-icon-wrap {
      animation: navTabPop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    @keyframes navTabPop {
      0% { transform: scale(0.8); }
      50% { transform: scale(1.25); filter: drop-shadow(0 0 8px rgba(0, 152, 234, 0.8)); }
      100% { transform: scale(1); }
    }

    /* 3. Universal Button Press Feedback */
    button, .btn-claim, .btn-buy-mrg, .btn-withdraw, .admin-btn, .modal-btn-confirm, .btn-copy-ref, .btn-share-ref, .history-filter-chip {
      transition: transform 0.14s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s ease, box-shadow 0.2s ease !important;
      -webkit-tap-highlight-color: transparent;
    }
    button:active, .btn-claim:active, .btn-buy-mrg:active, .btn-withdraw:active, .admin-btn:active, .modal-btn-confirm:active, .btn-copy-ref:active, .btn-share-ref:active {
      transform: scale(0.94) !important;
      filter: brightness(1.2);
    }

    /* 4. Home Screen Live Balance Card */
    .home-balance-card {
      background: linear-gradient(135deg, rgba(16, 26, 44, 0.95), rgba(24, 38, 64, 0.95));
      border: 1px solid rgba(0, 152, 234, 0.4);
      border-radius: 18px;
      padding: 14px 16px;
      margin-top: 14px;
      display: flex;
      align-items: center;
      gap: 14px;
      cursor: pointer;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
      transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .home-balance-card:active {
      transform: scale(0.97);
      border-color: var(--accent-blue);
      box-shadow: 0 0 16px rgba(0, 152, 234, 0.4);
    }
    .home-bal-icon-wrap {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(0, 152, 234, 0.25), transparent);
      border: 1px solid rgba(0, 152, 234, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .home-bal-icon-wrap img {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      object-fit: cover;
    }
    .home-bal-content {
      flex: 1;
      overflow: hidden;
    }
    .home-bal-sub-label {
      font-size: 10px;
      font-weight: 800;
      color: #70b5f5;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      margin-bottom: 2px;
    }
    .home-bal-row {
      display: flex;
      align-items: baseline;
      gap: 6px;
    }
    .home-bal-val {
      font-size: 24px;
      font-weight: 900;
      color: #ffffff;
      font-family: var(--font-numeric);
      letter-spacing: -0.5px;
    }
    .home-bal-sym {
      font-size: 14px;
      font-weight: 800;
      color: var(--accent-blue);
    }
    .home-bal-sub {
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 1px;
    }
    .home-bal-chevron {
      font-size: 20px;
      color: var(--text-muted);
      font-weight: 300;
    }

    /* 5. Mascot Coin Squash, Stretch & Tap Particles */
    .mascot-coin {
      transition: transform 0.15s cubic-bezier(0.34, 1.56, 0.64, 1);
      cursor: pointer;
    }
    .mascot-coin:active {
      transform: scale(0.88, 1.12) rotate(-3deg);
    }
    @keyframes mascotTapSquish {
      0% { transform: scale(1); }
      30% { transform: scale(1.15, 0.88); }
      60% { transform: scale(0.92, 1.08); }
      100% { transform: scale(1); }
    }
    .mascot-tap-anim {
      animation: mascotTapSquish 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    @keyframes coinSpinBurst {
      0% { transform: scale(1) rotate(0deg); }
      50% { transform: scale(1.2) rotate(180deg); }
      100% { transform: scale(1) rotate(360deg); }
    }
    .coin-spin-burst {
      animation: coinSpinBurst 0.65s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    /* 6. Flying Coin Particles for Claims */
    .flying-coin-particle {
      position: fixed;
      width: 26px;
      height: 26px;
      z-index: 999999;
      pointer-events: none;
      transition: transform 0.65s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.65s ease-in;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.5));
    }

    /* 7. Balance Bounce and Glow Pulse */
    @keyframes balBounce {
      0% { transform: scale(1); }
      35% { transform: scale(1.26); color: #ffd700; text-shadow: 0 0 18px rgba(255, 215, 0, 0.9); }
      75% { transform: scale(0.94); }
      100% { transform: scale(1); }
    }
    .balance-bounce {
      animation: balBounce 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }
    @keyframes balanceGlowPulse {
      0% { box-shadow: 0 0 0 0 rgba(0, 152, 234, 0.8); }
      50% { box-shadow: 0 0 20px 4px rgba(244, 182, 56, 0.9); }
      100% { box-shadow: 0 0 0 0 rgba(0, 152, 234, 0); }
    }
    .balance-glow-pulse {
      animation: balanceGlowPulse 0.75s ease-out;
    }

    /* 8. Token Logo Spin & Pulse on Change */
    @keyframes tokenLogoSwap {
      0% { transform: scale(0.4) rotate(-180deg); opacity: 0; }
      60% { transform: scale(1.22) rotate(20deg); opacity: 1; }
      100% { transform: scale(1) rotate(0deg); opacity: 1; }
    }
    .token-logo-swapped {
      animation: tokenLogoSwap 0.55s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
    }

    /* 9. Streak Card Flip Animation */
    @keyframes streakCardFlip {
      0% { transform: scale(1) rotateY(0deg); }
      50% { transform: scale(1.15) rotateY(180deg); box-shadow: 0 0 16px rgba(0, 201, 128, 0.6); }
      100% { transform: scale(1) rotateY(360deg); }
    }
    .streak-flip-anim {
      animation: streakCardFlip 0.65s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }

    /* 10. Modal Spring Entrance */
    .modal-sheet {
      transform: translateY(100%);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
    }
    .modal-backdrop.show .modal-sheet {
      transform: translateY(0);
    }

    /* 11. Admin Panel Spring Transition */
    .admin-viewport {
      transition: transform 0.38s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
    }

    /* 12. Floating Tap Particle */
    .tap-particle {
      position: absolute;
      color: #ffd700;
      font-weight: 800;
      font-size: 16px;
      pointer-events: none;
      animation: tapFloatUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      text-shadow: 0 0 10px rgba(255, 215, 0, 0.8);
      z-index: 100;
    }
    @keyframes tapFloatUp {
      0% { opacity: 1; transform: translate(-50%, -50%) scale(0.8); }
      50% { opacity: 1; transform: translate(-50%, -120%) scale(1.2); }
      100% { opacity: 0; transform: translate(-50%, -200%) scale(1.4); }
    }
'''

# Insert animations_css before </style>
html = html.replace('  </style>', animations_css + '\n  </style>', 1)
print("✓ Successfully injected comprehensive animation CSS suite")

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved intermediate template.html successfully")
