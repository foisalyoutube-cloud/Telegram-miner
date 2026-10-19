#!/usr/bin/env python3
import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update defaultUserControls to clean values
old_default_user_ctrl = '''    const defaultUserControls = {
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
    };'''

new_default_user_ctrl = '''    const defaultUserControls = {
      userName: 'Telegram Miner',
      userHandle: '@telegram_miner',
      userBio: '💎 Pro Miner | Influencer',
      userAvatar: 'TM',
      verificationStatus: 'verified', // 'verified', 'unverified', 'vip', 'influencer'
      nftTier: 'non_nft', // 'non_nft', 'genesis', 'whale', 'og'
      accountStanding: 'active', // 'active', 'warning', 'frozen'
      minerLevel: 1,
      peakLevel: 1,
      todaysPnl: '+0.00',
      allTimeMined: '0.00',
      baseHashrate: '1.00 MH/s',
      speedMultiplier: 1,
      tonWallet: 'UQBFoMy-deRHYz842P39910y-deRH',
      walletMRG: 0.0,
      unclaimedMRG: 0.000000,
      totalHoldings: '0.00',
      streakDay: 1,
      streakTodayChecked: false,
      squadCount: 0,
      squadEarned: 0.00,
      adminMessage: ''
    };'''

if old_default_user_ctrl in html:
    html = html.replace(old_default_user_ctrl, new_default_user_ctrl)
    print("✓ Updated defaultUserControls with clean values")
else:
    # Use regex replacement
    pattern = r'const defaultUserControls = \{[\s\S]*?adminMessage: \'\'\s*\};'
    html = re.sub(pattern, new_default_user_ctrl.strip(), html, count=1)
    print("✓ Updated defaultUserControls via regex")

# 2. Update defaultConfig baseHashrate
html = html.replace("baseHashrate: '3.19 TH/s',", "baseHashrate: '1.00 MH/s',")

# 3. Add Token Logo Presets and Token Logo Management Engine in JS
token_logo_and_anim_engine = '''
    // ==========================================
    // TOKEN LOGO ENGINE (UNIVERSAL REAL-TIME SYNC)
    // ==========================================
    const DEFAULT_COIN_B64 = "data:image/jpeg;base64,__COIN_B64__";
    let currentSelectedTokenLogo = DEFAULT_COIN_B64;

    // SVG Presets (self-contained, ultra-sharp vector graphics)
    const TOKEN_PRESETS = {
      gold: 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><radialGradient id="goldGrad" cx="35%" cy="35%" r="65%"><stop offset="0%" stop-color="%23FFF6A6"/><stop offset="45%" stop-color="%23F5A623"/><stop offset="100%" stop-color="%23B36B00"/></radialGradient><linearGradient id="rimGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="%23FFE680"/><stop offset="100%" stop-color="%23663C00"/></linearGradient></defs><circle cx="50" cy="50" r="48" fill="url(%23rimGrad)" stroke="%23331C00" stroke-width="2"/><circle cx="50" cy="50" r="42" fill="url(%23goldGrad)"/><circle cx="50" cy="50" r="37" fill="none" stroke="%23FFE885" stroke-dasharray="3,3" stroke-width="1.5"/><text x="50" y="58" font-size="28" font-weight="900" font-family="Arial,sans-serif" fill="%23FFFFFF" text-anchor="middle" filter="drop-shadow(0 2px 3px rgba(0,0,0,0.5))">MRG</text></svg>',
      ton: 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><linearGradient id="tonGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="%232EB5FF"/><stop offset="100%" stop-color="%230072C6"/></linearGradient></defs><circle cx="50" cy="50" r="48" fill="%2300182E" stroke="%230098EA" stroke-width="3"/><polygon points="50,15 85,38 72,85 28,85 15,38" fill="url(%23tonGrad)"/><polygon points="50,15 50,85 72,85 85,38" fill="%230086D6"/><polygon points="50,22 75,40 50,75 25,40" fill="%23FFFFFF" opacity="0.3"/><polygon points="50,22 50,75 75,40" fill="%23FFFFFF" opacity="0.45"/><text x="50" y="58" font-size="26" font-weight="bold" font-family="Arial,sans-serif" fill="%23FFFFFF" text-anchor="middle">💎</text></svg>',
      btc: 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="%23F7931A" stroke="%23B36200" stroke-width="3"/><circle cx="50" cy="50" r="42" fill="none" stroke="%23FFD085" stroke-width="2"/><text x="50" y="66" font-size="48" font-weight="bold" font-family="Arial,sans-serif" fill="%23FFFFFF" text-anchor="middle">₿</text></svg>',
      eth: 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="%231E2433" stroke="%23627EEA" stroke-width="3"/><polygon points="50,16 50,54 75,43" fill="%238A92B2"/><polygon points="50,16 25,43 50,54" fill="%23627EEA"/><polygon points="50,58 50,84 75,49" fill="%238A92B2"/><polygon points="50,58 25,49 50,84" fill="%23627EEA"/><polygon points="50,54 75,43 50,47" fill="%23454A75"/><polygon points="50,54 50,47 25,43" fill="%23384260"/></svg>',
      fire: 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><radialGradient id="fireGrad" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="%23FF3838"/><stop offset="100%" stop-color="%234A0000"/></radialGradient></defs><circle cx="50" cy="50" r="48" fill="url(%23fireGrad)" stroke="%23FF8000" stroke-width="3"/><text x="50" y="68" font-size="52" text-anchor="middle">🔥</text></svg>',
      star: 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="%23221E0A" stroke="%23F4B638" stroke-width="3"/><text x="50" y="66" font-size="50" text-anchor="middle">⭐</text></svg>',
      rocket: 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="%2310182E" stroke="%237A5CFF" stroke-width="3"/><text x="50" y="68" font-size="50" text-anchor="middle">🚀</text></svg>',
      original: DEFAULT_COIN_B64
    };

    function emojiToDataUrl(emoji) {
      return `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="%23162235" stroke="%23F4B638" stroke-width="3"/><text x="50" y="68" font-size="50" text-anchor="middle">${encodeURIComponent(emoji)}</text></svg>`;
    }

    function applyTokenLogo(logoSrc) {
      if (!logoSrc) return;
      currentSelectedTokenLogo = logoSrc;
      appConfig.tokenLogo = logoSrc;
      try {
        localStorage.setItem('mrg_app_config', JSON.stringify(appConfig));
      } catch (e) {}

      // Update ALL token logo images across the applet
      document.querySelectorAll('.token-logo-img, .coin-icon, #mascotCoin, #adminTokenLogoPreview').forEach(img => {
        if (img.tagName === 'IMG') {
          img.src = logoSrc;
          img.classList.remove('token-logo-swapped');
          void img.offsetWidth; // trigger reflow
          img.classList.add('token-logo-swapped');
        }
      });

      const preview = document.getElementById('adminTokenLogoPreview');
      if (preview) preview.src = logoSrc;

      const status = document.getElementById('adminTokenLogoStatus');
      if (status) status.innerText = 'Logo Updated & Synced ✓';
    }

    function adminSelectPresetLogo(presetName) {
      soundTap();
      const logo = TOKEN_PRESETS[presetName] || DEFAULT_COIN_B64;
      currentSelectedTokenLogo = logo;
      const preview = document.getElementById('adminTokenLogoPreview');
      if (preview) {
        preview.src = logo;
        preview.classList.add('token-logo-swapped');
        setTimeout(() => preview.classList.remove('token-logo-swapped'), 600);
      }
      const status = document.getElementById('adminTokenLogoStatus');
      if (status) status.innerText = `Selected Preset: ${presetName.toUpperCase()} (Click Save to apply)`;
      showToast(`Selected "${presetName.toUpperCase()}" preset logo!`);
    }

    function handleAdminTokenLogoUpload(event) {
      const file = event.target.files && event.target.files[0];
      if (!file) return;
      soundTap();
      const reader = new FileReader();
      reader.onload = function(e) {
        const base64 = e.target.result;
        currentSelectedTokenLogo = base64;
        const preview = document.getElementById('adminTokenLogoPreview');
        if (preview) preview.src = base64;
        const status = document.getElementById('adminTokenLogoStatus');
        if (status) status.innerText = `Custom Image Loaded: ${file.name}`;
        showToast('📁 Custom logo loaded! Click "Save & Change All Token Logos".');
      };
      reader.readAsDataURL(file);
    }

    function applyCustomTokenLogoUrl() {
      soundTap();
      const input = document.getElementById('cfgTokenLogoUrl');
      if (!input) return;
      let val = input.value.trim();
      if (!val) {
        showToast('Please enter an Image URL or Emoji!');
        return;
      }

      let logoUrl = val;
      // If it looks like an emoji (short text without http)
      if (!val.startsWith('http') && !val.startsWith('data:')) {
        logoUrl = emojiToDataUrl(val);
      }

      currentSelectedTokenLogo = logoUrl;
      const preview = document.getElementById('adminTokenLogoPreview');
      if (preview) preview.src = logoUrl;
      const status = document.getElementById('adminTokenLogoStatus');
      if (status) status.innerText = 'Custom URL/Emoji Applied';
      adminApplyAllTokenLogos(logoUrl);
    }

    function adminApplyAllTokenLogos(logo) {
      soundSuccess();
      const targetLogo = logo || currentSelectedTokenLogo || DEFAULT_COIN_B64;
      applyTokenLogo(targetLogo);
      showToast('✨ All token logos updated successfully across the app!');
      if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
        window.Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      }
    }

    // ==========================================
    // BALANCE FORMATTING & HOME SCREEN SYNC
    // ==========================================
    function formatBalanceDisplay(num) {
      num = parseFloat(num) || 0;
      if (num >= 1000000) return (num / 1000000).toFixed(2) + 'M';
      if (num >= 1000) return (num / 1000).toFixed(2) + 'K';
      if (num >= 100) return num.toFixed(1);
      if (num >= 1) return num.toFixed(2);
      if (num > 0) return num.toFixed(3);
      return '0.00';
    }

    function updateAllBalanceDisplays(bal, delta) {
      bal = parseFloat(bal) || 0;
      const formatted = formatBalanceDisplay(bal);
      const precise = bal >= 10 ? bal.toFixed(2) : bal.toFixed(3);
      const sym = appConfig.tokenSymbol || 'MRG';
      const usdVal = (bal * (appConfig.tokenPriceUSD || 0.00128)).toFixed(2);

      // Top Telegram Bar balance capsule
      const topBal = document.getElementById('topBalance');
      if (topBal) {
        topBal.innerText = formatted;
        topBal.classList.add('balance-bounce');
        setTimeout(() => topBal.classList.remove('balance-bounce'), 700);
      }
      const topCapsule = document.querySelector('.balance-capsule');
      if (topCapsule) {
        topCapsule.classList.add('balance-glow-pulse');
        setTimeout(() => topCapsule.classList.remove('balance-glow-pulse'), 750);
      }

      // Home Screen (Tab 1) Balance Card
      const homeBal = document.getElementById('homeWalletBalance');
      if (homeBal) {
        homeBal.innerText = precise;
        homeBal.classList.add('balance-bounce');
        setTimeout(() => homeBal.classList.remove('balance-bounce'), 700);
      }
      const homeSub = document.getElementById('homeWalletSub');
      if (homeSub) {
        homeSub.innerText = `≈ $${usdVal} USD · Available Balance`;
      }

      // Tab 5 Wallet Balance
      const walletBal = document.getElementById('walletMRGBalance');
      if (walletBal) walletBal.innerText = precise;
      const walletTotal = document.getElementById('walletTotalHolding');
      if (walletTotal) walletTotal.innerHTML = `${formatted} <span class="token-sym">${sym}</span>`;

      // Reset Mine card unclaimed & claim button
      const unclVal = document.getElementById('unclaimedVal');
      if (unclVal) unclVal.innerText = '0.000000';
      const btnClaimVal = document.getElementById('btnClaimVal');
      if (btnClaimVal) btnClaimVal.innerText = '0.00';
    }

    // Flying Coin Claim Animation
    function triggerClaimAnimation(amount) {
      const claimBtn = document.getElementById('btnClaim');
      const target = document.querySelector('.balance-capsule') || document.getElementById('topBalance');
      if (!claimBtn || !target) return;

      const btnRect = claimBtn.getBoundingClientRect();
      const targetRect = target.getBoundingClientRect();
      const homeBalCard = document.getElementById('homeBalanceCard');
      const homeRect = homeBalCard ? homeBalCard.getBoundingClientRect() : null;

      const particleCount = 8;
      const logoSrc = appConfig.tokenLogo || DEFAULT_COIN_B64;

      for (let i = 0; i < particleCount; i++) {
        const coin = document.createElement('div');
        coin.className = 'flying-coin-particle';
        
        if (logoSrc && !logoSrc.includes('<svg') && (logoSrc.startsWith('data:') || logoSrc.startsWith('http'))) {
          coin.innerHTML = `<img src="${logoSrc}" style="width: 24px; height: 24px; border-radius: 50%; object-fit: cover;">`;
        } else {
          coin.innerText = '🪙';
        }

        const startX = btnRect.left + btnRect.width / 2 + (Math.random() * 50 - 25);
        const startY = btnRect.top + btnRect.height / 2 + (Math.random() * 20 - 10);
        
        // Alternate destinations between top bar and home card
        const destRect = (i % 2 === 0 || !homeRect) ? targetRect : homeRect;
        const endX = destRect.left + destRect.width / 2 + (Math.random() * 20 - 10);
        const endY = destRect.top + destRect.height / 2 + (Math.random() * 10 - 5);

        coin.style.left = `${startX}px`;
        coin.style.top = `${startY}px`;
        document.body.appendChild(coin);

        const delay = i * 45;
        setTimeout(() => {
          coin.style.transform = `translate(${endX - startX}px, ${endY - startY}px) scale(0.65)`;
          coin.style.opacity = '0';
        }, delay + 10);

        setTimeout(() => {
          coin.remove();
        }, delay + 700);
      }
    }
'''

# Insert token_logo_and_anim_engine right before `function claimMiningReward`
pattern = r'// Claim Mining Reward\s*function claimMiningReward\(\)\s*\{'

new_claim_mining_reward = '''// Claim Mining Reward (ANIMATED & HOME SCREEN REAL-TIME SYNC)
    function claimMiningReward() {
      // If unclaimed is very low or 0, give helpful feedback or small starter mining boost
      if (state.unclaimedMRG <= 0.0000001) {
        showToast('⛏️ Miner active! Tap mascot coin or wait to accumulate rewards.');
        const mascot = document.getElementById('mascotCoin');
        if (mascot) {
          mascot.classList.add('mascot-tap-anim');
          setTimeout(() => mascot.classList.remove('mascot-tap-anim'), 400);
        }
        return;
      }

      soundClaim();
      const claimed = state.unclaimedMRG;
      state.walletMRG = (parseFloat(state.walletMRG) || 0) + claimed;
      state.topMRG = state.walletMRG;
      state.unclaimedMRG = 0.000000;

      // Synchronize with userControls for 100% Admin & User Panel harmony
      if (typeof userControls !== 'undefined') {
        userControls.walletMRG = state.walletMRG;
        userControls.unclaimedMRG = 0.000000;
        userControls.totalHoldings = formatBalanceDisplay(state.walletMRG);
        saveUserControlsToStorage();
      }
      saveState();

      // Trigger fluid particle animation and update all home & wallet displays
      triggerClaimAnimation(claimed);
      updateAllBalanceDisplays(state.walletMRG, claimed);

      // Mascot coin celebratory spin burst
      const mascot = document.getElementById('mascotCoin');
      if (mascot) {
        mascot.classList.add('coin-spin-burst');
        setTimeout(() => mascot.classList.remove('coin-spin-burst'), 700);
      }

      const sym = appConfig.tokenSymbol || 'MRG';
      showToast(`🎉 Claimed +${claimed.toFixed(4)} ${sym} to Home Balance!`);
      
      addTransaction({
        type: 'claim',
        title: 'Cloud Mining Claim',
        amount: claimed,
        desc: `Mined by Level ${userControls.minerLevel || 1} Miner (${claimed.toFixed(4)} ${sym})`,
        status: 'Completed'
      });

      if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
        window.Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      }
    }'''

# Replace claimMiningReward and inject token_logo_and_anim_engine
if re.search(pattern, html):
    # Find the end of the existing claimMiningReward function
    match = re.search(pattern, html)
    start_pos = match.start()
    # Find matching closing brace
    # Search from start_pos to the next function comment
    end_pos = html.find('// Streak Check-in', start_pos)
    if end_pos != -1:
        html = html[:start_pos] + token_logo_and_anim_engine + '\n    ' + new_claim_mining_reward + '\n\n    ' + html[end_pos:]
        print("✓ Successfully replaced claimMiningReward with animated and home-synced engine")
    else:
        print("! Could not find // Streak Check-in end marker")

# Also enhance Mascot Coin Click with animated squash, stretch, and sound
old_mascot_click = '''    // Tap on Mascot Coin
    const mascotCoin = document.getElementById('mascotCoin');
    const coinStage = document.getElementById('coinStage');
    if (mascotCoin && coinStage) {
      mascotCoin.addEventListener('click', (e) => {
        soundTap();
        state.unclaimedMRG += 0.0001;
        document.getElementById('unclaimedVal').innerText = state.unclaimedMRG.toFixed(6);

        // Spawn floating text particle
        const particle = document.createElement('div');
        particle.className = 'tap-particle';
        particle.innerText = '+0.0001';
        particle.style.left = '50%';
        particle.style.top = '45%';
        coinStage.appendChild(particle);
        setTimeout(() => particle.remove(), 800);

        if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
          window.Telegram.WebApp.HapticFeedback.impactOccurred('medium');
        }
      });
    }'''

new_mascot_click = '''    // Tap on Mascot Coin (ANIMATED SQUASH & FLOATING PARTICLES)
    const mascotCoin = document.getElementById('mascotCoin');
    const coinStage = document.getElementById('coinStage');
    if (mascotCoin && coinStage) {
      mascotCoin.addEventListener('click', (e) => {
        soundTap();
        const tapReward = 0.001;
        state.unclaimedMRG += tapReward;
        document.getElementById('unclaimedVal').innerText = state.unclaimedMRG.toFixed(6);
        const btnVal = document.getElementById('btnClaimVal');
        if (btnVal) btnVal.innerText = state.unclaimedMRG.toFixed(4);

        // Mascot coin squash & stretch animation
        mascotCoin.classList.remove('mascot-tap-anim');
        void mascotCoin.offsetWidth;
        mascotCoin.classList.add('mascot-tap-anim');

        // Spawn floating text particle with slight random offset
        const particle = document.createElement('div');
        particle.className = 'tap-particle';
        particle.innerText = `+${tapReward.toFixed(3)}`;
        const randX = 50 + (Math.random() * 24 - 12);
        const randY = 45 + (Math.random() * 16 - 8);
        particle.style.left = `${randX}%`;
        particle.style.top = `${randY}%`;
        coinStage.appendChild(particle);
        setTimeout(() => particle.remove(), 850);

        if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
          window.Telegram.WebApp.HapticFeedback.impactOccurred('medium');
        }
      });
    }'''

if old_mascot_click in html:
    html = html.replace(old_mascot_click, new_mascot_click)
    print("✓ Successfully upgraded Mascot Coin click with fluid squash animation")

# Enhance Streak Check-in with 3D card flip animation & home screen balance update
old_streak_func = '''    // Streak Check-in
    function claimStreakDay(day) {
      if (state.streakDay >= day) {
        showToast('Already checked in for today!');
        return;
      }
      soundClaim();
      state.streakDay = day;
      const reward = 5 + day;
      state.walletMRG += reward;
      state.topMRG += reward;

      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';

      const dCard = document.getElementById(`streakD${day}`);
      if (dCard) {
        dCard.classList.remove('pending', 'today');
        dCard.classList.add('completed');
        dCard.innerHTML = `<span class="streak-day-label">D${day}</span><div class="streak-icon-circle">✓</div><span class="streak-reward-text">+${reward}</span>`;
      }
      const sBadge = document.getElementById('streakBadge');
      if (sBadge) sBadge.innerText = `Day ${day} of 7`;

      showToast(`🔥 Day ${day} Streak claimed! +${reward} MRG added.`);
      addTransaction({
        type: 'reward',
        title: `Daily Check-in: Day ${day}`,
        amount: reward,
        desc: 'Consecutive check-in bonus',
        status: 'Completed'
      });
      saveState();
    }'''

new_streak_func = '''    // Streak Check-in (ANIMATED 3D FLIP & HOME SCREEN SYNC)
    function claimStreakDay(day) {
      if (state.streakDay >= day && userControls.streakTodayChecked) {
        showToast('Already checked in for today!');
        return;
      }
      soundClaim();
      state.streakDay = day;
      const reward = 5 + day;
      state.walletMRG = (parseFloat(state.walletMRG) || 0) + reward;
      state.topMRG = state.walletMRG;

      if (typeof userControls !== 'undefined') {
        userControls.walletMRG = state.walletMRG;
        userControls.streakDay = day;
        userControls.streakTodayChecked = true;
        userControls.totalHoldings = formatBalanceDisplay(state.walletMRG);
        saveUserControlsToStorage();
      }

      updateAllBalanceDisplays(state.walletMRG, reward);

      const dCard = document.getElementById(`streakD${day}`);
      if (dCard) {
        dCard.classList.remove('pending', 'today');
        dCard.classList.add('completed', 'streak-flip-anim');
        dCard.innerHTML = `<span class="streak-day-label">D${day}</span><div class="streak-icon-circle">✓</div><span class="streak-reward-text">+${reward}</span>`;
      }
      const sBadge = document.getElementById('streakBadge');
      if (sBadge) sBadge.innerText = `Day ${day} of 7`;

      showToast(`🔥 Day ${day} Streak claimed! +${reward} ${appConfig.tokenSymbol} added to Home Balance.`);
      addTransaction({
        type: 'reward',
        title: `Daily Check-in: Day ${day}`,
        amount: reward,
        desc: 'Consecutive check-in bonus',
        status: 'Completed'
      });
      saveState();
      if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
        window.Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      }
    }'''

if old_streak_func in html:
    html = html.replace(old_streak_func, new_streak_func)
    print("✓ Upgraded Streak Check-in with 3D card flip & home balance sync")

# Update task completion in renderUserTasks to use updateAllBalanceDisplays
old_task_complete = '''        task.completed = true;
        state.walletMRG += task.reward;
        state.topMRG += task.reward;
        document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
        document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';
        showToast(`✅ Task Completed! +${task.reward} ${appConfig.tokenSymbol} added.`);'''

new_task_complete = '''        task.completed = true;
        state.walletMRG = (parseFloat(state.walletMRG) || 0) + task.reward;
        state.topMRG = state.walletMRG;
        if (typeof userControls !== 'undefined') {
          userControls.walletMRG = state.walletMRG;
          userControls.totalHoldings = formatBalanceDisplay(state.walletMRG);
          saveUserControlsToStorage();
        }
        updateAllBalanceDisplays(state.walletMRG, task.reward);
        showToast(`✅ Task Completed! +${task.reward} ${appConfig.tokenSymbol} added to Home Balance.`);'''

if old_task_complete in html:
    html = html.replace(old_task_complete, new_task_complete)
    print("✓ Upgraded Task completion to sync with home balance")

# Update DEX Swap in simulateSwap to use updateAllBalanceDisplays
old_dex_swap = '''    function simulateSwap() {
      soundSuccess();
      closeBuyModal();
      const depositAmt = 50.0;
      state.walletMRG += depositAmt;
      state.topMRG += depositAmt;
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';
      showToast(`🎉 Swapped GRAM for +${depositAmt} MRG!`);'''

new_dex_swap = '''    function simulateSwap() {
      soundSuccess();
      closeBuyModal();
      const depositAmt = 50.0;
      state.walletMRG = (parseFloat(state.walletMRG) || 0) + depositAmt;
      state.topMRG = state.walletMRG;
      if (typeof userControls !== 'undefined') {
        userControls.walletMRG = state.walletMRG;
        userControls.totalHoldings = formatBalanceDisplay(state.walletMRG);
        saveUserControlsToStorage();
      }
      updateAllBalanceDisplays(state.walletMRG, depositAmt);
      showToast(`🎉 Swapped GRAM for +${depositAmt} ${appConfig.tokenSymbol}! Added to Home Balance.`);'''

if old_dex_swap in html:
    html = html.replace(old_dex_swap, new_dex_swap)
    print("✓ Upgraded DEX Swap to sync with home balance")

# Update switchTab for smooth animated scrolling
old_switch_tab = '''    // Switch Tabs
    function switchTab(tabId) {
      soundTap();
      document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.nav-tab').forEach(n => n.classList.remove('active'));

      const target = document.getElementById(`tab-${tabId}`);
      const nav = document.getElementById(`nav-${tabId}`);
      if (target) target.classList.add('active');
      if (nav) nav.classList.add('active');
    }'''

new_switch_tab = '''    // Switch Tabs (ANIMATED SMOOTH TRANSITION)
    function switchTab(tabId) {
      soundTap();
      document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.nav-tab').forEach(n => n.classList.remove('active'));

      const target = document.getElementById(`tab-${tabId}`);
      const nav = document.getElementById(`nav-${tabId}`);
      if (target) {
        target.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
      if (nav) nav.classList.add('active');

      if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
        window.Telegram.WebApp.HapticFeedback.selectionChanged();
      }
    }'''

if old_switch_tab in html:
    html = html.replace(old_switch_tab, new_switch_tab)
    print("✓ Upgraded switchTab with smooth scroll & haptic selection")

# Update executeCleanAllAppData to clean demo token hold, demo miner level, demo mining speed
old_clean_func = '''    function executeCleanAllAppData() {
      // 1. Clear all localStorage keys
      try {
        localStorage.removeItem('mrg_miner_state');
        localStorage.removeItem('mrg_app_config');
        localStorage.removeItem('mrg_custom_tasks');
        localStorage.removeItem('mrg_user_controls');
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

      // 4b. Reset userControls to clean baseline
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
    }'''

new_clean_func = '''    function executeCleanAllAppData() {
      // 1. Clear all localStorage keys
      try {
        localStorage.removeItem('mrg_miner_state');
        localStorage.removeItem('mrg_app_config');
        localStorage.removeItem('mrg_custom_tasks');
        localStorage.removeItem('mrg_user_controls');
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

      // 4b. Reset userControls to clean baseline (DEMO HOLD, MINER LEVEL 1, MINING SPEED 1.00 MH/s CLEANED)
      userControls = Object.assign({}, defaultUserControls, {
        userName: 'Telegram Miner',
        userHandle: '@telegram_miner',
        tonWallet: 'UQBFoMy-deRHYz842P39910y-deRH',
        walletMRG: 0.0,
        unclaimedMRG: 0.000000,
        totalHoldings: '0.00',
        minerLevel: 1,
        peakLevel: 1,
        baseHashrate: '1.00 MH/s',
        todaysPnl: '+0.00',
        allTimeMined: '0.00',
        speedMultiplier: 1,
        streakDay: 1,
        streakTodayChecked: false
      });
      saveUserControlsToStorage();

      // 5. Reset appConfig to clean baseline
      appConfig = Object.assign({}, defaultConfig, {
        appName: 'MRG Miner',
        tokenSymbol: 'MRG',
        tokenPriceUSD: 0.00128,
        baseHashrate: '1.00 MH/s',
        userName: 'Telegram Miner',
        userHandle: '@telegram_miner',
        tonWallet: 'UQBFoMy-deRHYz842P39910y-deRH'
      });

      // 6. Auto-sync directly from Telegram WebApp
      const synced = autoSyncTelegramData(false);

      // 7. Update all UI elements with clean values
      updateAllBalanceDisplays(0.0, 0);
      const subrateEl = document.querySelector('.unclaimed-subrate');
      if (subrateEl) subrateEl.innerText = `≈ $0.0000 · ${appConfig.baseHashrate}`;

      renderTransactions();
      renderUserTasks();
      renderAdminTasks();
      applyUserControls();
      applyGlobalConfig();
      populateUserControlInputs();
      saveState();

      closeCleanDataModal();
      soundSuccess();
      if (synced) {
        showToast(`🧹 Cleaned demo records! Auto-synced with Telegram: ${appConfig.userHandle}`);
      } else {
        showToast('🧹 Cleaned demo records, miner level 1, and mining speed!');
      }
    }'''

if old_clean_func in html:
    html = html.replace(old_clean_func, new_clean_func)
    print("✓ Upgraded executeCleanAllAppData with clean demo records")

# Also in applyGlobalConfig(), ensure tokenLogo is applied
old_apply_global = '''    function applyGlobalConfig() {
      const sym = appConfig.tokenSymbol || 'MRG';
      const name = appConfig.appName || 'MRG Miner';
      const price = appConfig.tokenPriceUSD || 0.00128;'''

new_apply_global = '''    function applyGlobalConfig() {
      const sym = appConfig.tokenSymbol || 'MRG';
      const name = appConfig.appName || 'MRG Miner';
      const price = appConfig.tokenPriceUSD || 0.00128;

      if (appConfig.tokenLogo) {
        applyTokenLogo(appConfig.tokenLogo);
      }'''

if old_apply_global in html:
    html = html.replace(old_apply_global, new_apply_global)
    print("✓ Integrated tokenLogo auto-application into applyGlobalConfig")

# In DOMContentLoaded, auto-clean cached demo data (v4) and update Home screen
old_dom_loaded = '''      // Auto-sync Telegram credentials (display name, telegram handle, TON wallet)
      autoSyncTelegramData(false);
      // Render initial values
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';
      renderTransactions();
      renderUserTasks();
      renderAdminTasks();
      applyUserControls();
      applyGlobalConfig();
      populateUserControlInputs();'''

new_dom_loaded = '''      // Auto-sync Telegram credentials (display name, telegram handle, TON wallet)
      autoSyncTelegramData(false);

      // Auto-clean old demo values (clean demo token hold, demo miner level 1, demo speed 1.00 MH/s)
      try {
        const cleanedV4 = localStorage.getItem('mrg_cleaned_v4');
        if (!cleanedV4) {
          // If stored userControls had legacy demo 83 or 2.1K
          if (userControls.minerLevel === 83 || userControls.totalHoldings === '2.1K') {
            userControls.minerLevel = 1;
            userControls.peakLevel = 1;
            userControls.totalHoldings = '0.00';
            userControls.baseHashrate = '1.00 MH/s';
            userControls.todaysPnl = '+0.00';
            userControls.allTimeMined = '0.00';
            saveUserControlsToStorage();
          }
          if (appConfig.baseHashrate === '3.19 TH/s') {
            appConfig.baseHashrate = '1.00 MH/s';
            try { localStorage.setItem('mrg_app_config', JSON.stringify(appConfig)); } catch (e) {}
          }
          localStorage.setItem('mrg_cleaned_v4', 'true');
        }
      } catch (e) {}

      // Render initial values and sync Home Screen balance
      updateAllBalanceDisplays(state.walletMRG || 0.0, 0);
      renderTransactions();
      renderUserTasks();
      renderAdminTasks();
      applyUserControls();
      applyGlobalConfig();
      populateUserControlInputs();'''

if old_dom_loaded in html:
    html = html.replace(old_dom_loaded, new_dom_loaded)
    print("✓ Upgraded DOMContentLoaded initialization and balance sync")

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished inject_token_logo_and_animations.py successfully!")
