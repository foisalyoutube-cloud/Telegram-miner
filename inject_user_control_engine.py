import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace or enhance the JavaScript functions for user control.
# Let's see what exists currently between:
# "// State" and "// GLOBAL APP & TOKEN CONFIGURATION ENGINE"

user_ctrl_js = '''    // ==========================================
    // USER CONTROLS STATE & ENGINE (ADMIN <-> USER PANEL)
    // ==========================================
    const defaultUserControls = {
      userName: 'Telegram Miner',
      userHandle: '@telegram_miner',
      userBio: '💎 Pro Miner | Influencer',
      userAvatar: 'TM',
      verificationStatus: 'verified', // 'verified', 'unverified', 'vip', 'influencer'
      nftTier: 'non_nft', // 'non_nft', 'genesis', 'whale', 'og'
      accountStanding: 'active', // 'active', 'warning', 'frozen'
      minerLevel: 83,
      peakLevel: 103,
      todaysPnl: '+71.5',
      allTimeMined: '2.3K',
      baseHashrate: '3.19 TH/s',
      speedMultiplier: 1,
      tonWallet: 'UQBFoMy-deRHYz842P39910y-deRH',
      walletMRG: 0.0,
      unclaimedMRG: 0.000000,
      totalHoldings: '2.1K',
      streakDay: 2,
      streakTodayChecked: true,
      squadCount: 3,
      squadEarned: 0.00,
      adminMessage: ''
    };

    let userControls = Object.assign({}, defaultUserControls);

    try {
      const savedUserCtrl = localStorage.getItem('mrg_user_controls');
      if (savedUserCtrl) {
        userControls = Object.assign(userControls, JSON.parse(savedUserCtrl));
      }
    } catch (e) {}

    function saveUserControlsToStorage() {
      try {
        localStorage.setItem('mrg_user_controls', JSON.stringify(userControls));
      } catch (e) {}
    }

    function applyUserControls() {
      // 1. User Identity & Profile (Tab 4 & Topbar)
      const name = userControls.userName || 'Telegram Miner';
      const handle = userControls.userHandle || '@telegram_miner';
      const avatar = userControls.userAvatar || name.split(' ').map(n => n[0]).slice(0, 2).join('').toUpperCase() || 'TM';
      const bio = userControls.userBio || '💎 Pro Miner | Influencer';

      document.querySelectorAll('.user-profile-name').forEach(el => el.innerText = name);
      document.querySelectorAll('.user-profile-handle').forEach(el => el.innerText = handle);
      document.querySelectorAll('.user-avatar-small').forEach(el => el.innerText = avatar);
      const userProfilePic = document.querySelector('.user-profile-pic');
      if (userProfilePic) userProfilePic.innerText = avatar;
      const userBioEl = document.getElementById('userProfileBio');
      if (userBioEl) userBioEl.innerText = bio;

      // Sync with global appConfig
      appConfig.userName = name;
      appConfig.userHandle = handle;
      appConfig.tonWallet = userControls.tonWallet;
      appConfig.baseHashrate = userControls.baseHashrate;

      // 2. Verification Status Badge & Wallet KYC Status
      const profileTgBadge = document.getElementById('profileTgVerifiedBadge');
      const walletKycText = document.getElementById('walletKycStatusText');
      const walletKycIconBox = document.getElementById('walletKycIconBox');
      const adminUserStatus = document.getElementById('adminUserStatus');

      if (userControls.verificationStatus === 'verified') {
        if (profileTgBadge) {
          profileTgBadge.innerText = '✓ Verified Account';
          profileTgBadge.className = 'badge-chip verified';
          profileTgBadge.style.cssText = 'background: rgba(0, 201, 128, 0.2); color: #00c980; border: 1px solid rgba(0, 201, 128, 0.4);';
        }
        if (walletKycText) { walletKycText.innerText = 'Verified ✓'; walletKycText.style.color = '#00c980'; }
        if (walletKycIconBox) { walletKycIconBox.innerText = '🛡'; walletKycIconBox.className = 'wallet-icon-box green'; }
        if (adminUserStatus) { adminUserStatus.innerText = 'Verified ✓'; adminUserStatus.className = 'badge-chip verified'; }
      } else if (userControls.verificationStatus === 'unverified') {
        if (profileTgBadge) {
          profileTgBadge.innerText = '✕ Unverified';
          profileTgBadge.className = 'badge-chip nft';
          profileTgBadge.style.cssText = 'background: rgba(255, 71, 87, 0.18); color: #ff4757; border: 1px solid rgba(255, 71, 87, 0.4);';
        }
        if (walletKycText) { walletKycText.innerText = 'Unverified ⚠️ Action Required'; walletKycText.style.color = '#ff4757'; }
        if (walletKycIconBox) { walletKycIconBox.innerText = '⚠️'; walletKycIconBox.className = 'wallet-icon-box red'; }
        if (adminUserStatus) { adminUserStatus.innerText = 'Unverified ✕'; adminUserStatus.className = 'badge-chip nft'; }
      } else if (userControls.verificationStatus === 'vip') {
        if (profileTgBadge) {
          profileTgBadge.innerText = '👑 VIP Member';
          profileTgBadge.className = 'badge-chip verified';
          profileTgBadge.style.cssText = 'background: rgba(244, 182, 56, 0.2); color: #f4b638; border: 1px solid rgba(244, 182, 56, 0.4);';
        }
        if (walletKycText) { walletKycText.innerText = 'VIP Gold Member 👑'; walletKycText.style.color = '#f4b638'; }
        if (walletKycIconBox) { walletKycIconBox.innerText = '👑'; walletKycIconBox.className = 'wallet-icon-box gold'; }
        if (adminUserStatus) { adminUserStatus.innerText = 'VIP Gold 👑'; adminUserStatus.className = 'badge-chip gold'; }
      } else if (userControls.verificationStatus === 'influencer') {
        if (profileTgBadge) {
          profileTgBadge.innerText = '🌟 Influencer Verified';
          profileTgBadge.className = 'badge-chip verified';
          profileTgBadge.style.cssText = 'background: rgba(165, 94, 234, 0.2); color: #a55eea; border: 1px solid rgba(165, 94, 234, 0.4);';
        }
        if (walletKycText) { walletKycText.innerText = 'Verified Influencer 🌟'; walletKycText.style.color = '#a55eea'; }
        if (walletKycIconBox) { walletKycIconBox.innerText = '🌟'; walletKycIconBox.className = 'wallet-icon-box purple'; }
        if (adminUserStatus) { adminUserStatus.innerText = 'Influencer 🌟'; adminUserStatus.className = 'badge-chip purple'; }
      }

      // 3. NFT Tier Badge
      const profileNftBadge = document.getElementById('profileNftBadge');
      if (profileNftBadge) {
        if (userControls.nftTier === 'genesis') {
          profileNftBadge.innerText = '💎 Genesis NFT Holder (+20%)';
          profileNftBadge.style.cssText = 'background: rgba(0, 201, 128, 0.15); color: #00c980; border: 1px solid rgba(0, 201, 128, 0.4);';
        } else if (userControls.nftTier === 'whale') {
          profileNftBadge.innerText = '🐳 Crypto Whale Tier';
          profileNftBadge.style.cssText = 'background: rgba(244, 182, 56, 0.18); color: #f4b638; border: 1px solid rgba(244, 182, 56, 0.4);';
        } else if (userControls.nftTier === 'og') {
          profileNftBadge.innerText = '🎖️ OG Community Pioneer';
          profileNftBadge.style.cssText = 'background: rgba(41, 151, 255, 0.18); color: #2997ff; border: 1px solid rgba(41, 151, 255, 0.4);';
        } else {
          profileNftBadge.innerText = '💎 Non-NFT Holder';
          profileNftBadge.style.cssText = '';
        }
      }

      // 4. Account Standing Alert
      const standingAlert = document.getElementById('userStandingAlert');
      if (standingAlert) {
        if (userControls.accountStanding === 'warning') {
          standingAlert.style.display = 'block';
          standingAlert.style.background = 'rgba(244, 182, 56, 0.15)';
          standingAlert.style.border = '1px solid rgba(244, 182, 56, 0.4)';
          standingAlert.style.color = '#f4b638';
          standingAlert.innerText = '⚠️ Account Standing: Warning notice issued. Please maintain daily activity.';
        } else if (userControls.accountStanding === 'frozen') {
          standingAlert.style.display = 'block';
          standingAlert.style.background = 'rgba(255, 71, 87, 0.15)';
          standingAlert.style.border = '1px solid rgba(255, 71, 87, 0.4)';
          standingAlert.style.color = '#ff6b81';
          standingAlert.innerText = '❄️ Account Suspended / Frozen by Admin. Mining and withdrawal functions restricted.';
        } else {
          standingAlert.style.display = 'none';
        }
      }

      // 5. Admin Direct Message Card
      const msgCard = document.getElementById('adminUserMessageCard');
      const msgText = document.getElementById('adminUserMessageText');
      if (msgCard && msgText) {
        if (userControls.adminMessage && userControls.adminMessage.trim()) {
          msgText.innerText = userControls.adminMessage;
          msgCard.style.display = 'block';
        } else {
          msgCard.style.display = 'none';
        }
      }

      // 6. User Balances & Financials
      state.walletMRG = parseFloat(userControls.walletMRG) || 0.0;
      state.topMRG = state.walletMRG;
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      const topBalEl = document.getElementById('topBalance');
      if (topBalEl) {
        topBalEl.innerText = state.topMRG >= 1000 
          ? (state.topMRG / 1000).toFixed(1) + 'K' 
          : state.topMRG.toFixed(1);
      }
      const walletSubEl = document.querySelector('#tab-wallet .unclaimed-subrate');
      if (walletSubEl) {
        walletSubEl.innerText = `≈ $${(state.walletMRG * appConfig.tokenPriceUSD).toFixed(2)}`;
      }

      // Unclaimed pool
      state.unclaimedMRG = parseFloat(userControls.unclaimedMRG) || 0.000000;
      const unclEl = document.getElementById('unclaimedVal');
      if (unclEl) unclEl.innerText = state.unclaimedMRG.toFixed(6);
      const btnClaimVal = document.getElementById('btnClaimVal');
      if (btnClaimVal) btnClaimVal.innerText = state.unclaimedMRG.toFixed(2);
      const unclSubEl = document.querySelector('.unclaimed-subrate');
      if (unclSubEl) {
        unclSubEl.innerText = `≈ $${(state.unclaimedMRG * appConfig.tokenPriceUSD).toFixed(4)} · ${userControls.baseHashrate}`;
      }

      // Total Holdings
      const holdingEl = document.getElementById('walletTotalHolding');
      if (holdingEl) {
        holdingEl.innerHTML = `${userControls.totalHoldings} <span class="token-sym">${appConfig.tokenSymbol}</span>`;
      }

      // 7. Miner Level, Rig & Hashrate
      const lvl = parseInt(userControls.minerLevel) || 83;
      const peak = parseInt(userControls.peakLevel) || 103;
      const sym = appConfig.tokenSymbol || 'MRG';

      const mineLvlTag = document.getElementById('mineLevelTag');
      if (mineLvlTag) mineLvlTag.innerText = `Level ${lvl} Miner`;
      const mineStatLvl = document.getElementById('mineStatLevel');
      if (mineStatLvl) mineStatLvl.innerText = `Level ${lvl}`;
      const topbarLvl = document.getElementById('topbarLevelSpan');
      if (topbarLvl) topbarLvl.innerText = `Level ${lvl}`;

      // Tab 3 Miners Store stats
      const tabLvlVal = document.getElementById('minersTabLevelVal');
      if (tabLvlVal) tabLvlVal.innerText = lvl;
      const tabPeakVal = document.getElementById('minersTabPeakVal');
      if (tabPeakVal) tabPeakVal.innerText = peak;
      const tabPnlVal = document.getElementById('minersTabPnlVal');
      if (tabPnlVal) tabPnlVal.innerText = userControls.todaysPnl || '+71.5';
      const tabNextLvl = document.getElementById('minersTabNextLevel');
      if (tabNextLvl) tabNextLvl.innerText = `Level ${lvl + 1}`;
      const tabRemain = document.getElementById('minersTabRemain');
      if (tabRemain) tabRemain.innerHTML = `3.0 <span class="token-sym">${sym}</span> to go`;
      const allTimeMinedEl = document.getElementById('minersAllTimeMinedSub');
      if (allTimeMinedEl) allTimeMinedEl.innerHTML = `All-Time Mined: ${userControls.allTimeMined || '2.3K'} <span class="token-sym">${sym}</span>`;
      const peakSubEl = document.getElementById('minersPeakLevelSub');
      if (peakSubEl) peakSubEl.innerText = `Peak Level ${peak}`;
      const activeRigTitle = document.getElementById('minersActiveRigTitle');
      if (activeRigTitle) activeRigTitle.innerText = `Level ${lvl} Miner (${userControls.baseHashrate})`;

      // Hashrate
      const mineStatHash = document.getElementById('mineStatHashrate');
      if (mineStatHash) mineStatHash.innerText = userControls.baseHashrate;

      // Speed Multiplier
      const mult = parseInt(userControls.speedMultiplier) || 1;
      state.miningRatePerSec = 0.0000085 * mult;
      const multPill = document.getElementById('mineSpeedBoostPill');
      if (multPill) {
        if (mult > 1) {
          multPill.style.display = 'inline-block';
          multPill.innerText = `⚡ ${mult}x Speed Boost Active`;
        } else {
          multPill.style.display = 'none';
        }
      }
      const multTag = document.getElementById('currentSpeedMultiplierTag');
      if (multTag) multTag.innerText = `${mult}x ${mult > 1 ? 'Boost' : 'Normal'}`;

      // 8. Connected TON Wallet
      const tonAddr = userControls.tonWallet || 'UQBFoMy-deRHYz842P39910y-deRH';
      const shortAddr = tonAddr.length > 12 
        ? tonAddr.substring(0, 6) + '...' + tonAddr.substring(tonAddr.length - 6)
        : tonAddr;
      const tonAddressEl = document.getElementById('tonAddress');
      if (tonAddressEl) tonAddressEl.innerText = shortAddr;
      const withdrawAddrInp = document.getElementById('withdrawAddress');
      if (withdrawAddrInp && (!withdrawAddrInp.value || withdrawAddrInp.value.startsWith('UQBFoMy-deRHYz842P39910'))) {
        withdrawAddrInp.value = tonAddr;
      }
      const syncBannerSub = document.getElementById('tgSyncBannerSub');
      if (syncBannerSub) syncBannerSub.innerText = `Synced: ${handle} • TON: ${shortAddr}`;

      // 9. Daily Streak
      renderStreakUI();

      // 10. Squad & Referral Mining
      const squadEarnedEl = document.getElementById('squadEarnedMRG');
      if (squadEarnedEl) squadEarnedEl.innerText = (parseFloat(userControls.squadEarned) || 0).toFixed(2);
      const squadUsdEl = document.getElementById('squadEarnedUSD');
      if (squadUsdEl) {
        squadUsdEl.innerHTML = `≈ $${((parseFloat(userControls.squadEarned) || 0) * appConfig.tokenPriceUSD).toFixed(3)} earned from squad (<span id="squadFriendsCountText">${userControls.squadCount || 3} friends</span>)`;
      }

      // 11. Admin Panel UI Sync
      const admActiveHandle = document.getElementById('adminUserActiveHandle');
      if (admActiveHandle) admActiveHandle.innerText = handle;
      const admSummaryLvl = document.getElementById('adminSummaryLevel');
      if (admSummaryLvl) admSummaryLvl.innerText = lvl;
      const admRegCurrent = document.getElementById('adminRegistryCurrentUser');
      if (admRegCurrent) admRegCurrent.innerText = handle;
      const admRegCurrentStatus = document.getElementById('adminRegistryCurrentUserStatus');
      if (admRegCurrentStatus) admRegCurrentStatus.innerText = `Level ${lvl} • Active`;

      saveUserControlsToStorage();
    }

    function renderStreakUI() {
      const sDay = parseInt(userControls.streakDay) || 1;
      const checked = !!userControls.streakTodayChecked;
      state.streakDay = sDay;

      const badge = document.getElementById('streakBadge');
      if (badge) badge.innerText = `Day ${sDay} of 7`;

      const grid = document.querySelector('.streak-grid');
      if (grid) {
        const rewards = [5, 6, 7, 8, 9, 10, 15];
        grid.innerHTML = rewards.map((r, idx) => {
          const dNum = idx + 1;
          const isStar = dNum === 7;
          const dLabel = isStar ? '★' : `D${dNum}`;

          if (dNum < sDay) {
            return `
              <div class="streak-day-card completed">
                <span class="streak-day-label">${dLabel}</span>
                <div class="streak-icon-circle">✓</div>
                <span class="streak-reward-text">+${r}</span>
              </div>
            `;
          } else if (dNum === sDay) {
            if (checked) {
              return `
                <div class="streak-day-card completed">
                  <span class="streak-day-label">${dLabel}</span>
                  <div class="streak-icon-circle">✓</div>
                  <span class="streak-reward-text">+${r}</span>
                </div>
              `;
            } else {
              return `
                <div class="streak-day-card today pending" onclick="claimStreakDay(${dNum})">
                  <span class="streak-day-label">${dLabel}</span>
                  <div class="streak-icon-circle">${isStar ? '⭐' : '🪙'}</div>
                  <span class="streak-reward-text">+${r}</span>
                </div>
              `;
            }
          } else {
            return `
              <div class="streak-day-card pending">
                <span class="streak-day-label">${dLabel}</span>
                <div class="streak-icon-circle">${isStar ? '⭐' : '🪙'}</div>
                <span class="streak-reward-text">+${r}</span>
              </div>
            `;
          }
        }).join('');
      }

      const btn = document.getElementById('btnDailyCheckin');
      if (btn) {
        if (checked) {
          btn.innerText = 'Checked in today ✓';
          btn.style.opacity = '0.7';
          btn.onclick = function() { showToast('Already checked in for today!'); };
        } else {
          btn.innerText = `Check in today (+${sDay + 4} ${appConfig.tokenSymbol})`;
          btn.style.opacity = '1';
          btn.onclick = function() { claimStreakDay(sDay); };
        }
      }

      const note = document.querySelector('.streak-footer-note');
      if (note) note.innerText = `Day ${sDay} of 7. Miss a day and streak restarts.`;
    }

    function populateUserControlInputs() {
      const setVal = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.value = (val !== undefined && val !== null) ? val : '';
      };
      setVal('userCtrlName', userControls.userName);
      setVal('userCtrlHandle', userControls.userHandle);
      setVal('userCtrlBio', userControls.userBio);
      setVal('userCtrlAvatar', userControls.userAvatar);
      setVal('userCtrlVerification', userControls.verificationStatus);
      setVal('userCtrlNftTier', userControls.nftTier);
      setVal('userCtrlStanding', userControls.accountStanding);
      setVal('userCtrlWalletBalance', userControls.walletMRG);
      setVal('userCtrlUnclaimed', userControls.unclaimedMRG);
      setVal('userCtrlTotalHolding', userControls.totalHoldings);
      setVal('userCtrlMinerLevel', userControls.minerLevel);
      setVal('userCtrlPeakLevel', userControls.peakLevel);
      setVal('userCtrlTodaysPnl', userControls.todaysPnl);
      setVal('userCtrlAllTimeMined', userControls.allTimeMined);
      setVal('userCtrlHashrate', userControls.baseHashrate);
      setVal('userCtrlTonWallet', userControls.tonWallet);
      setVal('userCtrlSquadCount', userControls.squadCount);
      setVal('userCtrlSquadEarned', userControls.squadEarned);
      setVal('adminUserMessageInput', userControls.adminMessage);
    }

    function liveUpdateUserField(field, val) {
      userControls[field] = val;
      applyUserControls();
    }

    function saveAllUserControls() {
      soundSuccess();
      const getVal = (id) => {
        const el = document.getElementById(id);
        return el ? el.value : '';
      };

      userControls.userName = getVal('userCtrlName').trim() || 'Telegram Miner';
      let handle = getVal('userCtrlHandle').trim() || '@telegram_miner';
      if (!handle.startsWith('@')) handle = '@' + handle;
      userControls.userHandle = handle;
      userControls.userBio = getVal('userCtrlBio').trim() || '💎 Pro Miner | Influencer';
      userControls.userAvatar = getVal('userCtrlAvatar').trim() || 'TM';
      userControls.verificationStatus = getVal('userCtrlVerification') || 'verified';
      userControls.nftTier = getVal('userCtrlNftTier') || 'non_nft';
      userControls.accountStanding = getVal('userCtrlStanding') || 'active';
      userControls.walletMRG = parseFloat(getVal('userCtrlWalletBalance')) || 0.0;
      userControls.unclaimedMRG = parseFloat(getVal('userCtrlUnclaimed')) || 0.000000;
      userControls.totalHoldings = getVal('userCtrlTotalHolding').trim() || '2.1K';
      userControls.minerLevel = parseInt(getVal('userCtrlMinerLevel')) || 83;
      userControls.peakLevel = parseInt(getVal('userCtrlPeakLevel')) || 103;
      userControls.todaysPnl = getVal('userCtrlTodaysPnl').trim() || '+71.5';
      userControls.allTimeMined = getVal('userCtrlAllTimeMined').trim() || '2.3K';
      userControls.baseHashrate = getVal('userCtrlHashrate').trim() || '3.19 TH/s';
      userControls.tonWallet = getVal('userCtrlTonWallet').trim() || 'UQBFoMy-deRHYz842P39910y-deRH';
      userControls.squadCount = parseInt(getVal('userCtrlSquadCount')) || 3;
      userControls.squadEarned = parseFloat(getVal('userCtrlSquadEarned')) || 0.00;
      userControls.adminMessage = getVal('adminUserMessageInput').trim();

      // Keep appConfig in sync as well
      appConfig.userName = userControls.userName;
      appConfig.userHandle = userControls.userHandle;
      appConfig.tonWallet = userControls.tonWallet;
      appConfig.baseHashrate = userControls.baseHashrate;
      try {
        localStorage.setItem('mrg_app_config', JSON.stringify(appConfig));
      } catch (e) {}

      applyUserControls();
      applyGlobalConfig();
      saveState();

      showToast('💾 All User Controls saved & applied to User Panel!');
    }

    function resetUserControlsDefault() {
      soundTap();
      userControls = Object.assign({}, defaultUserControls);
      populateUserControlInputs();
      applyUserControls();
      showToast('🔄 User controls reset to defaults.');
    }

    function adminSetExactWalletBalance() {
      soundSuccess();
      const inp = document.getElementById('userCtrlWalletBalance');
      const val = parseFloat(inp ? inp.value : 0) || 0.0;
      const prev = userControls.walletMRG;
      userControls.walletMRG = val;
      const diff = val - prev;
      addTransaction({
        type: diff >= 0 ? 'deposit' : 'withdraw',
        title: 'Admin Balance Set',
        amount: Math.abs(diff),
        desc: `Admin updated wallet balance to ${val.toFixed(1)} ${appConfig.tokenSymbol}`,
        status: 'Completed'
      });
      applyUserControls();
      saveState();
      showToast(`✅ Wallet balance set to: ${val.toFixed(1)} ${appConfig.tokenSymbol}`);
    }

    function adminQuickAddBalance(amt) {
      soundSuccess();
      userControls.walletMRG = Math.max(0, (userControls.walletMRG || 0) + amt);
      const inp = document.getElementById('userCtrlWalletBalance');
      if (inp) inp.value = userControls.walletMRG.toFixed(1);
      addTransaction({
        type: amt > 0 ? 'deposit' : 'withdraw',
        title: amt > 0 ? 'Admin Balance Credit' : 'Admin Balance Debit',
        amount: Math.abs(amt),
        desc: `Admin manual balance adjustment (${amt > 0 ? '+' : ''}${amt} ${appConfig.tokenSymbol})`,
        status: 'Completed'
      });
      applyUserControls();
      saveState();
      showToast(`${amt > 0 ? 'Added +' : 'Deducted '}${Math.abs(amt)} ${appConfig.tokenSymbol} to Wallet!`);
    }

    function adminSetExactUnclaimed() {
      soundSuccess();
      const inp = document.getElementById('userCtrlUnclaimed');
      const val = parseFloat(inp ? inp.value : 0) || 0.000000;
      userControls.unclaimedMRG = val;
      applyUserControls();
      saveState();
      showToast(`✅ Unclaimed Mining Pool set to: ${val.toFixed(6)} ${appConfig.tokenSymbol}`);
    }

    function adminQuickAddUnclaimed(amt) {
      soundSuccess();
      userControls.unclaimedMRG = (userControls.unclaimedMRG || 0) + amt;
      const inp = document.getElementById('userCtrlUnclaimed');
      if (inp) inp.value = userControls.unclaimedMRG.toFixed(6);
      applyUserControls();
      saveState();
      showToast(`+${amt} added to Unclaimed Mining Pool!`);
    }

    function adminResetUnclaimedZero() {
      soundTap();
      userControls.unclaimedMRG = 0.000000;
      const inp = document.getElementById('userCtrlUnclaimed');
      if (inp) inp.value = '0.000000';
      applyUserControls();
      saveState();
      showToast('Unclaimed pool reset to 0.000000');
    }

    function adminSetUserMultiplier(mult) {
      soundSuccess();
      userControls.speedMultiplier = mult;
      applyUserControls();
      showToast(`Mining speed set to ${mult}x Boost!`);
    }

    function adminGenerateRandomWallet() {
      soundTap();
      const randomId = Math.random().toString(36).substring(2, 10);
      const newWallet = generateDeterministicTonWallet(randomId);
      userControls.tonWallet = newWallet;
      const inp = document.getElementById('userCtrlTonWallet');
      if (inp) inp.value = newWallet;
      applyUserControls();
      showToast('🎲 Generated and linked new TON wallet address!');
    }

    function adminToggleWalletDisconnect() {
      soundTap();
      if (userControls.tonWallet && userControls.tonWallet !== 'Not connected') {
        userControls.tonWallet = 'Not connected';
        showToast('Wallet marked as Disconnected');
      } else {
        userControls.tonWallet = generateDeterministicTonWallet(userControls.userHandle);
        showToast('Wallet reconnected to TON');
      }
      const inp = document.getElementById('userCtrlTonWallet');
      if (inp) inp.value = userControls.tonWallet;
      applyUserControls();
    }

    function adminSetStreakDay(d) {
      soundSuccess();
      userControls.streakDay = d;
      userControls.streakTodayChecked = false;
      applyUserControls();
      showToast(`Daily streak set to Day ${d}`);
    }

    function adminToggleTodayCheckin() {
      soundSuccess();
      userControls.streakTodayChecked = !userControls.streakTodayChecked;
      applyUserControls();
      showToast(userControls.streakTodayChecked ? '✓ Today marked as Checked-In' : 'Today marked as Pending Claim');
    }

    function adminResetStreak() {
      soundTap();
      userControls.streakDay = 1;
      userControls.streakTodayChecked = false;
      applyUserControls();
      showToast('Daily check-in streak reset to Day 1');
    }

    function adminUnlockAllStreak() {
      soundSuccess();
      userControls.streakDay = 7;
      userControls.streakTodayChecked = true;
      applyUserControls();
      showToast('⭐ Unlocked all 7 Days Check-in!');
    }

    function adminAddSquadFriend(n) {
      soundSuccess();
      userControls.squadCount = (userControls.squadCount || 0) + n;
      const inp = document.getElementById('userCtrlSquadCount');
      if (inp) inp.value = userControls.squadCount;
      applyUserControls();
      showToast(`+${n} Friend added to Squad Mining!`);
    }

    function adminAddSquadReward(amt) {
      soundSuccess();
      userControls.squadEarned = (userControls.squadEarned || 0) + amt;
      userControls.walletMRG = (userControls.walletMRG || 0) + amt;
      const inp = document.getElementById('userCtrlSquadEarned');
      if (inp) inp.value = userControls.squadEarned.toFixed(2);
      const wInp = document.getElementById('userCtrlWalletBalance');
      if (wInp) wInp.value = userControls.walletMRG.toFixed(1);

      addTransaction({
        type: 'deposit',
        title: 'Squad Commission Reward',
        amount: amt,
        desc: `Team mining bonus (+${amt} ${appConfig.tokenSymbol})`,
        status: 'Completed'
      });

      applyUserControls();
      saveState();
      showToast(`+${amt} ${appConfig.tokenSymbol} Squad reward credited to user!`);
    }

    function adminSendDirectGift() {
      soundSuccess();
      const amtInp = document.getElementById('adminGiftAmount');
      const rsnInp = document.getElementById('adminGiftReason');
      const amt = parseFloat(amtInp ? amtInp.value : 0) || 100;
      const reason = (rsnInp ? rsnInp.value.trim() : '') || 'Admin Loyalty Gift';

      userControls.walletMRG = (userControls.walletMRG || 0) + amt;
      userControls.adminMessage = `🎁 Congratulations! Admin sent you a gift of +${amt} ${appConfig.tokenSymbol} (${reason})!`;

      addTransaction({
        type: 'deposit',
        title: `🎁 ${reason}`,
        amount: amt,
        desc: `Direct admin gift (+${amt} ${appConfig.tokenSymbol}) credited to your in-app wallet`,
        status: 'Completed'
      });

      populateUserControlInputs();
      applyUserControls();
      saveState();
      showToast(`🎁 Gift of +${amt} ${appConfig.tokenSymbol} sent directly to user wallet!`);
    }

    function adminPushUserMessage() {
      soundSuccess();
      const inp = document.getElementById('adminUserMessageInput');
      const msg = inp ? inp.value.trim() : '';
      if (!msg) {
        showToast('Please enter a message to push.');
        return;
      }
      userControls.adminMessage = msg;
      applyUserControls();
      showToast('📢 Notification banner published to User Panel!');
    }

    function adminClearUserMessage() {
      soundTap();
      userControls.adminMessage = '';
      const inp = document.getElementById('adminUserMessageInput');
      if (inp) inp.value = '';
      applyUserControls();
      showToast('Admin notification cleared from User Panel.');
    }

    function dismissUserMessage() {
      soundTap();
      userControls.adminMessage = '';
      const card = document.getElementById('adminUserMessageCard');
      if (card) card.style.display = 'none';
      saveUserControlsToStorage();
    }

    // Registry Switcher
    const mockMinersRegistry = {
      '@telegram_miner': {
        name: 'Telegram Miner',
        level: 83,
        peak: 103,
        hashrate: '3.19 TH/s',
        wallet: 'UQBFoMy-deRHYz842P39910y-deRH',
        balance: 0.0,
        verification: 'verified',
        tier: 'non_nft'
      },
      '@alex_ton': {
        name: 'Alex Miner (TON Pro)',
        level: 72,
        peak: 90,
        hashrate: '8.40 TH/s',
        wallet: 'UQAf829-deRHXy9148011c-alex',
        balance: 45.0,
        verification: 'verified',
        tier: 'genesis'
      },
      '@cryptokid': {
        name: 'Crypto Pro 100K',
        level: 65,
        peak: 80,
        hashrate: '5.20 TH/s',
        wallet: 'EQB8331-cryptokid0018-ton',
        balance: 120.0,
        verification: 'vip',
        tier: 'whale'
      },
      '@rakib_dhaka': {
        name: 'Rakib TON BD',
        level: 40,
        peak: 55,
        hashrate: '2.10 TH/s',
        wallet: 'UQC9412-rakibdhaka007-bd',
        balance: 12.0,
        verification: 'unverified',
        tier: 'non_nft'
      }
    };

    function loadUserToAdmin(handle) {
      soundTap();
      const data = mockMinersRegistry[handle];
      if (data) {
        userControls.userName = data.name;
        userControls.userHandle = handle;
        userControls.minerLevel = data.level;
        userControls.peakLevel = data.peak;
        userControls.baseHashrate = data.hashrate;
        userControls.tonWallet = data.wallet;
        userControls.walletMRG = data.balance;
        userControls.verificationStatus = data.verification;
        userControls.nftTier = data.tier;
        userControls.userAvatar = data.name.split(' ').map(n => n[0]).slice(0, 2).join('').toUpperCase();

        populateUserControlInputs();
        applyUserControls();
        applyGlobalConfig();
        saveState();

        showToast(`👤 Loaded user account: ${handle}`);
      }
    }
'''

# Insert the user controls engine before `// GLOBAL APP & TOKEN CONFIGURATION ENGINE`
if '// ==========================================\n    // GLOBAL APP & TOKEN CONFIGURATION ENGINE' in html:
    html = html.replace(
        '// ==========================================\n    // GLOBAL APP & TOKEN CONFIGURATION ENGINE',
        user_ctrl_js + '\n\n    // ==========================================\n    // GLOBAL APP & TOKEN CONFIGURATION ENGINE'
    )
else:
    html = html.replace(
        '// Global Config',
        user_ctrl_js + '\n\n    // Global Config'
    )

# Now, in `applyGlobalConfig()`, ensure it calls `applyUserControls()` and populates inputs
# Also update autoSyncTelegramData to sync with userControls
html = html.replace(
    'applyGlobalConfig();\n        updateTelegramStatusUI(true, handle, displayName, tonAddr);',
    '''userControls.userName = displayName;
        userControls.userHandle = handle;
        userControls.tonWallet = tonAddr;
        userControls.userAvatar = displayName.split(' ').map(n => n[0]).slice(0, 2).join('').toUpperCase();
        applyUserControls();
        applyGlobalConfig();
        populateUserControlInputs();
        updateTelegramStatusUI(true, handle, displayName, tonAddr);'''
)

# In openAdminPanel, call populateUserControlInputs()
html = html.replace(
    'document.getElementById(\'adminViewport\').classList.add(\'active\');\n      renderAdminWithdrawals();',
    '''document.getElementById('adminViewport').classList.add('active');
      populateUserControlInputs();
      renderAdminWithdrawals();'''
)

# In DOMContentLoaded, call applyUserControls() and populateUserControlInputs()
html = html.replace(
    'applyGlobalConfig();\n      if (state.lang === \'bn\') {',
    '''applyUserControls();
      applyGlobalConfig();
      populateUserControlInputs();
      if (state.lang === 'bn') {'''
)

# In clean app data, also reset userControls
html = html.replace(
    '// 5. Reset appConfig to clean baseline',
    '''// 4b. Reset userControls to clean baseline
      userControls = Object.assign({}, defaultUserControls, {
        userName: 'Telegram Miner',
        userHandle: '@telegram_miner',
        tonWallet: 'UQBFoMy-deRHYz842P39910y-deRH',
        walletMRG: 0.0,
        unclaimedMRG: 0.000000,
        streakDay: 1,
        streakTodayChecked: false
      });
      saveUserControlsToStorage();

      // 5. Reset appConfig to clean baseline'''
)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected user control engine into template.html successfully!")
