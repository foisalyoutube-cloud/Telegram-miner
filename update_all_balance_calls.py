#!/usr/bin/env python3

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update claimStreakDay
old_streak = '''    // Streak Check-in
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
        dCard.classList.remove('pending');
        dCard.classList.add('completed');
        dCard.querySelector('.streak-icon-circle').innerText = '✓';
      }
      document.getElementById('streakBadge').innerText = `Day ${day} of 7`;
      document.getElementById('btnDailyCheckin').innerText = 'Checked in today';
      document.getElementById('btnDailyCheckin').classList.remove('active-claim');

      showToast(`🔥 Day ${day} Check-in complete! +${reward} MRG added`);
      addTransaction({
        type: 'deposit',
        title: `Streak Day ${day} Bonus`,
        amount: reward,
        desc: 'Daily check-in streak reward',
        status: 'Completed'
      });
      saveState();
    }'''

new_streak = '''    // Streak Check-in (ANIMATED 3D FLIP & HOME SCREEN SYNC)
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
      triggerClaimAnimation(reward);

      const dCard = document.getElementById(`streakD${day}`);
      if (dCard) {
        dCard.classList.remove('pending');
        dCard.classList.add('completed', 'streak-flip-anim');
        const iconCircle = dCard.querySelector('.streak-icon-circle');
        if (iconCircle) iconCircle.innerText = '✓';
      }
      const sBadge = document.getElementById('streakBadge');
      if (sBadge) sBadge.innerText = `Day ${day} of 7`;
      const btnCheckin = document.getElementById('btnDailyCheckin');
      if (btnCheckin) {
        btnCheckin.innerText = 'Checked in today ✓';
        btnCheckin.classList.remove('active-claim');
      }

      const sym = appConfig.tokenSymbol || 'MRG';
      showToast(`🔥 Day ${day} Check-in claimed! +${reward} ${sym} added to Home Balance`);
      addTransaction({
        type: 'reward',
        title: `Streak Day ${day} Bonus`,
        amount: reward,
        desc: 'Daily check-in streak reward',
        status: 'Completed'
      });
      saveState();
      if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {
        window.Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      }
    }'''

if old_streak in html:
    html = html.replace(old_streak, new_streak)
    print("✓ Successfully replaced claimStreakDay")
else:
    print("! Could not find old_streak")

# 2. Update executeTask
old_exec_task = '''    // Tasks Execution
    function executeTask(itemEl, taskTitle, reward) {
      soundTap();
      showToast(`Checking task: ${taskTitle}...`);
      setTimeout(() => {
        soundSuccess();
        state.walletMRG += reward;
        state.topMRG += reward;
        document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
        document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';
        itemEl.style.opacity = '0.5';
        itemEl.style.pointerEvents = 'none';
        const rightBadge = itemEl.querySelector('.task-timer-badge') || itemEl.querySelector('.task-claim-btn');
        if (rightBadge) rightBadge.innerText = 'Completed ✓';
        showToast(`✅ Task Completed! +${reward} MRG added.`);
        addTransaction({
          type: 'deposit',
          title: `Task: ${taskTitle}`,
          amount: reward,
          desc: 'Partner quest completion reward',
          status: 'Completed'
        });
        saveState();
      }, 1200);
    }'''

new_exec_task = '''    // Tasks Execution (ANIMATED & HOME SCREEN SYNC)
    function executeTask(itemEl, taskTitle, reward) {
      soundTap();
      showToast(`Checking task: ${taskTitle}...`);
      setTimeout(() => {
        soundSuccess();
        state.walletMRG = (parseFloat(state.walletMRG) || 0) + reward;
        state.topMRG = state.walletMRG;

        if (typeof userControls !== 'undefined') {
          userControls.walletMRG = state.walletMRG;
          userControls.totalHoldings = formatBalanceDisplay(state.walletMRG);
          saveUserControlsToStorage();
        }

        updateAllBalanceDisplays(state.walletMRG, reward);
        triggerClaimAnimation(reward);

        itemEl.style.opacity = '0.6';
        itemEl.style.pointerEvents = 'none';
        const rightBadge = itemEl.querySelector('.task-timer-badge') || itemEl.querySelector('.task-claim-btn');
        if (rightBadge) rightBadge.innerText = 'Completed ✓';

        const sym = appConfig.tokenSymbol || 'MRG';
        showToast(`✅ Task Completed! +${reward} ${sym} added to Home Balance.`);
        addTransaction({
          type: 'deposit',
          title: `Task: ${taskTitle}`,
          amount: reward,
          desc: 'Partner quest completion reward',
          status: 'Completed'
        });
        saveState();
      }, 1200);
    }'''

if old_exec_task in html:
    html = html.replace(old_exec_task, new_exec_task)
    print("✓ Successfully replaced executeTask")
else:
    print("! Could not find old_exec_task")

# 3. Update confirmWithdraw
old_withdraw = '''      soundSuccess();
      state.walletMRG -= amt;
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      closeWithdrawModal();'''

new_withdraw = '''      soundSuccess();
      state.walletMRG = Math.max(0, (parseFloat(state.walletMRG) || 0) - amt);
      state.topMRG = state.walletMRG;
      if (typeof userControls !== 'undefined') {
        userControls.walletMRG = state.walletMRG;
        userControls.totalHoldings = formatBalanceDisplay(state.walletMRG);
        saveUserControlsToStorage();
      }
      updateAllBalanceDisplays(state.walletMRG, -amt);
      closeWithdrawModal();'''

if old_withdraw in html:
    html = html.replace(old_withdraw, new_withdraw)
    print("✓ Successfully replaced confirmWithdraw")
else:
    print("! Could not find old_withdraw")

# 4. Update simulateSwap
old_swap = '''    function simulateSwap() {
      soundSuccess();
      closeBuyModal();
      const depositAmt = 50.0;
      state.walletMRG += depositAmt;
      state.topMRG += depositAmt;
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';
      addTransaction({
        type: 'deposit',
        title: 'Swap GRAM for MRG (STON.fi)',
        amount: depositAmt,
        desc: 'Decentralized exchange liquidity pool swap (0.0625 TON -> 50 MRG)',
        status: 'Completed'
      });
      showToast('🎉 Deposit successful! +50.0 MRG from STON.fi added.');
      saveState();
    }'''

new_swap = '''    function simulateSwap() {
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
      triggerClaimAnimation(depositAmt);

      const sym = appConfig.tokenSymbol || 'MRG';
      addTransaction({
        type: 'deposit',
        title: `Swap GRAM for ${sym} (STON.fi)`,
        amount: depositAmt,
        desc: `Decentralized exchange liquidity pool swap (0.0625 TON -> 50 ${sym})`,
        status: 'Completed'
      });
      showToast(`🎉 Deposit successful! +50.0 ${sym} added to Home Balance.`);
      saveState();
    }'''

if old_swap in html:
    html = html.replace(old_swap, new_swap)
    print("✓ Successfully replaced simulateSwap")
else:
    print("! Could not find old_swap")

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished update_all_balance_calls.py successfully!")
