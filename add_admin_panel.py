import re

with open('template.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add Admin CSS
admin_css = """
    /* ====================================================
       ADMIN PANEL STYLES
    ==================================================== */
    .admin-viewport {
      display: none;
      flex-direction: column;
      position: fixed;
      inset: 0;
      background: #090e17;
      z-index: 200;
      overflow-y: auto;
      padding-bottom: 40px;
      animation: fadeIn 0.2s ease forwards;
    }
    .admin-viewport.active {
      display: flex;
    }

    .admin-header-bar {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(9, 14, 23, 0.96);
      backdrop-filter: blur(12px);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 18px;
      border-bottom: 1px solid rgba(244, 182, 56, 0.2);
    }
    .admin-back-btn {
      display: flex;
      align-items: center;
      gap: 6px;
      color: var(--accent-gold);
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
    }
    .admin-badge-pill {
      background: rgba(244, 182, 56, 0.15);
      border: 1px solid rgba(244, 182, 56, 0.35);
      color: var(--accent-gold);
      font-size: 11px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 14px;
      letter-spacing: 0.5px;
    }

    .admin-inner {
      max-width: 480px;
      margin: 0 auto;
      width: 100%;
      padding: 16px;
    }

    .admin-stats-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 18px;
    }
    .admin-stat-card {
      background: #111a28;
      border: 1px solid #1c2b42;
      border-radius: 16px;
      padding: 14px;
    }
    .admin-stat-card .title {
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }
    .admin-stat-card .val {
      font-size: 20px;
      font-weight: 900;
      color: #ffffff;
    }
    .admin-stat-card .sub {
      font-size: 11px;
      color: var(--accent-green);
      margin-top: 2px;
      font-weight: 600;
    }

    .admin-nav-tabs {
      display: flex;
      gap: 6px;
      background: #101826;
      border: 1px solid #1a283e;
      border-radius: 16px;
      padding: 5px;
      margin-bottom: 18px;
      overflow-x: auto;
    }
    .admin-tab-btn {
      flex: 1;
      text-align: center;
      padding: 8px 10px;
      font-size: 12px;
      font-weight: 700;
      color: var(--text-gray);
      border-radius: 12px;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }
    .admin-tab-btn.active {
      background: var(--accent-blue);
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(41, 151, 255, 0.3);
    }

    .admin-tab-section {
      display: none;
    }
    .admin-tab-section.active {
      display: block;
    }

    .admin-card {
      background: #111a28;
      border: 1px solid #1c2b42;
      border-radius: 18px;
      padding: 18px 16px;
      margin-bottom: 14px;
    }
    .admin-card-title {
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .admin-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      gap: 10px;
    }
    .admin-row:last-child {
      margin-bottom: 0;
    }
    .admin-label {
      font-size: 13px;
      color: var(--text-gray);
      font-weight: 600;
    }
    .admin-input-sm {
      background: #090e17;
      border: 1px solid #23344d;
      border-radius: 10px;
      padding: 8px 10px;
      color: #ffffff;
      font-size: 13px;
      width: 110px;
      outline: none;
    }
    .admin-btn {
      background: var(--accent-blue);
      color: #ffffff;
      border: none;
      border-radius: 12px;
      padding: 9px 14px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      transition: opacity 0.15s;
    }
    .admin-btn:active {
      opacity: 0.8;
    }
    .admin-btn.gold {
      background: var(--accent-gold);
      color: #0e141f;
    }
    .admin-btn.red {
      background: var(--danger-red);
      color: #ffffff;
    }
    .admin-btn.green {
      background: var(--accent-green);
      color: #ffffff;
    }

    .broadcast-banner {
      display: none;
      background: linear-gradient(90deg, #ff9f1c 0%, #f4b638 100%);
      color: #090e17;
      font-size: 12px;
      font-weight: 800;
      padding: 8px 14px;
      text-align: center;
      position: sticky;
      top: 57px;
      z-index: 99;
      box-shadow: 0 2px 10px rgba(244, 182, 56, 0.4);
      animation: pulseAlert 2.5s infinite;
    }
    @keyframes pulseAlert {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.85; }
    }
"""

text = text.replace("    /* Bottom Navigation Bar */", admin_css + "\n    /* Bottom Navigation Bar */")

# 2. Add Broadcast Banner right under tg-topbar
banner_html = """
  <!-- Admin Live Announcement Banner -->
  <div class="broadcast-banner" id="liveBroadcastBanner" onclick="showToast('Admin Announcement')">
    <span id="broadcastText">🚀 2X Mining Boost Weekend is Live! Hold MRG to earn double.</span>
  </div>
"""

text = text.replace("  <!-- Viewport -->", banner_html + "\n  <!-- Viewport -->")

# 3. Add Admin Button in Friends Tab Profile Banner
old_chips = """            <div class="badge-chips-row">
              <span class="badge-chip nft">💎 Non-NFT Holder</span>
              <span class="badge-chip verified">✓ Verified</span>
            </div>"""

new_chips = """            <div class="badge-chips-row">
              <span class="badge-chip nft">💎 Non-NFT Holder</span>
              <span class="badge-chip verified">✓ Verified</span>
              <span class="badge-chip" onclick="openAdminPanel()" style="background: rgba(244, 182, 56, 0.18); color: var(--accent-gold); border: 1px solid rgba(244, 182, 56, 0.4); cursor: pointer; font-weight: 800;">⚙️ Admin Panel</span>
            </div>"""

text = text.replace(old_chips, new_chips)

# 4. Add Top-Right 3-Dots Menu Trigger
old_dots = '<span onclick="showToast(\'MRG Miner Bot v2.4 (TON Network)\')">⋮</span>'
new_dots = '<span onclick="openAdminMenu()">⋮</span>'
text = text.replace(old_dots, new_dots)

# 5. Add Admin View HTML at the bottom before script
admin_markup = """
  <!-- ADMIN PANEL VIEW -->
  <div class="admin-viewport" id="adminViewport">
    <div class="admin-header-bar">
      <div class="admin-back-btn" onclick="closeAdminPanel()">
        <span>←</span>
        <span>Back to User App</span>
      </div>
      <div class="admin-badge-pill">🛡️ ADMIN CONSOLE</div>
    </div>

    <div class="admin-inner">
      <!-- Admin Stats Grid -->
      <div class="admin-stats-grid">
        <div class="admin-stat-card">
          <div class="title">Total Miners</div>
          <div class="val">128,450</div>
          <div class="sub">+1,240 today</div>
        </div>
        <div class="admin-stat-card">
          <div class="title">Network Hash</div>
          <div class="val">849.2 TH/s</div>
          <div class="sub">99.8% Online</div>
        </div>
        <div class="admin-stat-card">
          <div class="title">Total Reserve</div>
          <div class="val">2.84M MRG</div>
          <div class="sub">TON Liquidity Pool</div>
        </div>
        <div class="admin-stat-card">
          <div class="title">Pending Payouts</div>
          <div class="val" id="adminPendingPayouts">3 requests</div>
          <div class="sub" style="color: var(--accent-gold);">Needs review</div>
        </div>
      </div>

      <!-- Admin Tabs Navigation -->
      <div class="admin-nav-tabs">
        <div class="admin-tab-btn active" onclick="switchAdminTab('users', this)">User Controls</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('mining', this)">Mining Rates</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('tasks', this)">Tasks &amp; Quests</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('withdrawals', this)">Withdrawals</div>
        <div class="admin-tab-btn" onclick="switchAdminTab('broadcast', this)">Broadcast</div>
      </div>

      <!-- ADMIN TAB 1: USER CONTROLS -->
      <div class="admin-tab-section active" id="admin-sec-users">
        <div class="admin-card">
          <div class="admin-card-title">
            <span>👤 Active Account (@GwFoisal)</span>
            <span class="badge-chip verified" id="adminUserStatus">Verified ✓</span>
          </div>

          <div class="admin-row">
            <span class="admin-label">Wallet Balance</span>
            <div style="display: flex; gap: 6px;">
              <input type="number" class="admin-input-sm" id="adminAddBalanceInput" placeholder="Amount" value="50">
              <button class="admin-btn green" onclick="adminModifyBalance(1)">+ Add</button>
              <button class="admin-btn red" onclick="adminModifyBalance(-1)">- Cut</button>
            </div>
          </div>

          <div class="admin-row">
            <span class="admin-label">Miner Level</span>
            <div style="display: flex; gap: 6px;">
              <input type="number" class="admin-input-sm" id="adminLevelInput" placeholder="Level" value="83">
              <button class="admin-btn" onclick="adminSetLevel()">Apply</button>
            </div>
          </div>

          <div class="admin-row">
            <span class="admin-label">Account Verification</span>
            <button class="admin-btn gold" id="btnToggleVerify" onclick="adminToggleVerify()">Toggle Verified</button>
          </div>

          <div class="admin-row">
            <span class="admin-label">Streak Status</span>
            <button class="admin-btn" onclick="adminResetStreak()">Reset to Day 1</button>
            <button class="admin-btn gold" onclick="adminUnlockAllStreak()">Unlock Day 7</button>
          </div>
        </div>

        <div class="admin-card">
          <div class="admin-card-title">
            <span>👥 Registered Miners Registry</span>
          </div>
          <div style="font-size: 13px; color: var(--text-gray); margin-bottom: 8px;">
            <div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid #1a283e;">
              <span><strong>@GwFoisal</strong> (Current)</span>
              <span style="color: var(--accent-gold);">Level 83 • Active</span>
            </div>
            <div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid #1a283e;">
              <span><strong>@alex_ton</strong></span>
              <span style="color: var(--accent-green);">Level 72 • Mining</span>
            </div>
            <div style="display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid #1a283e;">
              <span><strong>@cryptokid</strong></span>
              <span style="color: var(--accent-blue);">Level 65 • Mining</span>
            </div>
            <div style="display: flex; justify-content: space-between; padding: 6px 0;">
              <span><strong>@rakib_dhaka</strong></span>
              <span style="color: var(--text-gray);">Level 40 • Idle</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ADMIN TAB 2: MINING RATES -->
      <div class="admin-tab-section" id="admin-sec-mining">
        <div class="admin-card">
          <div class="admin-card-title">
            <span>⚡ Global Hashrate &amp; Speed Multiplier</span>
            <span id="currentSpeedMultiplierTag" style="color: var(--accent-gold); font-size: 12px;">1.0x Normal</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Boost hash yield across the bot for community events or promotions.
          </p>

          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-bottom: 14px;">
            <button class="admin-btn" style="padding: 10px 4px; font-size: 12px;" onclick="adminSetMultiplier(1)">1x</button>
            <button class="admin-btn gold" style="padding: 10px 4px; font-size: 12px;" onclick="adminSetMultiplier(2)">2x Boost</button>
            <button class="admin-btn gold" style="padding: 10px 4px; font-size: 12px;" onclick="adminSetMultiplier(5)">5x Turbo</button>
            <button class="admin-btn red" style="padding: 10px 4px; font-size: 12px;" onclick="adminSetMultiplier(10)">10x Frenzy</button>
          </div>

          <div class="admin-row">
            <span class="admin-label">Simulate Mine Tap (+1.0 MRG)</span>
            <button class="admin-btn green" onclick="adminFastTap()">+1.0 Tap Reward</button>
          </div>
        </div>
      </div>

      <!-- ADMIN TAB 3: TASKS & QUESTS -->
      <div class="admin-tab-section" id="admin-sec-tasks">
        <div class="admin-card">
          <div class="admin-card-title">
            <span>➕ Create New Community Task</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px;">
            <input type="text" class="modal-input" id="newTaskTitle" placeholder="Task Title (e.g. Join Ton Community)" value="Join TON Whale Chat">
            <input type="number" class="modal-input" id="newTaskReward" placeholder="Reward MRG" value="25">
            <select class="modal-input" id="newTaskType" style="cursor: pointer;">
              <option value="tg">Telegram Task</option>
              <option value="tw">Twitter / X Task</option>
              <option value="yt">YouTube Task</option>
              <option value="boost">Boost Channel</option>
            </select>
            <button class="admin-btn green" style="padding: 12px;" onclick="adminCreateTask()">Publish Task to Users</button>
          </div>
        </div>
      </div>

      <!-- ADMIN TAB 4: WITHDRAWALS QUEUE -->
      <div class="admin-tab-section" id="admin-sec-withdrawals">
        <div class="admin-card">
          <div class="admin-card-title">
            <span>💸 Pending Withdrawal Requests</span>
          </div>
          <div id="adminWithdrawalsList">
            <!-- Dynamic withdrawals list -->
          </div>
        </div>
      </div>

      <!-- ADMIN TAB 5: BROADCAST -->
      <div class="admin-tab-section" id="admin-sec-broadcast">
        <div class="admin-card">
          <div class="admin-card-title">
            <span>📢 System Broadcast Alert</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Show an announcement banner on every user's screen in real time.
          </p>
          <input type="text" class="modal-input" id="broadcastInput" placeholder="Announcement message..." value="🚀 2X Mining Boost Weekend is Live! Hold MRG to earn double.">
          <div style="display: flex; gap: 8px;">
            <button class="admin-btn green" style="flex: 1; padding: 12px;" onclick="adminPublishBroadcast()">Show Banner</button>
            <button class="admin-btn red" style="flex: 1; padding: 12px;" onclick="adminHideBroadcast()">Hide Banner</button>
          </div>
        </div>
      </div>

    </div>
  </div>
"""

text = text.replace("  <!-- Transaction Details Modal -->", admin_markup + "\n  <!-- Transaction Details Modal -->")

# 6. Add JavaScript for Admin Panel
admin_js = """
    // ==========================================
    // ADMIN PANEL JAVASCRIPT CONTROLS
    // ==========================================
    function openAdminPanel() {
      soundTap();
      document.getElementById('adminViewport').classList.add('active');
      renderAdminWithdrawals();
    }

    function closeAdminPanel() {
      soundTap();
      document.getElementById('adminViewport').classList.remove('active');
    }

    function openAdminMenu() {
      soundTap();
      openAdminPanel();
    }

    function switchAdminTab(secId, btnEl) {
      soundTap();
      document.querySelectorAll('.admin-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.admin-tab-section').forEach(s => s.classList.remove('active'));
      btnEl.classList.add('active');
      const targetSec = document.getElementById('admin-sec-' + secId);
      if (targetSec) targetSec.classList.add('active');
    }

    // Modify User Balance
    function adminModifyBalance(direction) {
      soundSuccess();
      const input = document.getElementById('adminAddBalanceInput');
      const amt = parseFloat(input.value) || 0;
      if (amt <= 0) return;
      const change = amt * direction;
      state.walletMRG = Math.max(0, state.walletMRG + change);
      state.topMRG = Math.max(0, state.topMRG + change);
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';
      addTransaction({
        type: change > 0 ? 'deposit' : 'withdraw',
        title: change > 0 ? 'Admin Credit MRG' : 'Admin Debit MRG',
        amount: change,
        desc: `Admin manual balance adjustment (${change > 0 ? '+' : ''}${change} MRG)`,
        status: 'Completed'
      });
      showToast(`${change > 0 ? 'Added +' : 'Deducted '}${amt} MRG to Wallet!`);
      saveState();
    }

    // Set Level
    function adminSetLevel() {
      soundSuccess();
      const lvl = parseInt(document.getElementById('adminLevelInput').value) || 83;
      document.querySelectorAll('.mine-level-tag').forEach(el => el.innerText = `Level ${lvl} Miner`);
      document.querySelectorAll('.level-capsule span:last-child').forEach(el => el.innerText = `Level ${lvl}`);
      showToast(`User level updated to Level ${lvl}`);
    }

    // Toggle Verification
    function adminToggleVerify() {
      soundTap();
      const statusEl = document.getElementById('adminUserStatus');
      const isVerified = statusEl.innerText.includes('Verified');
      if (isVerified) {
        statusEl.innerText = 'Unverified ✕';
        statusEl.className = 'badge-chip nft';
        showToast('Account verification revoked');
      } else {
        statusEl.innerText = 'Verified ✓';
        statusEl.className = 'badge-chip verified';
        showToast('Account marked as Verified ✓');
      }
    }

    // Reset or Unlock Streak
    function adminResetStreak() {
      soundTap();
      state.streakDay = 1;
      document.getElementById('streakBadge').innerText = 'Day 1 of 7';
      showToast('Daily check-in streak reset to Day 1');
      saveState();
    }

    function adminUnlockAllStreak() {
      soundSuccess();
      state.streakDay = 7;
      document.getElementById('streakBadge').innerText = 'Day 7 of 7';
      document.querySelectorAll('.streak-day-card').forEach(c => {
        c.classList.remove('pending');
        c.classList.add('completed');
        c.querySelector('.streak-icon-circle').innerText = '✓';
      });
      showToast('Unlocked all 7 Days Check-in!');
      saveState();
    }

    // Multiplier
    function adminSetMultiplier(mult) {
      soundSuccess();
      state.miningRatePerSec = 0.0000085 * mult;
      document.getElementById('currentSpeedMultiplierTag').innerText = `${mult}x ${mult > 1 ? 'Boost' : 'Normal'}`;
      showToast(`Mining speed set to ${mult}x!`);
    }

    function adminFastTap() {
      soundSuccess();
      state.unclaimedMRG += 1.0;
      document.getElementById('unclaimedVal').innerText = state.unclaimedMRG.toFixed(6);
      showToast('+1.0 MRG added to Unclaimed Pool!');
    }

    // Create New Task
    function adminCreateTask() {
      soundSuccess();
      const title = document.getElementById('newTaskTitle').value.trim() || 'Special Quest';
      const reward = parseFloat(document.getElementById('newTaskReward').value) || 10;
      const type = document.getElementById('newTaskType').value;

      const tasksContainer = document.getElementById('tab-tasks');
      if (tasksContainer) {
        const div = document.createElement('div');
        div.className = 'task-item';
        div.onclick = function() { executeTask(this, title, reward); };
        div.innerHTML = `
          <div class="task-left">
            <div class="task-logo ${type}">★</div>
            <div>
              <div class="task-info-title">${title}</div>
              <div class="task-info-reward"><span class="gold">+${reward} MRG</span> · Admin Event</div>
            </div>
          </div>
          <button class="task-claim-btn">Start</button>
        `;
        tasksContainer.appendChild(div);
      }
      showToast(`✅ Created Task: "${title}" (+${reward} MRG)!`);
      closeAdminPanel();
      switchTab('tasks');
    }

    // Broadcast announcement
    function adminPublishBroadcast() {
      soundSuccess();
      const msg = document.getElementById('broadcastInput').value.trim();
      const banner = document.getElementById('liveBroadcastBanner');
      document.getElementById('broadcastText').innerText = msg;
      banner.style.display = 'block';
      showToast('Announcement banner published to users!');
    }

    function adminHideBroadcast() {
      soundTap();
      document.getElementById('liveBroadcastBanner').style.display = 'none';
      showToast('Announcement banner hidden.');
    }

    // Pending Withdrawals Queue
    const adminWithdrawals = [
      { id: 'w1', user: '@alex_ton', amt: 45.0, addr: 'UQAf...812', time: '10m ago' },
      { id: 'w2', user: '@cryptokid', amt: 120.0, addr: 'EQB8...331', time: '35m ago' },
      { id: 'w3', user: '@GwFoisal', amt: 50.0, addr: 'UQBF...eRH', time: '1h ago' }
    ];

    function renderAdminWithdrawals() {
      const container = document.getElementById('adminWithdrawalsList');
      if (!container) return;
      document.getElementById('adminPendingPayouts').innerText = `${adminWithdrawals.length} requests`;
      if (adminWithdrawals.length === 0) {
        container.innerHTML = '<div style="color: var(--text-muted); font-size: 13px; text-align: center; padding: 14px;">No pending withdrawal requests.</div>';
        return;
      }
      container.innerHTML = adminWithdrawals.map(w => `
        <div style="background: #090e17; border-radius: 12px; padding: 12px; margin-bottom: 8px; border: 1px solid #1c2b42;">
          <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
            <strong style="color: #fff; font-size: 14px;">${w.user}</strong>
            <span style="color: var(--accent-gold); font-weight: 800;">${w.amt} MRG</span>
          </div>
          <div style="font-size: 11px; color: var(--text-gray); margin-bottom: 8px;">
            Address: ${w.addr} • ${w.time}
          </div>
          <div style="display: flex; gap: 8px;">
            <button class="admin-btn green" style="flex: 1; padding: 6px;" onclick="adminApproveWithdrawal('${w.id}', ${w.amt})">Approve &amp; Pay</button>
            <button class="admin-btn red" style="flex: 1; padding: 6px;" onclick="adminRejectWithdrawal('${w.id}')">Reject</button>
          </div>
        </div>
      `).join('');
    }

    function adminApproveWithdrawal(id, amt) {
      soundSuccess();
      const idx = adminWithdrawals.findIndex(w => w.id === id);
      if (idx !== -1) {
        adminWithdrawals.splice(idx, 1);
        renderAdminWithdrawals();
        showToast(`Approved withdrawal of ${amt} MRG!`);
      }
    }

    function adminRejectWithdrawal(id) {
      soundTap();
      const idx = adminWithdrawals.findIndex(w => w.id === id);
      if (idx !== -1) {
        adminWithdrawals.splice(idx, 1);
        renderAdminWithdrawals();
        showToast('Withdrawal rejected and refunded.');
      }
    }
"""

text = text.replace("    // Real-time ticking mining rate", admin_js + "\n    // Real-time ticking mining rate")

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added Admin Panel to template.html successfully!")
