import re

with open('template.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace all static MRG token labels with class="token-sym"
# 1. Top bar: <span class="currency">MRG</span> -> <span class="currency token-sym">MRG</span>
text = text.replace('<span class="currency">MRG</span>', '<span class="currency token-sym">MRG</span>')

# 2. Mine tab: <span class="curr">MRG</span> -> <span class="curr token-sym">MRG</span>
text = text.replace('<span class="curr">MRG</span>', '<span class="curr token-sym">MRG</span>')

# 3. Mine button: <span>Claim Reward · <span id="btnClaimVal">0.00</span> MRG</span>
text = text.replace('<span>Claim Reward · <span id="btnClaimVal">0.00</span> MRG</span>',
                    '<span>Claim Reward · <span id="btnClaimVal">0.00</span> <span class="token-sym">MRG</span></span>')

# 4. Level progress: <span class="remain">3.0 MRG to go</span>
text = text.replace('<span class="remain">3.0 MRG to go</span>',
                    '<span class="remain">3.0 <span class="token-sym">MRG</span> to go</span>')

# 5. Performance sub: All-Time Mined: 2.3K MRG
text = text.replace('All-Time Mined: 2.3K MRG',
                    'All-Time Mined: 2.3K <span class="token-sym">MRG</span>')

# 6. DEX buy title: Buy MRG on DEX
text = text.replace('Buy MRG on DEX', 'Buy <span class="token-sym">MRG</span> on DEX')
text = text.replace('Swap GRAM for MRG on STON.fi', 'Swap GRAM for <span class="token-sym">MRG</span> on STON.fi')

# 7. Wallet Tab:
text = text.replace('<span>Buy MRG</span>', '<span>Buy <span class="token-sym">MRG</span></span>')
text = text.replace('2.0K MRG on-chain', '2.0K <span class="token-sym">MRG</span> on-chain')
text = text.replace('Total MRG Holding', 'Total <span class="token-sym">MRG</span> Holding')
text = text.replace('<div class="miner-stat-val" style="color: #fff;">2.1K MRG</div>',
                    '<div class="miner-stat-val" style="color: #fff;">2.1K <span class="token-sym">MRG</span></div>')
text = text.replace('Withdraw MRG', 'Withdraw <span class="token-sym">MRG</span>')
text = text.replace('Buy MRG on STON.fi', 'Buy <span class="token-sym">MRG</span> on STON.fi')

# Update Admin Tabs to include "Branding & Token" as first tab
old_nav_tabs = """      <!-- Admin Tabs Navigation -->
      <div class="admin-nav-tabs">
        <div class="admin-tab-btn active" onclick="switchAdminTab('users', this)">User Controls</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('mining', this)">Mining Rates</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('tasks', this)">Tasks &amp; Quests</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('withdrawals', this)">Withdrawals</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('broadcast', this)">Broadcast</div>
      </div>"""

new_nav_tabs = """      <!-- Admin Tabs Navigation -->
      <div class="admin-nav-tabs">
        <div class="admin-tab-btn active" onclick="switchAdminTab('branding', this)">🏷️ App &amp; Token</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('users', this)">User Controls</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('mining', this)">Mining Rates</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('tasks', this)">Tasks &amp; Quests</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('withdrawals', this)">Withdrawals</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('broadcast', this)">Broadcast</div>
      </div>"""

text = text.replace(old_nav_tabs, new_nav_tabs)

# Add Branding Section as first admin section
branding_section = """
      <!-- ADMIN TAB 0: BRANDING & TOKEN SETTINGS -->
      <div class="admin-tab-section active" id="admin-sec-branding">
        <div class="admin-card">
          <div class="admin-card-title">
            <span>🏷️ App &amp; Token Customization</span>
            <span class="badge-chip verified" style="font-size: 11px;">Live Config</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 16px;">
            Customize token name, app name, exchange rate, and profile details across the entire application in real time.
          </p>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">App Name</label>
              <input type="text" class="modal-input" id="cfgAppName" placeholder="e.g. MRG Miner Bot" value="MRG Miner">
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Token Symbol</label>
                <input type="text" class="modal-input" id="cfgTokenSymbol" placeholder="e.g. MRG, NOT, DOGS" value="MRG">
              </div>
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Token Price ($ USD)</label>
                <input type="number" step="0.0001" class="modal-input" id="cfgTokenPrice" placeholder="0.00128" value="0.00128">
              </div>
            </div>

            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Base Mining Hashrate</label>
              <input type="text" class="modal-input" id="cfgHashrate" placeholder="e.g. 3.19 TH/s" value="3.19 TH/s">
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">User Display Name</label>
                <input type="text" class="modal-input" id="cfgUserName" placeholder="Name" value="GW FOISAL 100K | INFLUENCER">
              </div>
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Telegram Handle</label>
                <input type="text" class="modal-input" id="cfgUserHandle" placeholder="@Handle" value="@GwFoisal">
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Referral Bonus</label>
                <input type="number" class="modal-input" id="cfgRefReward" placeholder="Tokens" value="100">
              </div>
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Squad Commission %</label>
                <input type="number" class="modal-input" id="cfgRefPercent" placeholder="%" value="10">
              </div>
            </div>

            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Connected TON Wallet Address</label>
              <input type="text" class="modal-input" id="cfgWalletAddr" placeholder="UQ..." value="UQBFoMy-deRHYz842P39910y-deRH">
            </div>

            <div style="display: flex; gap: 8px; margin-top: 6px;">
              <button class="admin-btn green" style="flex: 2; padding: 14px; font-size: 14px;" onclick="saveGlobalConfig()">
                💾 Save &amp; Apply All Changes
              </button>
              <button class="admin-btn" style="flex: 1; padding: 14px; background: #1c2b42; color: var(--text-gray);" onclick="resetGlobalConfig()">
                🔄 Reset
              </button>
            </div>
          </div>
        </div>
      </div>
"""

# Make admin-sec-users non-active initially since branding is now active
text = text.replace('<div class="admin-tab-section active" id="admin-sec-users">',
                    '<div class="admin-tab-section" id="admin-sec-users">')

text = text.replace('<!-- ADMIN TAB 1: USER CONTROLS -->',
                    branding_section + '\n      <!-- ADMIN TAB 1: USER CONTROLS -->')

# Update Javascript state & config engine
config_js = """
    // ==========================================
    // GLOBAL APP & TOKEN CONFIGURATION ENGINE
    // ==========================================
    const defaultConfig = {
      appName: 'MRG Miner',
      tokenSymbol: 'MRG',
      tokenPriceUSD: 0.00128,
      baseHashrate: '3.19 TH/s',
      userName: 'GW FOISAL 100K | INFLUENCER',
      userHandle: '@GwFoisal',
      refRewardMRG: 100,
      refPercent: 10,
      tonWallet: 'UQBFoMy-deRHYz842P39910y-deRH'
    };

    let appConfig = Object.assign({}, defaultConfig);

    try {
      const savedCfg = localStorage.getItem('mrg_app_config');
      if (savedCfg) {
        appConfig = Object.assign(appConfig, JSON.parse(savedCfg));
      }
    } catch (e) {}

    function applyGlobalConfig() {
      // 1. App Title
      document.title = appConfig.appName + ' Bot';
      const pageTitleEl = document.getElementById('pageTitle');
      if (pageTitleEl) pageTitleEl.innerText = appConfig.appName + ' Bot';

      // 2. Token Symbol across all elements
      document.querySelectorAll('.token-sym').forEach(el => {
        el.innerText = appConfig.tokenSymbol;
      });

      // 3. User Profile Info
      const profileName = document.querySelector('.user-profile-name');
      if (profileName) profileName.innerText = appConfig.userName;
      const profileHandle = document.querySelector('.user-profile-handle');
      if (profileHandle) profileHandle.innerText = appConfig.userHandle;

      // 4. Avatars initials
      const initials = appConfig.userName.split(' ').map(n => n[0]).slice(0, 2).join('').toUpperCase() || 'MR';
      document.querySelectorAll('.user-avatar-small').forEach(el => el.innerText = initials);
      const userProfilePic = document.querySelector('.user-profile-pic');
      if (userProfilePic) userProfilePic.innerText = initials;

      // 5. Mining Speed
      const speedEls = document.querySelectorAll('.miner-stat-val');
      if (speedEls.length > 0) speedEls[0].innerText = appConfig.baseHashrate;
      const subrateEl = document.querySelector('.unclaimed-subrate');
      if (subrateEl) {
        subrateEl.innerText = `≈ $${(state.unclaimedMRG * appConfig.tokenPriceUSD).toFixed(4)} · ${appConfig.baseHashrate}`;
      }

      // 6. Referral Card
      const inviteSubtitle = document.querySelector('#tab-friends .hero-subtitle');
      if (inviteSubtitle) {
        inviteSubtitle.innerText = `Get +${appConfig.refRewardMRG} ${appConfig.tokenSymbol} for every friend who starts mining, plus ${appConfig.refPercent}% of their mining output — forever.`;
      }
      const refCleanName = appConfig.appName.toLowerCase().replace(/[^a-z0-9]/g, '') || 'mrgminer';
      const refTextEl = document.getElementById('refLinkText');
      if (refTextEl) {
        refTextEl.innerText = `t.me/${refCleanName}bot/app?startapp=ref_DDAWR83`;
      }

      // 7. Wallet Address
      const tonAddressEl = document.getElementById('tonAddress');
      if (tonAddressEl) {
        const shortAddr = appConfig.tonWallet.length > 12 
          ? appConfig.tonWallet.substring(0, 6) + '...' + appConfig.tonWallet.substring(appConfig.tonWallet.length - 6)
          : appConfig.tonWallet;
        tonAddressEl.innerText = shortAddr;
      }

      // 8. Wallet USD balance
      const walletSubEl = document.querySelector('#tab-wallet .unclaimed-subrate');
      if (walletSubEl) {
        walletSubEl.innerText = `≈ $${(state.walletMRG * appConfig.tokenPriceUSD).toFixed(2)}`;
      }

      // 9. Synchronize Admin input fields
      const fApp = document.getElementById('cfgAppName'); if (fApp) fApp.value = appConfig.appName;
      const fSym = document.getElementById('cfgTokenSymbol'); if (fSym) fSym.value = appConfig.tokenSymbol;
      const fPrice = document.getElementById('cfgTokenPrice'); if (fPrice) fPrice.value = appConfig.tokenPriceUSD;
      const fHash = document.getElementById('cfgHashrate'); if (fHash) fHash.value = appConfig.baseHashrate;
      const fUser = document.getElementById('cfgUserName'); if (fUser) fUser.value = appConfig.userName;
      const fHandle = document.getElementById('cfgUserHandle'); if (fHandle) fHandle.value = appConfig.userHandle;
      const fRef = document.getElementById('cfgRefReward'); if (fRef) fRef.value = appConfig.refRewardMRG;
      const fPct = document.getElementById('cfgRefPercent'); if (fPct) fPct.value = appConfig.refPercent;
      const fWall = document.getElementById('cfgWalletAddr'); if (fWall) fWall.value = appConfig.tonWallet;
    }

    function saveGlobalConfig() {
      soundSuccess();
      appConfig.appName = document.getElementById('cfgAppName').value.trim() || 'MRG Miner';
      appConfig.tokenSymbol = document.getElementById('cfgTokenSymbol').value.trim().toUpperCase() || 'MRG';
      appConfig.tokenPriceUSD = parseFloat(document.getElementById('cfgTokenPrice').value) || 0.00128;
      appConfig.baseHashrate = document.getElementById('cfgHashrate').value.trim() || '3.19 TH/s';
      appConfig.userName = document.getElementById('cfgUserName').value.trim() || 'GW FOISAL';
      appConfig.userHandle = document.getElementById('cfgUserHandle').value.trim() || '@GwFoisal';
      appConfig.refRewardMRG = parseFloat(document.getElementById('cfgRefReward').value) || 100;
      appConfig.refPercent = parseFloat(document.getElementById('cfgRefPercent').value) || 10;
      appConfig.tonWallet = document.getElementById('cfgWalletAddr').value.trim() || 'UQBFoMy-deRH';

      try {
        localStorage.setItem('mrg_app_config', JSON.stringify(appConfig));
      } catch (e) {}

      applyGlobalConfig();
      renderTransactions();
      showToast(`✅ Saved! App: ${appConfig.appName} • Token: ${appConfig.tokenSymbol}`);
    }

    function resetGlobalConfig() {
      soundTap();
      appConfig = Object.assign({}, defaultConfig);
      try {
        localStorage.removeItem('mrg_app_config');
      } catch (e) {}
      applyGlobalConfig();
      renderTransactions();
      showToast('Config reset to default MRG settings.');
    }
"""

text = text.replace("    // Transaction History Functions", config_js + "\n    // Transaction History Functions")

# Call applyGlobalConfig() on DOMContentLoaded
old_dom_ready = "renderTransactions();"
new_dom_ready = "renderTransactions();\n      applyGlobalConfig();"
text = text.replace(old_dom_ready, new_dom_ready)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Branding & Token customization applied to template.html successfully!")
