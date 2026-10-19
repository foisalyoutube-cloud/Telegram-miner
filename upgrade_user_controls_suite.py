import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update User Panel Tab 1 (Mine tab) elements with IDs for dynamic binding
# We need #mineLevelTag, #topbarLevelSpan, #mineStatHashrate, #mineStatLevel, #mineSpeedBoostPill
html = html.replace(
    '<div class="mine-level-tag">Level 83 Miner</div>',
    '<div class="mine-level-tag" id="mineLevelTag">Level 83 Miner</div>\n            <div class="mine-speed-boost-pill" id="mineSpeedBoostPill" style="display:none; margin-top: 4px; font-size: 11px; padding: 2px 8px; border-radius: 10px; background: rgba(244, 182, 56, 0.2); color: var(--accent-gold); border: 1px solid rgba(244, 182, 56, 0.4); font-weight: 700; display: inline-block;">⚡ 1x Normal</div>'
)

html = html.replace(
    '<span>Level 83</span>\n      </div>\n    </div>\n\n    <div class="tg-right-actions">',
    '<span id="topbarLevelSpan">Level 83</span>\n      </div>\n    </div>\n\n    <div class="tg-right-actions">'
)

# In Tab 1 mine stat rows:
html = html.replace(
    '<div class="miner-stat-row">\n          <div class="miner-stat-left">\n            <div class="miner-icon-box">⏱</div>\n            <span>Mining Speed</span>\n          </div>\n          <div class="miner-stat-val">3.19 TH/s</div>\n        </div>\n        <div class="miner-stat-row">\n          <div class="miner-stat-left">\n            <div class="miner-icon-box" style="color: var(--accent-gold);">⚡</div>\n            <span>Current Miner</span>\n          </div>\n          <div class="miner-stat-val">Level 83</div>\n        </div>',
    '<div class="miner-stat-row">\n          <div class="miner-stat-left">\n            <div class="miner-icon-box">⏱</div>\n            <span>Mining Speed</span>\n          </div>\n          <div class="miner-stat-val" id="mineStatHashrate">3.19 TH/s</div>\n        </div>\n        <div class="miner-stat-row">\n          <div class="miner-stat-left">\n            <div class="miner-icon-box" style="color: var(--accent-gold);">⚡</div>\n            <span>Current Miner</span>\n          </div>\n          <div class="miner-stat-val" id="mineStatLevel">Level 83</div>\n        </div>'
)

# 2. Update Tab 3 (Miners Store tab) with IDs for dynamic binding
miners_old = '''        <div class="stats-trio">
          <div class="stat-trio-card">
            <div class="stat-trio-val">83</div>
            <div class="stat-trio-label">Level</div>
          </div>
          <div class="stat-trio-card">
            <div class="stat-trio-val">103</div>
            <div class="stat-trio-label">Peak</div>
          </div>
          <div class="stat-trio-card">
            <div class="stat-trio-val green">+71.5</div>
            <div class="stat-trio-label">Today's P&amp;L</div>
          </div>
        </div>

        <div class="level-progress-bar-wrap">
          <div class="level-progress-labels">
            <span class="next">Level 84</span>
            <span class="remain">3.0 <span class="token-sym">MRG</span> to go</span>
          </div>
          <div class="progress-track">
            <div class="progress-fill"></div>
          </div>
        </div>'''

miners_new = '''        <div class="stats-trio">
          <div class="stat-trio-card">
            <div class="stat-trio-val" id="minersTabLevelVal">83</div>
            <div class="stat-trio-label">Level</div>
          </div>
          <div class="stat-trio-card">
            <div class="stat-trio-val" id="minersTabPeakVal">103</div>
            <div class="stat-trio-label">Peak</div>
          </div>
          <div class="stat-trio-card">
            <div class="stat-trio-val green" id="minersTabPnlVal">+71.5</div>
            <div class="stat-trio-label">Today's P&amp;L</div>
          </div>
        </div>

        <div class="level-progress-bar-wrap">
          <div class="level-progress-labels">
            <span class="next" id="minersTabNextLevel">Level 84</span>
            <span class="remain" id="minersTabRemain">3.0 <span class="token-sym">MRG</span> to go</span>
          </div>
          <div class="progress-track">
            <div class="progress-fill" id="minersTabProgressFill" style="width: 72%;"></div>
          </div>
        </div>'''

if miners_old in html:
    html = html.replace(miners_old, miners_new)
else:
    print("WARNING: miners_old block not found verbatim, doing regex replace")
    html = re.sub(
        r'<div class="stats-trio">[\s\S]*?<div class="progress-track">\s*<div class="progress-fill"></div>\s*</div>\s*</div>',
        miners_new,
        html
    )

# Also update miners all-time mined and peak record subtext
html = re.sub(
    r'<div class="action-nav-text-sub">All-Time Mined: 2\.3K <span class="token-sym">MRG</span></div>',
    '<div class="action-nav-text-sub" id="minersAllTimeMinedSub">All-Time Mined: 2.3K <span class="token-sym">MRG</span></div>',
    html
)
html = re.sub(
    r'<div class="action-nav-text-sub">Peak Level 103</div>',
    '<div class="action-nav-text-sub" id="minersPeakLevelSub">Peak Level 103</div>',
    html
)
html = re.sub(
    r'Your current rig: <strong style="color: var\(--accent-blue\);">Level 83 Miner \(3\.19 TH/s\)</strong>\.',
    'Your current rig: <strong style="color: var(--accent-blue);" id="minersActiveRigTitle">Level 83 Miner (3.19 TH/s)</strong>.',
    html
)

# 3. Update Tab 4 (Friends / Profile banner)
# Add #profileNftBadge, #profileRoleBadge, #userProfileBio, #userStandingAlert, #adminUserMessageCard
profile_header_target = '''            <div class="badge-chips-row">
              <span class="badge-chip nft">💎 Non-NFT Holder</span>
              <span class="badge-chip verified" id="profileTgVerifiedBadge">✈️ Telegram Verified</span>
              <span class="badge-chip" onclick="openAdminPanel()" style="background: rgba(244, 182, 56, 0.18); color: var(--accent-gold); border: 1px solid rgba(244, 182, 56, 0.4); cursor: pointer; font-weight: 800;">⚙️ Admin Panel</span>
            </div>
          </div>
        </div>'''

profile_header_replacement = '''            <div class="badge-chips-row">
              <span class="badge-chip nft" id="profileNftBadge">💎 Non-NFT Holder</span>
              <span class="badge-chip verified" id="profileTgVerifiedBadge">✈️ Telegram Verified</span>
              <span class="badge-chip" id="profileRoleBadge" style="display: none; font-size: 11px;">👑 VIP</span>
              <span class="badge-chip" onclick="openAdminPanel()" style="background: rgba(244, 182, 56, 0.18); color: var(--accent-gold); border: 1px solid rgba(244, 182, 56, 0.4); cursor: pointer; font-weight: 800;">⚙️ Admin Panel</span>
            </div>
            <div class="user-profile-bio" id="userProfileBio" style="font-size: 11px; color: var(--text-muted); margin-top: 5px;">💎 Pro Miner | Influencer</div>
          </div>
        </div>

        <!-- Account Standing Alert Banner (Controlled by Admin) -->
        <div class="user-standing-alert" id="userStandingAlert" style="display: none; margin: 10px 0; padding: 10px 14px; border-radius: 12px; font-size: 12px; font-weight: 600;"></div>

        <!-- Admin Direct Push Notice Card (Controlled by Admin) -->
        <div class="admin-user-message-card" id="adminUserMessageCard" style="display: none; background: linear-gradient(135deg, rgba(244, 182, 56, 0.15), rgba(41, 151, 255, 0.15)); border: 1px solid rgba(244, 182, 56, 0.4); border-radius: 14px; padding: 12px 14px; margin: 10px 0;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 11px; font-weight: 800; color: var(--accent-gold); text-transform: uppercase; letter-spacing: 0.5px;">📩 Admin Direct Notification</span>
            <span onclick="dismissUserMessage()" style="cursor: pointer; color: var(--text-muted); font-size: 14px; font-weight: bold; padding: 2px 6px;">✕</span>
          </div>
          <div id="adminUserMessageText" style="font-size: 13px; color: #fff; font-weight: 600;"></div>
        </div>'''

if profile_header_target in html:
    html = html.replace(profile_header_target, profile_header_replacement)
else:
    print("WARNING: profile_header_target not found verbatim, checking regex")
    html = re.sub(
        r'<div class="badge-chips-row">\s*<span class="badge-chip nft">💎 Non-NFT Holder</span>\s*<span class="badge-chip verified" id="profileTgVerifiedBadge">[\s\S]*?</div>\s*</div>\s*</div>',
        profile_header_replacement,
        html
    )

# Squad mining elements in Tab 4
html = re.sub(
    r'<div style="font-size: 26px; font-weight: 800; color: #fff; margin-bottom: 2px;">\s*0\.00 <span style="font-size: 16px; color: var\(--text-gray\);">MRG</span>\s*</div>\s*<div style="font-size: 13px; color: var\(--text-muted\); margin-bottom: 14px;">≈ \$0\.000 earned from squad</div>',
    '<div style="font-size: 26px; font-weight: 800; color: #fff; margin-bottom: 2px;">\n          <span id="squadEarnedMRG">0.00</span> <span style="font-size: 16px; color: var(--text-gray);" class="token-sym">MRG</span>\n        </div>\n        <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 14px;" id="squadEarnedUSD">≈ $0.000 earned from squad (<span id="squadFriendsCountText">3 friends</span>)</div>',
    html
)

# 4. Update Tab 5 (Wallet tab)
# Add IDs for Total Holding and Account Verification row
html = re.sub(
    r'<div class="miner-stat-val" style="color: #fff;">2\.1K <span class="token-sym">MRG</span></div>',
    '<div class="miner-stat-val" style="color: #fff;" id="walletTotalHolding">2.1K <span class="token-sym">MRG</span></div>',
    html
)

wallet_kyc_target = '''        <div class="wallet-info-row" onclick="showToast('Your on-chain identity is Verified')">
          <div class="wallet-info-left">
            <div class="wallet-icon-box green">🛡</div>
            <div>
              <div class="wallet-info-title">Account Verification</div>
              <div class="wallet-info-sub">Soulbound KYC on TON</div>
            </div>
          </div>
          <span style="color: var(--accent-green); font-size: 13px; font-weight: 700;">Verified ›</span>
        </div>'''

wallet_kyc_replacement = '''        <div class="wallet-info-row" id="walletKycRow" onclick="showToast('Account Status: ' + (userControls.verificationStatus || 'Verified'))">
          <div class="wallet-info-left">
            <div class="wallet-icon-box green" id="walletKycIconBox">🛡</div>
            <div>
              <div class="wallet-info-title">Account Verification</div>
              <div class="wallet-info-sub" id="walletKycSub">Soulbound KYC on TON</div>
            </div>
          </div>
          <span id="walletKycStatusText" style="color: var(--accent-green); font-size: 13px; font-weight: 700;">Verified ›</span>
        </div>'''

if wallet_kyc_target in html:
    html = html.replace(wallet_kyc_target, wallet_kyc_replacement)
else:
    html = re.sub(
        r'<div class="wallet-info-row" onclick="showToast\(\'Your on-chain identity is Verified\'\)">[\s\S]*?<span style="color: var\(--accent-green\); font-size: 13px; font-weight: 700;">Verified ›</span>\s*</div>',
        wallet_kyc_replacement,
        html
    )

# 5. Replace ADMIN TAB 1: USER CONTROLS with Complete Comprehensive User Control Suite
admin_users_suite = '''      <!-- ADMIN TAB 1: USER CONTROLS -->
      <div class="admin-tab-section" id="admin-sec-users">
        <!-- Live User Summary & Status Bar -->
        <div class="admin-card" style="border: 1px solid rgba(41, 151, 255, 0.4); background: linear-gradient(135deg, rgba(16, 26, 44, 0.95), rgba(24, 38, 64, 0.95));">
          <div class="admin-card-title">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 18px;">👤</span>
              <div>
                <span id="adminUserActiveHandle" style="font-size: 15px; font-weight: 800; color: #fff;">@telegram_miner</span>
                <div id="adminUserSummarySub" style="font-size: 11px; color: var(--text-gray); font-weight: normal;">Active User Session • Level <span id="adminSummaryLevel">83</span></div>
              </div>
            </div>
            <span class="badge-chip verified" id="adminUserStatus" style="font-size: 11px;">Verified ✓</span>
          </div>

          <!-- Quick User Switcher Pills -->
          <div style="display: flex; gap: 6px; overflow-x: auto; padding-bottom: 6px; margin-top: 4px;">
            <button class="badge-chip verified" style="cursor: pointer; font-size: 11px; padding: 5px 10px;" onclick="loadUserToAdmin('@telegram_miner')">👤 Current User</button>
            <button class="badge-chip" style="cursor: pointer; font-size: 11px; padding: 5px 10px; background: #1c2b42; color: var(--text-gray);" onclick="loadUserToAdmin('@alex_ton')">@alex_ton</button>
            <button class="badge-chip" style="cursor: pointer; font-size: 11px; padding: 5px 10px; background: #1c2b42; color: var(--text-gray);" onclick="loadUserToAdmin('@cryptokid')">@cryptokid</button>
            <button class="badge-chip" style="cursor: pointer; font-size: 11px; padding: 5px 10px; background: #1c2b42; color: var(--text-gray);" onclick="loadUserToAdmin('@rakib_dhaka')">@rakib_dhaka</button>
          </div>
        </div>

        <!-- 1. USER IDENTITY & PROFILE CONTROLS -->
        <div class="admin-card">
          <div class="admin-card-title">
            <span>🏷️ 1. User Identity &amp; Profile (প্রোফাইল কন্ট্রোল)</span>
            <span class="badge-chip verified" style="font-size: 10px;">User Visible</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Modify user display name, telegram username, bio title, avatar initials, and account verification badge. Changes appear instantly in the user's profile and topbar.
          </p>

          <div style="display: flex; flex-direction: column; gap: 10px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Display Name</label>
                <input type="text" class="modal-input" id="userCtrlName" placeholder="e.g. GW Foisal" value="Telegram Miner" oninput="liveUpdateUserField('userName', this.value)">
              </div>
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Telegram @Handle</label>
                <input type="text" class="modal-input" id="userCtrlHandle" placeholder="@username" value="@telegram_miner" oninput="liveUpdateUserField('userHandle', this.value)">
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 10px;">
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">User Bio / Title Tag</label>
                <input type="text" class="modal-input" id="userCtrlBio" placeholder="e.g. 💎 Pro Miner | Influencer" value="💎 Pro Miner | Influencer" oninput="liveUpdateUserField('userBio', this.value)">
              </div>
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Avatar Text/Emoji</label>
                <input type="text" class="modal-input" id="userCtrlAvatar" placeholder="e.g. GF or 🚀" value="TM" maxlength="4" oninput="liveUpdateUserField('userAvatar', this.value)">
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Verification Status</label>
                <select class="modal-input" id="userCtrlVerification" onchange="liveUpdateUserField('verificationStatus', this.value)" style="height: 44px; background: #090e17; color: #fff;">
                  <option value="verified">✅ Verified ✓ (Green Badge)</option>
                  <option value="unverified">✕ Unverified (Action Required)</option>
                  <option value="vip">👑 VIP Premium Member (Gold)</option>
                  <option value="influencer">🌟 Influencer Verified (Purple)</option>
                </select>
              </div>
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">NFT / Tier Badge</label>
                <select class="modal-input" id="userCtrlNftTier" onchange="liveUpdateUserField('nftTier', this.value)" style="height: 44px; background: #090e17; color: #fff;">
                  <option value="non_nft">💎 Non-NFT Holder</option>
                  <option value="genesis">💎 Genesis NFT Holder (+20%)</option>
                  <option value="whale">🐳 Crypto Whale Tier</option>
                  <option value="og">🎖️ OG Pioneer Badge</option>
                </select>
              </div>
            </div>

            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Account Standing</label>
              <select class="modal-input" id="userCtrlStanding" onchange="liveUpdateUserField('accountStanding', this.value)" style="height: 44px; background: #090e17; color: #fff;">
                <option value="active">🟢 Active (Good Standing - Full Access)</option>
                <option value="warning">⚠️ Warning Notice (Shows Alert Banner)</option>
                <option value="frozen">❄️ Suspended / Frozen (Restricted Actions)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- 2. USER BALANCES & FINANCIAL CONTROLS -->
        <div class="admin-card">
          <div class="admin-card-title">
            <span>💰 2. User Balances &amp; Wallets (ব্যালেন্স নিয়ন্ত্রণ)</span>
            <span class="badge-chip verified" style="font-size: 10px;">Live Update</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Directly set or modify In-App Wallet balance, Unclaimed Mining Pool reward, and Total Holdings display.
          </p>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <!-- Wallet Balance -->
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">In-App Wallet Balance (<span class="token-sym">MRG</span>)</label>
              <div style="display: flex; gap: 8px;">
                <input type="number" step="0.1" class="modal-input" id="userCtrlWalletBalance" placeholder="Wallet Balance" value="0.0" style="margin-bottom: 0;">
                <button class="admin-btn green" style="padding: 10px 14px; white-space: nowrap;" onclick="adminSetExactWalletBalance()">Set Exact</button>
              </div>
              <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-top: 6px;">
                <button class="admin-btn" style="padding: 6px 4px; font-size: 11px; background: #1c2b42;" onclick="adminQuickAddBalance(10)">+10</button>
                <button class="admin-btn" style="padding: 6px 4px; font-size: 11px; background: #1c2b42;" onclick="adminQuickAddBalance(50)">+50</button>
                <button class="admin-btn" style="padding: 6px 4px; font-size: 11px; background: #1c2b42;" onclick="adminQuickAddBalance(200)">+200</button>
                <button class="admin-btn red" style="padding: 6px 4px; font-size: 11px;" onclick="adminQuickAddBalance(-50)">-50</button>
              </div>
            </div>

            <!-- Unclaimed Mining Pool -->
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Unclaimed Mining Reward Pool (<span class="token-sym">MRG</span>)</label>
              <div style="display: flex; gap: 8px;">
                <input type="number" step="0.000001" class="modal-input" id="userCtrlUnclaimed" placeholder="Unclaimed Pool" value="0.000000" style="margin-bottom: 0;">
                <button class="admin-btn green" style="padding: 10px 14px; white-space: nowrap;" onclick="adminSetExactUnclaimed()">Set Reward</button>
              </div>
              <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 6px;">
                <button class="admin-btn gold" style="padding: 6px 4px; font-size: 11px;" onclick="adminQuickAddUnclaimed(1.0)">+1.0 Tap Reward</button>
                <button class="admin-btn gold" style="padding: 6px 4px; font-size: 11px;" onclick="adminQuickAddUnclaimed(5.0)">+5.0 Boost</button>
                <button class="admin-btn red" style="padding: 6px 4px; font-size: 11px;" onclick="adminResetUnclaimedZero()">Clear to 0.0</button>
              </div>
            </div>

            <!-- Total Holdings Stat -->
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Total Holding Stat Display (Wallet Tab)</label>
              <input type="text" class="modal-input" id="userCtrlTotalHolding" placeholder="e.g. 2.1K" value="2.1K" oninput="liveUpdateUserField('totalHoldings', this.value)">
            </div>
          </div>
        </div>

        <!-- 3. MINER LEVEL, RIG & HASHRATE CONTROLS -->
        <div class="admin-card">
          <div class="admin-card-title">
            <span>⛏️ 3. Miner Level, Rig &amp; Hashrate (মাইনার ও লেভেল)</span>
            <span class="badge-chip verified" style="font-size: 10px;">Synced</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Set user miner level, peak level record, today's P&amp;L, all-time mined total, base hashrate, and speed multiplier.
          </p>

          <div style="display: flex; flex-direction: column; gap: 10px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Current Miner Level</label>
                <input type="number" class="modal-input" id="userCtrlMinerLevel" placeholder="e.g. 83" value="83" oninput="liveUpdateUserField('minerLevel', parseInt(this.value)||1)">
              </div>
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Peak Level Record</label>
                <input type="number" class="modal-input" id="userCtrlPeakLevel" placeholder="e.g. 103" value="103" oninput="liveUpdateUserField('peakLevel', parseInt(this.value)||1)">
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Today's P&amp;L Display</label>
                <input type="text" class="modal-input" id="userCtrlTodaysPnl" placeholder="e.g. +71.5" value="+71.5" oninput="liveUpdateUserField('todaysPnl', this.value)">
              </div>
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">All-Time Mined Display</label>
                <input type="text" class="modal-input" id="userCtrlAllTimeMined" placeholder="e.g. 2.3K" value="2.3K" oninput="liveUpdateUserField('allTimeMined', this.value)">
              </div>
            </div>

            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Base Mining Hashrate</label>
              <input type="text" class="modal-input" id="userCtrlHashrate" placeholder="e.g. 3.19 TH/s" value="3.19 TH/s" oninput="liveUpdateUserField('baseHashrate', this.value)">
            </div>

            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Mining Speed Multiplier</label>
              <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
                <button class="admin-btn" id="btnMult1" style="padding: 8px 4px; font-size: 12px;" onclick="adminSetUserMultiplier(1)">1x Normal</button>
                <button class="admin-btn gold" id="btnMult2" style="padding: 8px 4px; font-size: 12px;" onclick="adminSetUserMultiplier(2)">2x Boost</button>
                <button class="admin-btn gold" id="btnMult5" style="padding: 8px 4px; font-size: 12px;" onclick="adminSetUserMultiplier(5)">5x Turbo</button>
                <button class="admin-btn red" id="btnMult10" style="padding: 8px 4px; font-size: 12px;" onclick="adminSetUserMultiplier(10)">10x Frenzy</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 4. CONNECTED TON WALLET ADDRESS -->
        <div class="admin-card">
          <div class="admin-card-title">
            <span>🔗 4. Connected TON Wallet (ওয়ালেট কন্ট্রোল)</span>
            <span class="badge-chip verified" style="font-size: 10px;">Wallet Sync</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Set or modify the user's connected TON wallet address. Syncs to Wallet tab, Profile sync bar, and withdrawal forms.
          </p>

          <div style="display: flex; flex-direction: column; gap: 10px;">
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">TON Wallet Address (UQ... / EQ...)</label>
              <input type="text" class="modal-input" id="userCtrlTonWallet" placeholder="UQ..." value="UQBFoMy-deRHYz842P39910y-deRH" oninput="liveUpdateUserField('tonWallet', this.value)">
            </div>
            <div style="display: flex; gap: 8px;">
              <button class="admin-btn" style="flex: 1; padding: 10px; font-size: 12px; background: #1c2b42;" onclick="adminGenerateRandomWallet()">🎲 Generate New Address</button>
              <button class="admin-btn gold" style="flex: 1; padding: 10px; font-size: 12px;" onclick="adminToggleWalletDisconnect()">🚪 Toggle Connect/Disconnect</button>
            </div>
          </div>
        </div>

        <!-- 5. DAILY STREAK & CHECK-IN CONTROLS -->
        <div class="admin-card">
          <div class="admin-card-title">
            <span>📅 5. Daily Streak &amp; Check-in (দৈনিক স্ট্রিক)</span>
            <span class="badge-chip verified" style="font-size: 10px;">Tasks Tab</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Control the user's daily check-in streak day, unlock all 7 days, or toggle today's check-in status.
          </p>

          <div style="display: flex; flex-direction: column; gap: 10px;">
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Set Current Streak Day</label>
              <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px;">
                <button class="admin-btn" style="padding: 8px 0; font-size: 12px;" onclick="adminSetStreakDay(1)">D1</button>
                <button class="admin-btn" style="padding: 8px 0; font-size: 12px;" onclick="adminSetStreakDay(2)">D2</button>
                <button class="admin-btn" style="padding: 8px 0; font-size: 12px;" onclick="adminSetStreakDay(3)">D3</button>
                <button class="admin-btn" style="padding: 8px 0; font-size: 12px;" onclick="adminSetStreakDay(4)">D4</button>
                <button class="admin-btn" style="padding: 8px 0; font-size: 12px;" onclick="adminSetStreakDay(5)">D5</button>
                <button class="admin-btn" style="padding: 8px 0; font-size: 12px;" onclick="adminSetStreakDay(6)">D6</button>
                <button class="admin-btn gold" style="padding: 8px 0; font-size: 12px;" onclick="adminSetStreakDay(7)">★ D7</button>
              </div>
            </div>

            <div style="display: flex; gap: 8px;">
              <button class="admin-btn green" style="flex: 1; padding: 10px; font-size: 12px;" onclick="adminToggleTodayCheckin()">✓ Toggle Today Checked/Unchecked</button>
              <button class="admin-btn gold" style="flex: 1; padding: 10px; font-size: 12px;" onclick="adminUnlockAllStreak()">⭐ Unlock All 7 Days</button>
              <button class="admin-btn red" style="flex: 1; padding: 10px; font-size: 12px;" onclick="adminResetStreak()">🔄 Reset to Day 1</button>
            </div>
          </div>
        </div>

        <!-- 6. SQUAD, REFERRALS & TEAM EARNINGS -->
        <div class="admin-card">
          <div class="admin-card-title">
            <span>👥 6. Squad &amp; Referral Mining (রেফারেল ও টিম)</span>
            <span class="badge-chip verified" style="font-size: 10px;">Friends Tab</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Set invited friends count and total tokens earned from squad mining.
          </p>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 10px;">
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Invited Friends Count</label>
              <div style="display: flex; gap: 6px;">
                <input type="number" class="modal-input" id="userCtrlSquadCount" placeholder="Friends" value="3" style="margin-bottom: 0;" oninput="liveUpdateUserField('squadCount', parseInt(this.value)||0)">
                <button class="admin-btn" style="padding: 10px;" onclick="adminAddSquadFriend(1)">+1</button>
              </div>
            </div>
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Squad Earnings (<span class="token-sym">MRG</span>)</label>
              <div style="display: flex; gap: 6px;">
                <input type="number" step="0.1" class="modal-input" id="userCtrlSquadEarned" placeholder="Earned" value="0.00" style="margin-bottom: 0;" oninput="liveUpdateUserField('squadEarned', parseFloat(this.value)||0)">
                <button class="admin-btn green" style="padding: 10px;" onclick="adminAddSquadReward(25)">+25</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 7. DIRECT ACTIONS: GIFT TOKEN AIRDROP & USER NOTIFICATION -->
        <div class="admin-card" style="border: 1px solid rgba(244, 182, 56, 0.4); background: linear-gradient(135deg, rgba(26, 36, 54, 0.95), rgba(34, 46, 68, 0.95));">
          <div class="admin-card-title">
            <span>🎁 7. Direct Admin Action: Gift Airdrop &amp; Message</span>
            <span class="badge-chip verified" style="font-size: 10px; background: rgba(244, 182, 56, 0.2); color: var(--accent-gold);">Direct Push</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Send an instant token gift directly to this user's wallet with a celebratory transaction, or push a custom alert notice to the user's screen.
          </p>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <!-- Send Token Gift -->
            <div style="background: #0d1522; padding: 12px; border-radius: 12px; border: 1px solid #1c2b42;">
              <div style="font-size: 12px; font-weight: 700; color: #fff; margin-bottom: 8px;">🚀 Send Direct Token Gift / Airdrop</div>
              <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 8px; margin-bottom: 8px;">
                <input type="number" class="modal-input" id="adminGiftAmount" placeholder="Amount (e.g. 100)" value="100" style="margin-bottom: 0;">
                <input type="text" class="modal-input" id="adminGiftReason" placeholder="Reason (e.g. Admin Loyalty Gift)" value="Admin Loyalty Gift" style="margin-bottom: 0;">
              </div>
              <button class="admin-btn green" style="width: 100%; padding: 11px; font-weight: 700;" onclick="adminSendDirectGift()">
                🎁 Send Gift &amp; Credit User Wallet Now
              </button>
            </div>

            <!-- Push Message to User -->
            <div style="background: #0d1522; padding: 12px; border-radius: 12px; border: 1px solid #1c2b42;">
              <div style="font-size: 12px; font-weight: 700; color: #fff; margin-bottom: 8px;">📢 Push Direct Notification / Alert to User Panel</div>
              <input type="text" class="modal-input" id="adminUserMessageInput" placeholder="Write custom alert for user..." value="🎉 Congratulations! You have received special VIP Miner perks." style="margin-bottom: 8px;">
              <div style="display: flex; gap: 8px;">
                <button class="admin-btn" style="flex: 2; padding: 11px; background: #0098ea; font-weight: 700;" onclick="adminPushUserMessage()">
                  📢 Push Notice to User App
                </button>
                <button class="admin-btn red" style="flex: 1; padding: 11px;" onclick="adminClearUserMessage()">
                  ✕ Clear Notice
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- 8. SAVE & APPLY ALL USER CONTROLS BUTTON -->
        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 10px; margin-bottom: 14px;">
          <button class="admin-btn green" style="padding: 16px; font-size: 15px; font-weight: 800; border-radius: 14px; box-shadow: 0 4px 14px rgba(0, 201, 128, 0.4);" onclick="saveAllUserControls()">
            💾 Save All User Controls &amp; Apply to User Panel
          </button>
          <div style="display: flex; gap: 8px;">
            <button class="admin-btn" style="flex: 1; padding: 12px; background: #1c2b42; color: #fff;" onclick="populateUserControlInputs()">
              🔄 Re-sync Inputs from Live State
            </button>
            <button class="admin-btn red" style="flex: 1; padding: 12px;" onclick="resetUserControlsDefault()">
              ⚡ Reset to Defaults
            </button>
          </div>
        </div>

        <!-- Registered Miners Registry List -->
        <div class="admin-card">
          <div class="admin-card-title">
            <span>👥 Registered Miners Registry (Click to Inspect/Edit)</span>
          </div>
          <div style="font-size: 13px; color: var(--text-gray); margin-bottom: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 10px; border-radius: 10px; background: rgba(41, 151, 255, 0.1); border: 1px solid rgba(41, 151, 255, 0.3); margin-bottom: 6px; cursor: pointer;" onclick="loadUserToAdmin('@telegram_miner')">
              <span><strong id="adminRegistryCurrentUser" style="color: #fff;">@telegram_miner</strong> <span style="font-size: 11px; color: var(--accent-blue);">(Current Active)</span></span>
              <span id="adminRegistryCurrentUserStatus" style="color: var(--accent-gold); font-weight: 700;">Level 83 • Active</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 10px; border-radius: 10px; margin-bottom: 6px; cursor: pointer;" onclick="loadUserToAdmin('@alex_ton')">
              <span><strong style="color: #fff;">@alex_ton</strong></span>
              <span style="color: var(--accent-green);">Level 72 • Mining (Load ↗)</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 10px; border-radius: 10px; margin-bottom: 6px; cursor: pointer;" onclick="loadUserToAdmin('@cryptokid')">
              <span><strong style="color: #fff;">@cryptokid</strong></span>
              <span style="color: var(--accent-blue);">Level 65 • Mining (Load ↗)</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 10px; border-radius: 10px; cursor: pointer;" onclick="loadUserToAdmin('@rakib_dhaka')">
              <span><strong style="color: #fff;">@rakib_dhaka</strong></span>
              <span style="color: var(--text-gray);">Level 40 • Idle (Load ↗)</span>
            </div>
          </div>
        </div>
      </div>'''

# Replace admin-sec-users
html = re.sub(
    r'<!-- ADMIN TAB 1: USER CONTROLS -->[\s\S]*?<!-- ADMIN TAB 2: MINING RATES -->',
    admin_users_suite + '\n\n      <!-- ADMIN TAB 2: MINING RATES -->',
    html
)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated template.html markup successfully!")
