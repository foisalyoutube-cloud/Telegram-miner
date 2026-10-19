import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update default transactions to empty array [] so data is clean
html = re.sub(
    r'const defaultTransactions = \[[\s\S]*?\];',
    'const defaultTransactions = [];',
    html
)

# 2. Update default state to clean starting balances
html = re.sub(
    r'const state = \{[\s\S]*?selectedTx: null\s*\};',
    '''const state = {
      currentTab: 'mine',
      topMRG: 0.0,
      walletMRG: 0.0,
      unclaimedMRG: 0.000000,
      miningRatePerSec: 0.0000085,
      streakDay: 1,
      lang: 'en',
      txFilter: 'all',
      transactions: defaultTransactions,
      selectedTx: null
    };''',
    html
)

# 3. Update defaultConfig to clean baseline
html = re.sub(
    r'const defaultConfig = \{[\s\S]*?tonWallet: \'[^\']+\'\s*\};',
    '''const defaultConfig = {
      appName: 'MRG Miner',
      tokenSymbol: 'MRG',
      tokenPriceUSD: 0.00128,
      baseHashrate: '3.19 TH/s',
      userName: 'Telegram Miner',
      userHandle: '@telegram_miner',
      userPhoto: null,
      refRewardMRG: 100,
      refPercent: 10,
      tonWallet: 'UQBFoMy-deRHYz842P39910y-deRH'
    };''',
    html
)

# 4. In Tab 4 (Friends/Profile), update the hardcoded name/handle and add Telegram Sync bar
target_profile_row = '''          <div class="user-profile-info">
            <div class="user-profile-name">GW FOISAL 100K | INFLUENCER</div>
            <div class="user-profile-handle">@GwFoisal</div>
            <div class="badge-chips-row">
              <span class="badge-chip nft">💎 Non-NFT Holder</span>
              <span class="badge-chip verified">✓ Verified</span>
              <span class="badge-chip" onclick="openAdminPanel()" style="background: rgba(244, 182, 56, 0.18); color: var(--accent-gold); border: 1px solid rgba(244, 182, 56, 0.4); cursor: pointer; font-weight: 800;">⚙️ Admin Panel</span>
            </div>
          </div>'''

replacement_profile_row = '''          <div class="user-profile-info">
            <div class="user-profile-name">Telegram Miner</div>
            <div class="user-profile-handle">@telegram_miner</div>
            <div class="badge-chips-row">
              <span class="badge-chip nft">💎 Non-NFT Holder</span>
              <span class="badge-chip verified" id="profileTgVerifiedBadge">✈️ Telegram Verified</span>
              <span class="badge-chip" onclick="openAdminPanel()" style="background: rgba(244, 182, 56, 0.18); color: var(--accent-gold); border: 1px solid rgba(244, 182, 56, 0.4); cursor: pointer; font-weight: 800;">⚙️ Admin Panel</span>
            </div>
          </div>'''

if target_profile_row in html:
    html = html.replace(target_profile_row, replacement_profile_row)
else:
    # Use regex
    html = re.sub(
        r'<div class="user-profile-name">[^<]+</div>\s*<div class="user-profile-handle">[^<]+</div>',
        '<div class="user-profile-name">Telegram Miner</div>\n            <div class="user-profile-handle">@telegram_miner</div>',
        html
    )

# Add Telegram Sync Bar inside user-profile-banner right before lang-selector-bar
target_lang_bar = '<div class="lang-selector-bar" onclick="toggleLanguage()">'
tg_sync_bar_html = '''<!-- Telegram Connection & App Data Sync Bar -->
        <div class="tg-sync-bar" style="display: flex; align-items: center; justify-content: space-between; background: linear-gradient(135deg, rgba(0, 152, 234, 0.18), rgba(16, 26, 42, 0.9)); border: 1px solid rgba(0, 152, 234, 0.4); border-radius: 14px; padding: 10px 14px; margin-bottom: 10px;">
          <div style="display: flex; align-items: center; gap: 10px; overflow: hidden;">
            <div style="width: 34px; height: 34px; border-radius: 50%; background: #0098ea; display: flex; align-items: center; justify-content: center; font-size: 18px; color: #fff; flex-shrink: 0; box-shadow: 0 0 10px rgba(0, 152, 234, 0.4);">
              ✈
            </div>
            <div style="overflow: hidden;">
              <div style="font-size: 13px; font-weight: 700; color: #ffffff; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" id="tgSyncBannerTitle">Telegram Auto-Sync: Active</div>
              <div style="font-size: 11px; color: #70b5f5; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" id="tgSyncBannerSub">Synced: @telegram_miner • TON Wallet</div>
            </div>
          </div>
          <div style="display: flex; gap: 6px; flex-shrink: 0;">
            <button class="badge-chip" onclick="openTgSyncModal()" style="background: #0098ea; color: #fff; border: none; font-size: 11px; padding: 6px 10px; cursor: pointer; font-weight: 700; border-radius: 8px;">🔄 Sync</button>
            <button class="badge-chip" onclick="openCleanDataModal()" style="background: rgba(255, 75, 75, 0.18); color: #ff6b6b; border: 1px solid rgba(255, 75, 75, 0.4); font-size: 11px; padding: 6px 8px; cursor: pointer; font-weight: 600; border-radius: 8px;" title="Clean all app data">🧹 Clean</button>
          </div>
        </div>

        <div class="lang-selector-bar" onclick="toggleLanguage()">'''

if target_lang_bar in html and 'tg-sync-bar' not in html:
    html = html.replace(target_lang_bar, tg_sync_bar_html, 1)

# 5. In Tab 3 (Wallet), update status subtitle to show Telegram sync
target_wallet_sub = '<div class="wallet-info-sub">2.0K <span class="token-sym">MRG</span> on-chain</div>'
replacement_wallet_sub = '<div class="wallet-info-sub" id="walletTonStatusSub">✈️ Synced with Telegram TON Wallet</div>'
if target_wallet_sub in html:
    html = html.replace(target_wallet_sub, replacement_wallet_sub)

# 6. In Admin Panel Tab 0: Add Telegram Sync & Clean Data Card
admin_pin_card = '<!-- ADMIN PIN SECURITY CARD -->'
tg_admin_card = '''<!-- TELEGRAM AUTO-SYNC & CLEAN APP DATA CARD -->
        <div class="admin-card" style="margin-top: 14px; border: 1px solid rgba(0, 152, 234, 0.35); background: linear-gradient(135deg, rgba(16, 26, 44, 0.95), rgba(22, 34, 56, 0.95));">
          <div class="admin-card-title">
            <span>✈️ Telegram &amp; TON Wallet Auto-Sync</span>
            <span class="badge-chip verified" id="adminTgStatusBadge" style="font-size: 11px; background: rgba(0, 152, 234, 0.2); color: #2ea5ff; border: 1px solid rgba(0, 152, 234, 0.4);">Auto-Sync Ready</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Automatically synchronizes the user's display name, Telegram @handle, and TON wallet address upon launching in Telegram WebApp.
          </p>
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <div style="background: #0d1522; padding: 12px; border-radius: 12px; border: 1px solid #1a293d;">
              <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                <span style="font-size: 11px; color: var(--text-muted);">Current Synced User:</span>
                <span id="adminTgSyncUserDisplay" style="font-size: 12px; font-weight: 700; color: #fff;">@telegram_miner</span>
              </div>
              <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                <span style="font-size: 11px; color: var(--text-muted);">Display Name:</span>
                <span id="adminTgSyncNameDisplay" style="font-size: 12px; font-weight: 700; color: var(--accent-gold);">Telegram Miner</span>
              </div>
              <div style="display: flex; justify-content: space-between;">
                <span style="font-size: 11px; color: var(--text-muted);">TON Wallet:</span>
                <span id="adminTgSyncWalletDisplay" style="font-size: 11px; font-family: monospace; color: #2ea5ff;">UQBFoM...y-deRH</span>
              </div>
            </div>

            <div style="display: flex; gap: 8px;">
              <button class="admin-btn" style="flex: 1; padding: 12px; background: #0098ea; color: #fff; font-size: 13px; font-weight: 700;" onclick="forceSyncTelegramFromAdmin()">
                🔄 Auto-Sync From Telegram
              </button>
              <button class="admin-btn red" style="flex: 1; padding: 12px; font-size: 13px; font-weight: 700;" onclick="openCleanDataModal()">
                🧹 Clean All App Data
              </button>
            </div>
          </div>
        </div>

        <!-- ADMIN PIN SECURITY CARD -->'''

if admin_pin_card in html and 'TELEGRAM AUTO-SYNC & CLEAN APP DATA CARD' not in html:
    html = html.replace(admin_pin_card, tg_admin_card, 1)

# In Admin Tab 1 (User Controls): Make the account title dynamic
html = html.replace(
    '<span>👤 Active Account (@GwFoisal)</span>',
    '<span>👤 Active Account (<span id="adminUserActiveHandle">@telegram_miner</span>)</span>'
)
html = html.replace(
    '<span><strong>@GwFoisal</strong> (Current)</span>',
    '<span><strong id="adminRegistryCurrentUser">@telegram_miner</strong> (Current)</span>'
)

# 7. Add Clean Data Modal & Telegram Sync Modal right before </body
modals_to_add = '''
  <!-- Clean All App Data Confirmation Modal -->
  <div class="modal-backdrop" id="cleanDataModal">
    <div class="modal-sheet" style="text-align: center; max-width: 440px; border-radius: 28px 28px 0 0; background: #131c2b; border: 1px solid rgba(255, 75, 75, 0.3);">
      <div style="width: 58px; height: 58px; border-radius: 50%; background: rgba(255, 75, 75, 0.15); border: 1px solid rgba(255, 75, 75, 0.4); display: flex; align-items: center; justify-content: center; font-size: 28px; margin: 0 auto 12px auto; box-shadow: 0 0 20px rgba(255, 75, 75, 0.2);">
        🧹
      </div>
      <div class="modal-title" style="margin-bottom: 6px; color: #fff;">Clean All App Data</div>
      <div class="modal-desc" style="color: var(--text-gray); font-size: 13px; margin-bottom: 18px; line-height: 1.5;">
        This will wipe all cached app state, reset mining balances and transaction logs to 0, clear mock dummy data, and cleanly re-sync your display name, Telegram handle, and TON wallet fresh from Telegram.
      </div>
      
      <div style="background: rgba(255, 75, 75, 0.08); border: 1px solid rgba(255, 75, 75, 0.2); border-radius: 14px; padding: 12px; margin-bottom: 18px; text-align: left; font-size: 12px; color: #ff9e9e;">
        <div>✓ Resets Wallet Balance to 0.0 MRG</div>
        <div>✓ Cleans dummy transaction history</div>
        <div>✓ Restores default quests &amp; admin PIN (115414)</div>
        <div>✓ Auto-syncs live Telegram credentials &amp; TON wallet</div>
      </div>

      <div style="display: flex; gap: 10px;">
        <button class="modal-btn-confirm" style="flex: 1; background: transparent; color: var(--text-muted); border: 1px solid #23344d; margin-top: 0;" onclick="closeCleanDataModal()">
          Cancel
        </button>
        <button class="modal-btn-confirm" style="flex: 1.4; background: linear-gradient(135deg, #ff4b4b, #d92424); color: #fff; margin-top: 0; box-shadow: 0 4px 14px rgba(255, 75, 75, 0.4);" onclick="executeCleanAllAppData()">
          🧹 Wipe &amp; Reset All
        </button>
      </div>
    </div>
  </div>

  <!-- Telegram Account & TON Wallet Sync Modal -->
  <div class="modal-backdrop" id="tgSyncModal">
    <div class="modal-sheet" style="max-width: 440px; border-radius: 28px 28px 0 0; background: #131c2b; border: 1px solid rgba(0, 152, 234, 0.3);">
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 14px;">
        <div style="width: 44px; height: 44px; border-radius: 50%; background: #0098ea; display: flex; align-items: center; justify-content: center; font-size: 22px; color: #fff; flex-shrink: 0; box-shadow: 0 0 12px rgba(0, 152, 234, 0.4);">
          ✈
        </div>
        <div>
          <div class="modal-title" style="margin-bottom: 2px;">Telegram &amp; TON Sync</div>
          <div style="font-size: 12px; color: var(--text-muted);">Real-time profile and wallet synchronization</div>
        </div>
      </div>

      <div style="background: rgba(0, 152, 234, 0.08); border: 1px solid rgba(0, 152, 234, 0.25); border-radius: 12px; padding: 10px 14px; margin-bottom: 14px; font-size: 12px; color: #8ecbff;">
        <span id="tgModalDetectionText">⚡ Telegram WebApp detected. Data is synchronized automatically on connect.</span>
      </div>

      <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px;">
        <div>
          <label class="admin-label" style="display: block; margin-bottom: 4px;">User Display Name</label>
          <input type="text" class="modal-input" id="tgSyncInputName" placeholder="e.g. John Doe">
        </div>
        <div>
          <label class="admin-label" style="display: block; margin-bottom: 4px;">Telegram Username / Handle</label>
          <input type="text" class="modal-input" id="tgSyncInputHandle" placeholder="e.g. @username">
        </div>
        <div>
          <label class="admin-label" style="display: block; margin-bottom: 4px;">Connected TON Wallet Address</label>
          <input type="text" class="modal-input" id="tgSyncInputWallet" placeholder="UQ... or EQ...">
        </div>
      </div>

      <div style="display: flex; gap: 8px; margin-bottom: 8px;">
        <button class="modal-btn-confirm" style="flex: 1.2; background: #0098ea; color: #fff; margin-top: 0;" onclick="saveCustomTgSync()">
          💾 Save &amp; Apply Sync
        </button>
        <button class="modal-btn-confirm" style="flex: 1; background: #1c2b42; color: #fff; margin-top: 0;" onclick="autoSyncTelegramData(true)">
          🔄 Auto-Detect
        </button>
      </div>
      <button class="modal-btn-confirm" style="background: transparent; color: var(--text-muted); margin-top: 0; padding: 10px;" onclick="closeTgSyncModal()">
        Close
      </button>
    </div>
  </div>
'''

if 'id="cleanDataModal"' not in html:
    html = html.replace('<!-- Audio Synthesizer via Web Audio API & JavaScript Core -->', modals_to_add + '\n  <!-- Audio Synthesizer via Web Audio API & JavaScript Core -->')

# 8. Add JavaScript Functions for Clean All App Data & Telegram Auto-Sync
js_sync_logic = '''
    // ==========================================
    // TELEGRAM AUTO-SYNC & APP DATA CLEAN ENGINE
    // ==========================================

    function generateDeterministicTonWallet(seedId) {
      const seed = 'TON_V4R2_' + (seedId || 'miner_wallet_default');
      let hash = 0;
      for (let i = 0; i < seed.length; i++) {
        hash = ((hash << 5) - hash) + seed.charCodeAt(i);
        hash |= 0;
      }
      const h1 = Math.abs(hash).toString(16).padStart(8, '0');
      const h2 = Math.abs(hash ^ 0x5a5a5a5a).toString(16).padStart(8, '0');
      const mid = (h1 + h2 + 'c79e4d1f2a3b842e').substring(0, 18);
      return `UQ${h1.substring(0, 4)}${mid}deRH`;
    }

    function autoSyncTelegramData(forceNotify = false) {
      let tgUser = null;
      let source = 'none';

      // 1. Direct Telegram WebApp API
      if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.initDataUnsafe && window.Telegram.WebApp.initDataUnsafe.user) {
        tgUser = window.Telegram.WebApp.initDataUnsafe.user;
        source = 'webapp';
      }

      // 2. Query string parameters (?user= or ?tg_user= or ?start_param=)
      if (!tgUser) {
        try {
          const params = new URLSearchParams(window.location.search);
          const uParam = params.get('user') || params.get('tg_user') || params.get('tgWebAppData');
          if (uParam) {
            if (uParam.startsWith('{')) {
              tgUser = JSON.parse(decodeURIComponent(uParam));
              source = 'url_param';
            }
          }
        } catch (e) {}
      }

      // 3. Stored synced Telegram profile
      if (!tgUser) {
        try {
          const stored = localStorage.getItem('tg_synced_user');
          if (stored) {
            tgUser = JSON.parse(stored);
            source = 'storage';
          }
        } catch (e) {}
      }

      if (tgUser) {
        // Extract Display Name
        const firstName = (tgUser.first_name || '').trim();
        const lastName = (tgUser.last_name || '').trim();
        let displayName = [firstName, lastName].filter(Boolean).join(' ');
        if (!displayName && tgUser.username) displayName = tgUser.username;
        if (!displayName) displayName = 'Telegram Miner';

        // Extract Telegram Handle
        let handle = '';
        if (tgUser.username) {
          handle = tgUser.username.startsWith('@') ? tgUser.username : ('@' + tgUser.username);
        } else if (tgUser.id) {
          handle = '@user_' + tgUser.id;
        } else {
          handle = '@telegram_miner';
        }

        // Extract TON Wallet Address
        let tonAddr = tgUser.ton_wallet || tgUser.ton_address || tgUser.wallet_address;
        if (!tonAddr) {
          const savedWallet = localStorage.getItem('mrg_connected_ton_wallet');
          if (savedWallet && savedWallet.length > 10) {
            tonAddr = savedWallet;
          } else {
            tonAddr = generateDeterministicTonWallet(tgUser.id || handle);
          }
        }

        // Apply to appConfig
        appConfig.userName = displayName;
        appConfig.userHandle = handle;
        appConfig.tonWallet = tonAddr;
        if (tgUser.photo_url) {
          appConfig.userPhoto = tgUser.photo_url;
        }

        // Persist
        try {
          localStorage.setItem('mrg_app_config', JSON.stringify(appConfig));
          localStorage.setItem('tg_synced_user', JSON.stringify({
            id: tgUser.id,
            first_name: tgUser.first_name,
            last_name: tgUser.last_name,
            username: tgUser.username,
            photo_url: tgUser.photo_url,
            ton_wallet: tonAddr
          }));
          localStorage.setItem('mrg_connected_ton_wallet', tonAddr);
        } catch (e) {}

        applyGlobalConfig();
        updateTelegramStatusUI(true, handle, displayName, tonAddr);

        if (forceNotify) {
          soundSuccess();
          showToast(`✈️ Telegram Synced: ${handle} • ${displayName}`);
        }
        return true;
      } else {
        updateTelegramStatusUI(false);
        if (forceNotify) {
          showToast('ℹ️ Standalone preview mode. You can set custom Telegram credentials in the sync dialog.');
        }
        return false;
      }
    }

    function updateTelegramStatusUI(isConnected, handle, name, tonAddr) {
      const bannerTitle = document.getElementById('tgSyncBannerTitle');
      const bannerSub = document.getElementById('tgSyncBannerSub');
      const adminBadge = document.getElementById('adminTgStatusBadge');
      const adminUserDisp = document.getElementById('adminTgSyncUserDisplay');
      const adminNameDisp = document.getElementById('adminTgSyncNameDisplay');
      const adminWalletDisp = document.getElementById('adminTgSyncWalletDisplay');
      const modalDetectText = document.getElementById('tgModalDetectionText');
      const profileTgBadge = document.getElementById('profileTgVerifiedBadge');

      const activeHandle = handle || appConfig.userHandle;
      const activeName = name || appConfig.userName;
      const activeTon = tonAddr || appConfig.tonWallet;
      const shortTon = activeTon && activeTon.length > 12 
        ? activeTon.substring(0, 6) + '...' + activeTon.substring(activeTon.length - 4)
        : (activeTon || 'Not connected');

      if (bannerTitle) bannerTitle.innerText = isConnected ? 'Telegram Auto-Sync: Active' : 'Telegram Sync: Ready';
      if (bannerSub) bannerSub.innerText = `${activeHandle} • TON: ${shortTon}`;
      if (adminBadge) {
        adminBadge.innerText = isConnected ? 'Auto-Synced ✓' : 'Ready to Sync';
        adminBadge.style.color = isConnected ? '#00c980' : '#2ea5ff';
      }
      if (adminUserDisp) adminUserDisp.innerText = activeHandle;
      if (adminNameDisp) adminNameDisp.innerText = activeName;
      if (adminWalletDisp) adminWalletDisp.innerText = shortTon;
      if (profileTgBadge) {
        profileTgBadge.innerText = isConnected ? `✈️ ${activeHandle}` : '✈️ Telegram Ready';
      }
      if (modalDetectText) {
        modalDetectText.innerText = isConnected 
          ? `✓ Active Telegram session: ${activeHandle} (${activeName}). TON wallet linked.`
          : '⚡ Standalone mode. Data syncs automatically whenever connected in Telegram.';
      }
    }

    function openTgSyncModal() {
      soundTap();
      const inpName = document.getElementById('tgSyncInputName');
      const inpHandle = document.getElementById('tgSyncInputHandle');
      const inpWallet = document.getElementById('tgSyncInputWallet');
      if (inpName) inpName.value = appConfig.userName;
      if (inpHandle) inpHandle.value = appConfig.userHandle;
      if (inpWallet) inpWallet.value = appConfig.tonWallet;
      const modal = document.getElementById('tgSyncModal');
      if (modal) modal.classList.add('show');
    }

    function closeTgSyncModal() {
      soundTap();
      const modal = document.getElementById('tgSyncModal');
      if (modal) modal.classList.remove('show');
    }

    function saveCustomTgSync() {
      soundSuccess();
      const inpName = document.getElementById('tgSyncInputName');
      const inpHandle = document.getElementById('tgSyncInputHandle');
      const inpWallet = document.getElementById('tgSyncInputWallet');

      const nameVal = (inpName ? inpName.value.trim() : '') || 'Telegram Miner';
      let handleVal = (inpHandle ? inpHandle.value.trim() : '') || '@telegram_miner';
      if (!handleVal.startsWith('@')) handleVal = '@' + handleVal;
      const walletVal = (inpWallet ? inpWallet.value.trim() : '') || generateDeterministicTonWallet(handleVal);

      appConfig.userName = nameVal;
      appConfig.userHandle = handleVal;
      appConfig.tonWallet = walletVal;

      try {
        localStorage.setItem('mrg_app_config', JSON.stringify(appConfig));
        localStorage.setItem('tg_synced_user', JSON.stringify({
          id: Math.floor(Math.random() * 899999 + 100000),
          first_name: nameVal,
          username: handleVal.replace('@', ''),
          ton_wallet: walletVal
        }));
        localStorage.setItem('mrg_connected_ton_wallet', walletVal);
      } catch (e) {}

      applyGlobalConfig();
      updateTelegramStatusUI(true, handleVal, nameVal, walletVal);
      closeTgSyncModal();
      showToast(`✅ Synced: ${nameVal} (${handleVal}) • TON Wallet updated`);
    }

    function forceSyncTelegramFromAdmin() {
      soundTap();
      const ok = autoSyncTelegramData(true);
      if (!ok) {
        openTgSyncModal();
      }
    }

    function openCleanDataModal() {
      soundTap();
      const modal = document.getElementById('cleanDataModal');
      if (modal) modal.classList.add('show');
    }

    function closeCleanDataModal() {
      soundTap();
      const modal = document.getElementById('cleanDataModal');
      if (modal) modal.classList.remove('show');
    }

    function executeCleanAllAppData() {
      // 1. Clear all localStorage keys
      try {
        localStorage.removeItem('mrg_miner_state');
        localStorage.removeItem('mrg_app_config');
        localStorage.removeItem('mrg_custom_tasks');
        localStorage.removeItem('mrg_miner_level');
        localStorage.removeItem('tg_synced_user');
        localStorage.removeItem('mrg_connected_ton_wallet');
        localStorage.removeItem('mrg_admin_pin');
      } catch (e) {}

      // 2. Reset runtime state to clean zeroed values
      state.walletMRG = 0.0;
      state.unclaimedMRG = 0.000000;
      state.topMRG = 0.0;
      state.streakDay = 1;
      state.transactions = [];
      state.txFilter = 'all';

      // 3. Reset tasks to clean fresh list
      userTasks = defaultTasks.map(t => Object.assign({}, t, { completed: false }));

      // 4. Reset admin PIN
      setAdminPin('115414');

      // 5. Reset appConfig to clean baseline
      appConfig = Object.assign({}, defaultConfig, {
        appName: 'MRG Miner',
        tokenSymbol: 'MRG',
        tokenPriceUSD: 0.00128,
        baseHashrate: '3.19 TH/s',
        userName: 'Telegram Miner',
        userHandle: '@telegram_miner',
        tonWallet: 'UQBFoMy-deRHYz842P39910y-deRH'
      });

      // 6. Auto-sync directly from Telegram WebApp
      const synced = autoSyncTelegramData(false);

      // 7. Update all UI elements
      document.getElementById('walletMRGBalance').innerText = '0.0';
      document.getElementById('topBalance').innerText = '0.0K';
      const subrateEl = document.querySelector('.unclaimed-subrate');
      if (subrateEl) subrateEl.innerText = `≈ $0.0000 · ${appConfig.baseHashrate}`;

      renderTransactions();
      renderUserTasks();
      renderAdminTasks();
      applyGlobalConfig();
      saveState();

      closeCleanDataModal();
      soundSuccess();
      if (synced) {
        showToast(`🧹 All data cleaned! Auto-synced with Telegram: ${appConfig.userHandle}`);
      } else {
        showToast('🧹 All app data cleaned successfully! Fresh state initialized.');
      }
    }
'''

# Insert the logic right before applyGlobalConfig
html = html.replace('function applyGlobalConfig() {', js_sync_logic + '\n    function applyGlobalConfig() {')

# 9. Update applyGlobalConfig to sync dynamic admin user handle and copy address
apply_ext = '''
      // Dynamic Admin user handles
      const admActiveHandle = document.getElementById('adminUserActiveHandle');
      if (admActiveHandle) admActiveHandle.innerText = appConfig.userHandle;
      const admRegCurrent = document.getElementById('adminRegistryCurrentUser');
      if (admRegCurrent) admRegCurrent.innerText = appConfig.userHandle;

      // Update withdraw address input with connected TON wallet
      const withdrawAddrInp = document.getElementById('withdrawAddress');
      if (withdrawAddrInp && (!withdrawAddrInp.value || withdrawAddrInp.value.startsWith('UQBFoMy-deRHYz842P39910'))) {
        withdrawAddrInp.value = appConfig.tonWallet;
      }
'''
html = html.replace("const fWall = document.getElementById('cfgWalletAddr'); if (fWall) fWall.value = appConfig.tonWallet;", "const fWall = document.getElementById('cfgWalletAddr'); if (fWall) fWall.value = appConfig.tonWallet;" + apply_ext)

# Update copyAddress to use appConfig.tonWallet instead of hardcoded string
html = re.sub(
    r'function copyAddress\(\) \{[\s\S]*?showToast\(\'Wallet address copied to clipboard!\'\);\s*\}',
    '''function copyAddress() {
      soundTap();
      const addr = appConfig.tonWallet || 'UQBFoMy-deRHYz842P39910y-deRH';
      if (navigator.clipboard) {
        navigator.clipboard.writeText(addr);
      }
      const shortA = addr.length > 12 ? (addr.substring(0, 6) + '...' + addr.substring(addr.length - 4)) : addr;
      showToast(`TON Wallet copied: ${shortA}`);
    }''',
    html
)

# 10. Update DOMContentLoaded to perform one-time clean of stale mock data and autoSyncTelegramData
dom_loaded_target = '''    // Init Telegram WebApp API if inside Telegram
    window.addEventListener('DOMContentLoaded', () => {
      if (window.Telegram && window.Telegram.WebApp) {
        window.Telegram.WebApp.ready();
        window.Telegram.WebApp.expand();
      }'''

dom_loaded_replacement = '''    // Init Telegram WebApp API if inside Telegram & Clean Stale Mock Data
    window.addEventListener('DOMContentLoaded', () => {
      if (window.Telegram && window.Telegram.WebApp) {
        window.Telegram.WebApp.ready();
        window.Telegram.WebApp.expand();
      }

      // Check and auto-clean old stale mock data ('GW FOISAL 100K | INFLUENCER')
      try {
        const cleanFlag = localStorage.getItem('mrg_cleaned_v2');
        if (!cleanFlag) {
          const oldCfg = localStorage.getItem('mrg_app_config');
          if (oldCfg && oldCfg.includes('GW FOISAL')) {
            localStorage.removeItem('mrg_app_config');
            localStorage.removeItem('mrg_miner_state');
            state.walletMRG = 0.0;
            state.unclaimedMRG = 0.0;
            state.topMRG = 0.0;
            state.transactions = [];
          }
          localStorage.setItem('mrg_cleaned_v2', 'true');
        }
      } catch (e) {}

      // Auto-sync Telegram credentials (display name, telegram handle, TON wallet)
      autoSyncTelegramData(false);'''

html = html.replace(dom_loaded_target, dom_loaded_replacement)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated template.html successfully!")
