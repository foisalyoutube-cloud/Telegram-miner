import re

with open('template.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Token Symbol input in Admin Panel to have oninput="autoUpdateTokenName(this.value)"
text = text.replace(
    '<input type="text" class="modal-input" id="cfgTokenSymbol" placeholder="e.g. MRG, NOT, DOGS" value="MRG">',
    '<input type="text" class="modal-input" id="cfgTokenSymbol" oninput="autoUpdateTokenName(this.value)" placeholder="e.g. MRG, NOT, DOGS, TON" value="MRG">'
)
text = text.replace(
    '<input type="text" class="modal-input" id="cfgAppName" placeholder="e.g. MRG Miner Bot" value="MRG Miner">',
    '<input type="text" class="modal-input" id="cfgAppName" oninput="autoUpdateAppName(this.value)" placeholder="e.g. MRG Miner" value="MRG Miner">'
)

# 2. In Tasks Tab, replace hardcoded task-items with dynamic userTasksList
old_user_tasks = """      <div class="section-header">
        <span class="section-title">TASKS</span>
        <span class="section-badge">5 available</span>
      </div>

      <div class="task-item" onclick="executeTask(this, 'Subscribe MRG Channel', 5)">
        <div class="task-left">
          <div class="task-logo tg">✈</div>
          <div>
            <div class="task-info-title">Subscribe MRG Channel</div>
            <div class="task-info-reward"><span class="gold">+5 MRG</span> · Every 24h</div>
          </div>
        </div>
        <div class="task-timer-badge">🕒 <span class="task-countdown">10:13:23</span></div>
      </div>

      <div class="task-item" onclick="executeTask(this, 'Follow MRG on X', 5)">
        <div class="task-left">
          <div class="task-logo tw">𝕏</div>
          <div>
            <div class="task-info-title">Follow MRG on X</div>
            <div class="task-info-reward"><span class="gold">+5 MRG</span></div>
          </div>
        </div>
        <button class="task-claim-btn">Check</button>
      </div>

      <div class="task-item" onclick="executeTask(this, 'Watch MRG YouTube Video', 10)">
        <div class="task-left">
          <div class="task-logo yt">▶</div>
          <div>
            <div class="task-info-title">Watch MRG YouTube</div>
            <div class="task-info-reward"><span class="gold">+10 MRG</span></div>
          </div>
        </div>
        <div class="task-timer-badge">🕒 <span class="task-countdown">07:38:07</span></div>
      </div>

      <div class="task-item" onclick="executeTask(this, 'Boost Mining Channel', 20)">
        <div class="task-left">
          <div class="task-logo boost">🚀</div>
          <div>
            <div class="task-info-title">Boost Mining Channel</div>
            <div class="task-info-reward"><span class="gold">+20 MRG</span> · Extra hash</div>
          </div>
        </div>
        <button class="task-claim-btn">Boost</button>
      </div>"""

new_user_tasks = """      <div class="section-header">
        <span class="section-title">TASKS &amp; QUESTS</span>
        <span class="section-badge" id="userTasksCountBadge">4 available</span>
      </div>

      <div id="userTasksList">
        <!-- Rendered dynamically by renderUserTasks() -->
      </div>"""

text = text.replace(old_user_tasks, new_user_tasks)

# 3. Upgrade Admin Tasks Tab in Admin Panel
old_admin_tasks_sec = """      <!-- ADMIN TAB 3: TASKS & QUESTS -->
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
      </div>"""

new_admin_tasks_sec = """      <!-- ADMIN TAB 3: TASKS & QUESTS -->
      <div class="admin-tab-section" id="admin-sec-tasks">
        <div class="admin-card">
          <div class="admin-card-title">
            <span>➕ Add New Quest / Task</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 12px;">
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Task Title</label>
              <input type="text" class="modal-input" id="newTaskTitle" placeholder="e.g. Join Community Chat" value="Join Official Community">
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Reward (<span class="token-sym">MRG</span>)</label>
                <input type="number" class="modal-input" id="newTaskReward" placeholder="Reward" value="25">
              </div>
              <div>
                <label class="admin-label" style="display: block; margin-bottom: 4px;">Category / Icon</label>
                <select class="modal-input" id="newTaskType" style="cursor: pointer;">
                  <option value="tg">Telegram (✈)</option>
                  <option value="tw">Twitter / X (𝕏)</option>
                  <option value="yt">YouTube (▶)</option>
                  <option value="boost">Boost Channel (🚀)</option>
                </select>
              </div>
            </div>
            <div>
              <label class="admin-label" style="display: block; margin-bottom: 4px;">Destination URL / Link</label>
              <input type="text" class="modal-input" id="newTaskLink" placeholder="https://t.me/..." value="https://t.me/mrgminer">
            </div>
            <button class="admin-btn green" style="padding: 12px; font-size: 14px;" onclick="adminCreateTask()">
              ➕ Publish Quest to User Panel
            </button>
          </div>
        </div>

        <div class="admin-card">
          <div class="admin-card-title">
            <span>📋 Active Quests Management</span>
            <span class="badge-chip verified" id="adminTasksCountBadge">4 Quests</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            Edit rewards, rename tasks, or delete quests. Changes update the user panel immediately.
          </p>
          <div id="adminTasksList">
            <!-- Populated dynamically by renderAdminTasks() -->
          </div>
        </div>
      </div>"""

text = text.replace(old_admin_tasks_sec, new_admin_tasks_sec)

# 4. Add Edit Task Modal
edit_task_modal = """
  <!-- Edit Task Modal -->
  <div class="modal-backdrop" id="editTaskModal">
    <div class="modal-sheet">
      <div class="modal-title">Edit Quest / Task</div>
      <div class="modal-desc">Modify quest requirements and token rewards.</div>
      <input type="hidden" id="editTaskId">
      <label class="admin-label" style="display: block; margin-bottom: 4px;">Task Title</label>
      <input type="text" class="modal-input" id="editTaskTitle" placeholder="Task Title">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
        <div>
          <label class="admin-label" style="display: block; margin-bottom: 4px;">Reward (<span class="token-sym">MRG</span>)</label>
          <input type="number" class="modal-input" id="editTaskReward" placeholder="Reward">
        </div>
        <div>
          <label class="admin-label" style="display: block; margin-bottom: 4px;">Category</label>
          <select class="modal-input" id="editTaskType">
            <option value="tg">Telegram (✈)</option>
            <option value="tw">Twitter / X (𝕏)</option>
            <option value="yt">YouTube (▶)</option>
            <option value="boost">Boost Channel (🚀)</option>
          </select>
        </div>
      </div>
      <label class="admin-label" style="display: block; margin-bottom: 4px;">Link URL</label>
      <input type="text" class="modal-input" id="editTaskLink" placeholder="https://...">
      <button class="modal-btn-confirm" onclick="saveEditedTask()">Save Changes</button>
      <button class="modal-btn-confirm" style="background: transparent; color: var(--text-muted); margin-top: 8px;" onclick="closeEditTaskModal()">Cancel</button>
    </div>
  </div>
"""

text = text.replace("  <!-- Transaction Details Modal -->", edit_task_modal + "\n  <!-- Transaction Details Modal -->")

# 5. Add Task and Token Dynamic Engine to JavaScript
tasks_and_token_js = """
    // ==========================================
    // DYNAMIC TASKS & QUESTS SYSTEM
    // ==========================================
    const defaultTasks = [
      {
        id: 'task_1',
        title: 'Subscribe Telegram Channel',
        reward: 5,
        type: 'tg',
        icon: '✈',
        desc: 'Every 24h',
        timer: '10:13:23',
        link: 'https://t.me/mrgminer',
        completed: false
      },
      {
        id: 'task_2',
        title: 'Follow Official X / Twitter',
        reward: 5,
        type: 'tw',
        icon: '𝕏',
        desc: 'One-time bonus',
        timer: null,
        link: 'https://x.com/mrgminer',
        completed: false
      },
      {
        id: 'task_3',
        title: 'Watch YouTube Video',
        reward: 10,
        type: 'yt',
        icon: '▶',
        desc: 'Watch 60 seconds',
        timer: '07:38:07',
        link: 'https://youtube.com',
        completed: false
      },
      {
        id: 'task_4',
        title: 'Boost Mining Channel',
        reward: 20,
        type: 'boost',
        icon: '🚀',
        desc: 'Extra hash allocation',
        timer: null,
        link: 'https://t.me/boost/mrgminer',
        completed: false
      }
    ];

    let userTasks = defaultTasks.slice();
    try {
      const savedTasks = localStorage.getItem('mrg_custom_tasks');
      if (savedTasks) {
        userTasks = JSON.parse(savedTasks);
      }
    } catch (e) {}

    function saveTasksToStorage() {
      try {
        localStorage.setItem('mrg_custom_tasks', JSON.stringify(userTasks));
      } catch (e) {}
    }

    function renderUserTasks() {
      const container = document.getElementById('userTasksList');
      const badge = document.getElementById('userTasksCountBadge');
      if (!container) return;

      const activeCount = userTasks.filter(t => !t.completed).length;
      if (badge) badge.innerText = `${activeCount} available`;

      container.innerHTML = userTasks.map(task => {
        let logoClass = task.type || 'tg';
        let icon = '★';
        if (task.type === 'tg') icon = '✈';
        else if (task.type === 'tw') icon = '𝕏';
        else if (task.type === 'yt') icon = '▶';
        else if (task.type === 'boost') icon = '🚀';

        let rightBadge = '';
        if (task.completed) {
          rightBadge = `<div class="task-timer-badge" style="color: var(--accent-green); border-color: rgba(0,201,128,0.3);">Completed ✓</div>`;
        } else if (task.timer) {
          rightBadge = `<div class="task-timer-badge">🕒 <span>${task.timer}</span></div>`;
        } else {
          rightBadge = `<button class="task-claim-btn" onclick="event.stopPropagation(); executeTaskItem('${task.id}')">Start</button>`;
        }

        return `
          <div class="task-item" style="${task.completed ? 'opacity: 0.6;' : ''}" onclick="executeTaskItem('${task.id}')">
            <div class="task-left">
              <div class="task-logo ${logoClass}">${icon}</div>
              <div>
                <div class="task-info-title">${task.title}</div>
                <div class="task-info-reward"><span class="gold">+${task.reward} <span class="token-sym">${appConfig.tokenSymbol}</span></span> · ${task.desc || 'Quest'}</div>
              </div>
            </div>
            <div>${rightBadge}</div>
          </div>
        `;
      }).join('');
    }

    function renderAdminTasks() {
      const container = document.getElementById('adminTasksList');
      const badge = document.getElementById('adminTasksCountBadge');
      if (!container) return;

      if (badge) badge.innerText = `${userTasks.length} Quests`;

      if (userTasks.length === 0) {
        container.innerHTML = `<div style="text-align: center; color: var(--text-muted); padding: 14px; font-size: 13px;">No active quests. Add a new quest above!</div>`;
        return;
      }

      container.innerHTML = userTasks.map(task => {
        let icon = '★';
        if (task.type === 'tg') icon = '✈';
        else if (task.type === 'tw') icon = '𝕏';
        else if (task.type === 'yt') icon = '▶';
        else if (task.type === 'boost') icon = '🚀';

        return `
          <div style="background: #090e17; border-radius: 12px; padding: 12px; margin-bottom: 8px; border: 1px solid #1c2b42;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <strong style="color: #fff; font-size: 14px;">${icon} ${task.title}</strong>
              <span style="color: var(--accent-gold); font-weight: 800; font-size: 13px;">+${task.reward} <span class="token-sym">${appConfig.tokenSymbol}</span></span>
            </div>
            <div style="font-size: 11px; color: var(--text-gray); margin-bottom: 8px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              Link: ${task.link || 'N/A'} • Type: ${task.type.toUpperCase()}
            </div>
            <div style="display: flex; gap: 6px;">
              <button class="admin-btn" style="flex: 1; padding: 6px; font-size: 12px; background: #192a3e;" onclick="openEditTaskModal('${task.id}')">✏️ Edit</button>
              <button class="admin-btn red" style="flex: 1; padding: 6px; font-size: 12px;" onclick="adminDeleteTask('${task.id}')">🗑️ Delete</button>
            </div>
          </div>
        `;
      }).join('');
    }

    function executeTaskItem(id) {
      soundTap();
      const task = userTasks.find(t => t.id === id);
      if (!task) return;
      if (task.completed) {
        showToast('Task already completed!');
        return;
      }
      showToast(`Checking task: ${task.title}...`);
      setTimeout(() => {
        soundSuccess();
        task.completed = true;
        state.walletMRG += task.reward;
        state.topMRG += task.reward;
        document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
        document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';
        showToast(`✅ Task Completed! +${task.reward} ${appConfig.tokenSymbol} added.`);
        addTransaction({
          type: 'deposit',
          title: `Task: ${task.title}`,
          amount: task.reward,
          desc: 'Partner quest completion reward',
          status: 'Completed'
        });
        saveTasksToStorage();
        saveState();
        renderUserTasks();
      }, 1000);
    }

    function adminCreateTask() {
      soundSuccess();
      const title = document.getElementById('newTaskTitle').value.trim() || 'Community Quest';
      const reward = parseFloat(document.getElementById('newTaskReward').value) || 10;
      const type = document.getElementById('newTaskType').value || 'tg';
      const link = document.getElementById('newTaskLink').value.trim() || 'https://t.me/mrgminer';

      const newTask = {
        id: 'task_' + Date.now().toString(36),
        title: title,
        reward: reward,
        type: type,
        icon: '★',
        desc: 'Special community quest',
        timer: null,
        link: link,
        completed: false
      };

      userTasks.unshift(newTask);
      saveTasksToStorage();
      renderUserTasks();
      renderAdminTasks();
      showToast(`✅ Quest "${title}" published (+${reward} ${appConfig.tokenSymbol})!`);
    }

    function adminDeleteTask(id) {
      soundTap();
      const idx = userTasks.findIndex(t => t.id === id);
      if (idx !== -1) {
        const removed = userTasks.splice(idx, 1)[0];
        saveTasksToStorage();
        renderUserTasks();
        renderAdminTasks();
        showToast(`🗑️ Task "${removed.title}" deleted.`);
      }
    }

    function openEditTaskModal(id) {
      soundTap();
      const task = userTasks.find(t => t.id === id);
      if (!task) return;
      document.getElementById('editTaskId').value = task.id;
      document.getElementById('editTaskTitle').value = task.title;
      document.getElementById('editTaskReward').value = task.reward;
      document.getElementById('editTaskType').value = task.type || 'tg';
      document.getElementById('editTaskLink').value = task.link || '';
      document.getElementById('editTaskModal').classList.add('show');
    }

    function closeEditTaskModal() {
      document.getElementById('editTaskModal').classList.remove('show');
    }

    function saveEditedTask() {
      soundSuccess();
      const id = document.getElementById('editTaskId').value;
      const task = userTasks.find(t => t.id === id);
      if (!task) return;

      task.title = document.getElementById('editTaskTitle').value.trim() || task.title;
      task.reward = parseFloat(document.getElementById('editTaskReward').value) || task.reward;
      task.type = document.getElementById('editTaskType').value;
      task.link = document.getElementById('editTaskLink').value.trim();

      saveTasksToStorage();
      renderUserTasks();
      renderAdminTasks();
      closeEditTaskModal();
      showToast(`✅ Task "${task.title}" updated!`);
    }

    // ==========================================
    // AUTO TOKEN & APP NAME REAL-TIME SYNC
    // ==========================================
    function autoUpdateTokenName(val) {
      const sym = val.trim().toUpperCase() || 'MRG';
      appConfig.tokenSymbol = sym;
      applyGlobalConfig();
      renderUserTasks();
      renderAdminTasks();
      renderTransactions();
    }

    function autoUpdateAppName(val) {
      const name = val.trim() || 'MRG Miner';
      appConfig.appName = name;
      applyGlobalConfig();
    }
"""

text = text.replace("    // Transaction History Functions", tasks_and_token_js + "\n    // Transaction History Functions")

# Call renderUserTasks() and renderAdminTasks() on openAdminPanel and init
text = text.replace(
    "document.getElementById('adminViewport').classList.add('active');\n      renderAdminWithdrawals();",
    "document.getElementById('adminViewport').classList.add('active');\n      renderAdminWithdrawals();\n      renderAdminTasks();"
)

text = text.replace(
    "renderTransactions();\n      applyGlobalConfig();",
    "renderTransactions();\n      renderUserTasks();\n      renderAdminTasks();\n      applyGlobalConfig();"
)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Upgraded Tasks & Quests with dynamic engine and real-time auto token sync!")
