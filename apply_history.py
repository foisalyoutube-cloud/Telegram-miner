with open('generate_html.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the state initialization
old_state = """    // State
    const state = {
      currentTab: 'mine',
      topMRG: 2100.0,
      walletMRG: 94.0,
      unclaimedMRG: 0.002938,
      miningRatePerSec: 0.0000085,
      streakDay: 2,
      lang: 'en'
    };"""

new_state = """    // Default History
    const defaultTransactions = [
      {
        id: 'tx_1',
        type: 'withdraw',
        title: 'Withdraw to TON Wallet',
        amount: -20.0,
        currency: 'MRG',
        status: 'Completed',
        time: 'Yesterday, 04:30 PM',
        hash: 'ton_tx_09af82e3b1',
        desc: 'Sent to UQBFoM...y-deRH (Gas Fee: 0.05 TON)'
      },
      {
        id: 'tx_2',
        type: 'claim',
        title: 'Cloud Mining Claim',
        amount: 14.8500,
        currency: 'MRG',
        status: 'Completed',
        time: 'Yesterday, 10:15 AM',
        hash: 'ton_claim_8b31c9a',
        desc: 'Mined at 3.19 TH/s by Level 83 Miner'
      },
      {
        id: 'tx_3',
        type: 'deposit',
        title: 'DEX Buy MRG (STON.fi)',
        amount: 100.0,
        currency: 'MRG',
        status: 'Completed',
        time: 'Oct 17, 2026',
        hash: 'ston_swap_7c29e1',
        desc: 'Swapped 0.125 TON for 100 MRG on DEX'
      },
      {
        id: 'tx_4',
        type: 'claim',
        title: 'Cloud Mining Claim',
        amount: 8.2140,
        currency: 'MRG',
        status: 'Completed',
        time: 'Oct 16, 2026',
        hash: 'ton_claim_5f12a8',
        desc: 'Mined at 3.19 TH/s by Level 83 Miner'
      },
      {
        id: 'tx_5',
        type: 'deposit',
        title: 'Squad Mining Bonus',
        amount: 10.0,
        currency: 'MRG',
        status: 'Completed',
        time: 'Oct 16, 2026',
        hash: 'squad_ref_18b9c',
        desc: '10% bonus share from squad member Alex'
      }
    ];

    // State
    const state = {
      currentTab: 'mine',
      topMRG: 2100.0,
      walletMRG: 94.0,
      unclaimedMRG: 0.002938,
      miningRatePerSec: 0.0000085,
      streakDay: 2,
      lang: 'en',
      txFilter: 'all',
      transactions: defaultTransactions,
      selectedTx: null
    };"""

text = text.replace(old_state, new_state)

# Replace parse state
old_parse = """        state.lang = parsed.lang ?? state.lang;
      }
    } catch (e) {}"""

new_parse = """        state.lang = parsed.lang ?? state.lang;
        if (parsed.transactions && Array.isArray(parsed.transactions)) {
          state.transactions = parsed.transactions;
        }
      }
    } catch (e) {}"""

text = text.replace(old_parse, new_parse)

# Add transaction helpers and methods
tx_methods = """
    // Transaction History Functions
    function addTransaction(tx) {
      const now = new Date();
      const hours = now.getHours();
      const minutes = String(now.getMinutes()).padStart(2, '0');
      const ampm = hours >= 12 ? 'PM' : 'AM';
      const formattedTime = `Today, ${hours % 12 || 12}:${minutes} ${ampm}`;

      const newTx = {
        id: 'tx_' + Date.now().toString(36),
        type: tx.type,
        title: tx.title,
        amount: tx.amount,
        currency: 'MRG',
        status: tx.status || 'Completed',
        time: tx.time || formattedTime,
        hash: tx.hash || ('ton_' + Math.random().toString(36).substring(2, 10)),
        desc: tx.desc || 'Transaction verified on TON blockchain'
      };
      state.transactions.unshift(newTx);
      if (state.transactions.length > 50) state.transactions.pop();
      saveState();
      renderTransactions();
    }

    function setTxFilter(filter, el) {
      soundTap();
      state.txFilter = filter;
      document.querySelectorAll('.history-filter-chip').forEach(c => c.classList.remove('active'));
      if (el) el.classList.add('active');
      renderTransactions();
    }

    function renderTransactions() {
      const container = document.getElementById('txHistoryContainer');
      const badge = document.getElementById('txCountBadge');
      if (!container) return;

      let list = state.transactions;
      if (state.txFilter !== 'all') {
        list = list.filter(t => t.type === state.txFilter);
      }

      if (badge) {
        badge.innerText = `${list.length} item${list.length === 1 ? '' : 's'}`;
      }

      if (list.length === 0) {
        container.innerHTML = `
          <div class="empty-history-box">
            <div style="font-size: 26px; margin-bottom: 8px;">📂</div>
            <div style="font-weight: 600; color: #fff; margin-bottom: 4px;">No ${state.txFilter === 'all' ? '' : state.txFilter} records</div>
            <div style="font-size: 12px;">New transactions will appear here automatically.</div>
          </div>
        `;
        return;
      }

      container.innerHTML = list.map(tx => {
        const isPos = tx.amount > 0;
        const sign = isPos ? '+' : '';
        const amtFormatted = Math.abs(tx.amount) < 1 ? tx.amount.toFixed(4) : tx.amount.toFixed(1);
        const amtStr = sign + amtFormatted + ' MRG';
        const amtClass = isPos ? 'positive' : 'negative';

        let icon = '⛏️';
        if (tx.type === 'withdraw') icon = '↗';
        else if (tx.type === 'deposit') icon = '📥';
        else if (tx.type === 'reward') icon = '🎁';

        const statusClass = (tx.status === 'Completed' || tx.status === 'Confirmed') ? 'completed' : 'pending';

        return `
          <div class="tx-item-card" onclick="openTxDetailModal('${tx.id}')">
            <div class="tx-left">
              <div class="tx-icon-box ${tx.type}">${icon}</div>
              <div>
                <div class="tx-title">${tx.title}</div>
                <div class="tx-meta">
                  <span>${tx.time}</span>
                  <span>•</span>
                  <span class="tx-badge-status ${statusClass}">${tx.status}</span>
                </div>
              </div>
            </div>
            <div class="tx-right">
              <div class="tx-amount ${amtClass}">${amtStr}</div>
              <div class="tx-sub">${tx.type.toUpperCase()}</div>
            </div>
          </div>
        `;
      }).join('');
    }

    function openTxDetailModal(id) {
      soundTap();
      const tx = state.transactions.find(t => t.id === id);
      if (!tx) return;
      state.selectedTx = tx;
      document.getElementById('modalTxTitle').innerText = tx.title;
      document.getElementById('modalTxDesc').innerText = tx.desc || 'Transaction verified on The Open Network (TON).';
      const isPos = tx.amount > 0;
      const amtFormatted = Math.abs(tx.amount) < 1 ? tx.amount.toFixed(4) : tx.amount.toFixed(1);
      const amtStr = (isPos ? '+' : '') + amtFormatted + ' MRG';
      const amtEl = document.getElementById('modalTxAmount');
      amtEl.innerText = amtStr;
      amtEl.style.color = isPos ? 'var(--accent-green)' : '#ffffff';
      document.getElementById('modalTxType').innerText = tx.type.toUpperCase();
      document.getElementById('modalTxStatus').innerText = tx.status + ' ✓';
      document.getElementById('modalTxTime').innerText = tx.time;
      document.getElementById('modalTxHash').innerText = tx.hash;
      document.getElementById('txDetailModal').classList.add('show');
    }

    function closeTxModal() {
      document.getElementById('txDetailModal').classList.remove('show');
    }

    function viewOnExplorer() {
      soundTap();
      if (state.selectedTx) {
        showToast('Viewing on TonViewer: ' + state.selectedTx.hash);
      }
    }
"""

text = text.replace("    // Real-time ticking mining rate", tx_methods + "\n    // Real-time ticking mining rate")

# Now update claimMiningReward to log transaction
old_claim_call = """      showToast(`🎉 Claimed +${claimed.toFixed(4)} MRG to In-App Wallet!`);
      saveState();"""

new_claim_call = """      showToast(`🎉 Claimed +${claimed.toFixed(4)} MRG to In-App Wallet!`);
      addTransaction({
        type: 'claim',
        title: 'Cloud Mining Claim',
        amount: claimed,
        desc: `Mined 3.19 TH/s by Level 83 Miner (${claimed.toFixed(4)} MRG)`,
        status: 'Completed'
      });
      saveState();"""

text = text.replace(old_claim_call, new_claim_call)

# Update confirmWithdraw to log transaction
old_withdraw_call = """      showToast(`🚀 Withdrawal of ${amt} MRG submitted to TON mempool!`);
      saveState();"""

new_withdraw_call = """      showToast(`🚀 Withdrawal of ${amt} MRG submitted to TON mempool!`);
      const targetAddress = document.getElementById('withdrawAddress').value || 'UQBFoM...y-deRH';
      addTransaction({
        type: 'withdraw',
        title: 'Withdraw to TON Wallet',
        amount: -amt,
        desc: `Transfer to ${targetAddress} (Gas Fee: 0.05 TON)`,
        status: 'Confirmed'
      });
      saveState();"""

text = text.replace(old_withdraw_call, new_withdraw_call)

# Update simulateSwap to deposit MRG and log transaction
old_swap_call = """    function simulateSwap() {
      closeBuyModal();
      showToast('Opening STON.fi DEX swap pool...');
    }"""

new_swap_call = """    function simulateSwap() {
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
    }"""

text = text.replace(old_swap_call, new_swap_call)

# Update streak checkin to log transaction
old_streak_call = """      showToast(`🔥 Day ${day} Check-in complete! +${reward} MRG added`);
      saveState();"""

new_streak_call = """      showToast(`🔥 Day ${day} Check-in complete! +${reward} MRG added`);
      addTransaction({
        type: 'deposit',
        title: `Streak Day ${day} Check-in`,
        amount: reward,
        desc: 'Daily check-in streak reward',
        status: 'Completed'
      });
      saveState();"""

text = text.replace(old_streak_call, new_streak_call)

# Update tasks to log transaction
old_task_call = """        showToast(`✅ Task Completed! +${reward} MRG added.`);
        saveState();"""

new_task_call = """        showToast(`✅ Task Completed! +${reward} MRG added.`);
        addTransaction({
          type: 'deposit',
          title: `Task: ${taskTitle}`,
          amount: reward,
          desc: 'Partner quest completion reward',
          status: 'Completed'
        });
        saveState();"""

text = text.replace(old_task_call, new_task_call)

# Call renderTransactions() on init
old_init = """      // Render initial values
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';"""

new_init = """      // Render initial values
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';
      renderTransactions();"""

text = text.replace(old_init, new_init)

with open('generate_html.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("generate_html.py updated successfully!")
