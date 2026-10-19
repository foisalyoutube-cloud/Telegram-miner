import re

with open('template.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add CSS for PIN modal and keypad before </style>
pin_css = """
    /* Admin PIN Verification Modal & Keypad */
    .pin-indicators-box {
      display: flex;
      justify-content: center;
      gap: 10px;
      margin-bottom: 14px;
    }
    .pin-digit-dot {
      width: 44px;
      height: 50px;
      border-radius: 12px;
      background: #0d1522;
      border: 1.5px solid #23344d;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      font-weight: 800;
      color: var(--accent-gold);
      transition: all 0.18s ease;
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.4);
    }
    .pin-digit-dot.filled {
      border-color: var(--accent-gold);
      background: rgba(244, 182, 56, 0.12);
      box-shadow: 0 0 12px rgba(244, 182, 56, 0.35);
    }
    .pin-digit-dot.active-focus {
      border-color: var(--accent-blue);
      box-shadow: 0 0 10px rgba(41, 151, 255, 0.45);
    }
    .pin-digit-dot.success {
      border-color: var(--accent-green) !important;
      background: rgba(0, 201, 128, 0.2) !important;
      color: var(--accent-green) !important;
      box-shadow: 0 0 16px rgba(0, 201, 128, 0.5) !important;
    }
    .pin-digit-dot.error {
      border-color: var(--danger-red) !important;
      background: rgba(255, 71, 87, 0.2) !important;
      color: var(--danger-red) !important;
      box-shadow: 0 0 16px rgba(255, 71, 87, 0.5) !important;
    }

    .pin-keypad {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin: 0 auto 16px auto;
      max-width: 320px;
    }
    .pin-key-btn {
      background: #182436;
      border: 1px solid #263852;
      border-radius: 14px;
      color: #ffffff;
      font-size: 20px;
      font-weight: 700;
      min-height: 52px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.12s ease;
      touch-action: manipulation;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }
    .pin-key-btn:active {
      transform: scale(0.92);
      background: #23344d;
    }

    @keyframes pinShake {
      0%, 100% { transform: translateX(0); }
      20%, 60% { transform: translateX(-8px); }
      40%, 80% { transform: translateX(8px); }
    }
    .shake-anim {
      animation: pinShake 0.4s ease;
    }
  </style>
"""

text = text.replace('  </style>', pin_css)

# 2. Update Admin Header to have Lock button
old_admin_header = """    <div class="admin-header-bar">
      <div class="admin-back-btn" onclick="closeAdminPanel()">
        <span>←</span>
        <span>Back to User App</span>
      </div>
      <div class="admin-badge-pill">🛡️ ADMIN CONSOLE</div>
    </div>"""

new_admin_header = """    <div class="admin-header-bar">
      <div class="admin-back-btn" onclick="closeAdminPanel()">
        <span>←</span>
        <span>Back to User App</span>
      </div>
      <div style="display: flex; gap: 8px; align-items: center;">
        <div class="admin-badge-pill">🛡️ ADMIN CONSOLE</div>
        <button onclick="lockAndCloseAdmin()" style="background: rgba(255, 71, 87, 0.18); border: 1px solid rgba(255, 71, 87, 0.4); color: #ff6b81; border-radius: 20px; padding: 6px 12px; font-size: 11px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 4px;">
          <span>🔒</span> Lock
        </button>
      </div>
    </div>"""

text = text.replace(old_admin_header, new_admin_header)

# 3. Add PIN Security Management Card in Tab 0 (Branding & Settings)
old_save_global_btn = """            <div style="display: flex; gap: 8px; margin-top: 6px;">
              <button class="admin-btn green" style="flex: 2; padding: 14px; font-size: 14px;" onclick="saveGlobalConfig()">
                💾 Save &amp; Apply All Changes
              </button>
              <button class="admin-btn" style="flex: 1; padding: 14px; background: #1c2b42; color: var(--text-gray);" onclick="resetGlobalConfig()">
                🔄 Reset
              </button>
            </div>
          </div>
        </div>
      </div>"""

pin_mgmt_card = """            <div style="display: flex; gap: 8px; margin-top: 6px;">
              <button class="admin-btn green" style="flex: 2; padding: 14px; font-size: 14px;" onclick="saveGlobalConfig()">
                💾 Save &amp; Apply All Changes
              </button>
              <button class="admin-btn" style="flex: 1; padding: 14px; background: #1c2b42; color: var(--text-gray);" onclick="resetGlobalConfig()">
                🔄 Reset
              </button>
            </div>
          </div>
        </div>

        <!-- ADMIN PIN SECURITY CARD -->
        <div class="admin-card" style="margin-top: 14px; border: 1px solid rgba(244, 182, 56, 0.35); background: linear-gradient(135deg, rgba(22, 32, 48, 0.95), rgba(30, 42, 62, 0.95));">
          <div class="admin-card-title">
            <span>🔐 Admin PIN Security</span>
            <span class="badge-chip verified" style="font-size: 11px; background: rgba(0, 201, 128, 0.15); color: #00c980;">Protected</span>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px;">
            The Admin Panel is protected with a 6-digit master PIN. The default master PIN code is <strong>115414</strong>.
          </p>
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; background: #0f1622; padding: 10px 14px; border-radius: 12px; border: 1px solid #23344d;">
              <div>
                <div style="font-size: 11px; color: var(--text-muted);">Current Active PIN</div>
                <div id="adminPinCurrentDisplay" style="font-size: 17px; font-weight: 800; color: var(--accent-gold); letter-spacing: 2px;">115414</div>
              </div>
              <button class="admin-btn" style="padding: 6px 12px; font-size: 11px; background: #1c2b42;" onclick="togglePinVisibility()">👁️ Show/Hide</button>
            </div>
            
            <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 8px;">
              <input type="text" class="modal-input" id="cfgNewAdminPin" maxlength="6" placeholder="New 6-digit PIN" style="margin-bottom: 0;">
              <button class="admin-btn green" style="padding: 10px;" onclick="saveNewAdminPin()">Update PIN</button>
            </div>

            <div style="display: flex; gap: 8px;">
              <button class="admin-btn" style="flex: 1; padding: 8px; font-size: 12px; background: #182335; color: var(--text-gray);" onclick="resetAdminPinDefault()">
                🔄 Reset to Default (115414)
              </button>
              <button class="admin-btn red" style="flex: 1; padding: 8px; font-size: 12px;" onclick="lockAndCloseAdmin()">
                🔒 Lock Admin Now
              </button>
            </div>
          </div>
        </div>
      </div>"""

text = text.replace(old_save_global_btn, pin_mgmt_card)

# 4. Insert Admin PIN Verification Modal before Edit Task Modal
pin_modal_html = """  <!-- Admin PIN Verification Modal -->
  <div class="modal-backdrop" id="adminPinModal">
    <div class="modal-sheet" style="text-align: center; max-width: 420px; border-radius: 28px 28px 0 0; background: #131c2b; border: 1px solid rgba(255,255,255,0.1);">
      <div style="width: 56px; height: 56px; border-radius: 50%; background: rgba(244, 182, 56, 0.15); border: 1px solid rgba(244, 182, 56, 0.4); display: flex; align-items: center; justify-content: center; font-size: 26px; margin: 0 auto 12px auto; box-shadow: 0 0 20px rgba(244, 182, 56, 0.2);">
        🔐
      </div>
      <div class="modal-title" style="margin-bottom: 4px;">Admin Security PIN</div>
      <div class="modal-desc" style="margin-bottom: 16px;">
        Please enter the 6-digit master PIN to access the Admin Control Panel.
      </div>

      <!-- 6 PIN Digits Indicators -->
      <div class="pin-indicators-box" id="pinIndicatorsBox">
        <div class="pin-digit-dot" id="pinDot0"></div>
        <div class="pin-digit-dot" id="pinDot1"></div>
        <div class="pin-digit-dot" id="pinDot2"></div>
        <div class="pin-digit-dot" id="pinDot3"></div>
        <div class="pin-digit-dot" id="pinDot4"></div>
        <div class="pin-digit-dot" id="pinDot5"></div>
      </div>

      <!-- Error / Status message -->
      <div id="pinErrorMsg" style="min-height: 20px; font-size: 12px; font-weight: 700; color: #ff4757; margin-bottom: 14px; opacity: 0; transition: opacity 0.2s;">
        ❌ Incorrect PIN! Try again.
      </div>

      <!-- Hidden Input for soft/hardware keyboard -->
      <input type="password" id="adminPinHiddenInput" maxlength="6" inputmode="numeric" pattern="[0-9]*" 
             style="position: absolute; opacity: 0; pointer-events: none; width: 1px; height: 1px;" 
             oninput="handlePinKeyInput(this.value)" autocomplete="off">

      <!-- Touch Numeric Keypad -->
      <div class="pin-keypad">
        <button type="button" class="pin-key-btn" onclick="pressPinKey('1')">1</button>
        <button type="button" class="pin-key-btn" onclick="pressPinKey('2')">2</button>
        <button type="button" class="pin-key-btn" onclick="pressPinKey('3')">3</button>
        <button type="button" class="pin-key-btn" onclick="pressPinKey('4')">4</button>
        <button type="button" class="pin-key-btn" onclick="pressPinKey('5')">5</button>
        <button type="button" class="pin-key-btn" onclick="pressPinKey('6')">6</button>
        <button type="button" class="pin-key-btn" onclick="pressPinKey('7')">7</button>
        <button type="button" class="pin-key-btn" onclick="pressPinKey('8')">8</button>
        <button type="button" class="pin-key-btn" onclick="pressPinKey('9')">9</button>
        <button type="button" class="pin-key-btn action-key" onclick="pressPinKey('del')" style="background: rgba(255, 71, 87, 0.15); color: #ff6b81; font-size: 18px;">⌫</button>
        <button type="button" class="pin-key-btn" onclick="pressPinKey('0')">0</button>
        <button type="button" class="pin-key-btn action-key" onclick="verifyAdminPin()" style="background: rgba(0, 201, 128, 0.2); color: #00c980; font-size: 16px; font-weight: 800;">↵</button>
      </div>

      <div style="display: flex; gap: 8px; justify-content: center; margin-top: 4px;">
        <button type="button" class="modal-btn-confirm" style="background: transparent; color: var(--text-muted); font-size: 14px; padding: 10px;" onclick="closeAdminPinModal()">Cancel</button>
      </div>
    </div>
  </div>

  <!-- Edit Task Modal -->"""

text = text.replace('  <!-- Edit Task Modal -->', pin_modal_html)

# 5. Add soundError function after soundSuccess
sound_error_code = """    function soundSuccess() {
      playTone(523.25, 'triangle', 0.1, 0.15);
      setTimeout(() => playTone(659.25, 'triangle', 0.15, 0.2), 100);
      setTimeout(() => playTone(783.99, 'triangle', 0.2, 0.25), 200);
    }
    function soundError() {
      playTone(280, 'sawtooth', 0.15, 0.2);
      setTimeout(() => playTone(220, 'sawtooth', 0.18, 0.25), 90);
    }"""

text = text.replace("""    function soundSuccess() {
      playTone(523.25, 'triangle', 0.1, 0.15);
      setTimeout(() => playTone(659.25, 'triangle', 0.15, 0.2), 100);
      setTimeout(() => playTone(783.99, 'triangle', 0.2, 0.25), 200);
    }""", sound_error_code)

# 6. Replace openAdminPanel / closeAdminPanel with PIN Protection functions
old_admin_open_js = """    // ==========================================
    // ADMIN PANEL JAVASCRIPT CONTROLS
    // ==========================================
    function openAdminPanel() {
      soundTap();
      document.getElementById('adminViewport').classList.add('active');
      renderAdminWithdrawals();
      renderAdminTasks();
    }

    function closeAdminPanel() {
      soundTap();
      document.getElementById('adminViewport').classList.remove('active');
    }

    function openAdminMenu() {
      soundTap();
      openAdminPanel();
    }"""

new_admin_open_js = """    // ==========================================
    // ADMIN PANEL JAVASCRIPT CONTROLS WITH PIN 115414
    // ==========================================
    const DEFAULT_ADMIN_PIN = "115414";
    let enteredPinCode = "";
    let isPinVisible = false;

    function getAdminPin() {
      try {
        const stored = localStorage.getItem('mrg_admin_pin');
        if (stored && /^\d{6}$/.test(stored)) return stored;
      } catch (e) {}
      return DEFAULT_ADMIN_PIN;
    }

    function setAdminPin(newPin) {
      try {
        localStorage.setItem('mrg_admin_pin', newPin);
      } catch (e) {}
    }

    function openAdminPanel() {
      soundTap();
      showAdminPinModal();
    }

    function openAdminMenu() {
      soundTap();
      showAdminPinModal();
    }

    function showAdminPinModal() {
      enteredPinCode = "";
      updatePinDisplay();
      const errorMsg = document.getElementById('pinErrorMsg');
      if (errorMsg) {
        errorMsg.style.opacity = '0';
        errorMsg.innerText = '';
      }
      const modal = document.getElementById('adminPinModal');
      if (modal) modal.classList.add('show');

      // Focus hidden input for physical keyboard entry
      setTimeout(() => {
        const hiddenInp = document.getElementById('adminPinHiddenInput');
        if (hiddenInp) {
          hiddenInp.value = '';
          hiddenInp.focus();
        }
      }, 200);
    }

    function closeAdminPinModal() {
      soundTap();
      enteredPinCode = "";
      updatePinDisplay();
      const modal = document.getElementById('adminPinModal');
      if (modal) modal.classList.remove('show');
    }

    function pressPinKey(digit) {
      soundTap();
      const errorMsg = document.getElementById('pinErrorMsg');
      if (errorMsg) errorMsg.style.opacity = '0';

      if (digit === 'del') {
        if (enteredPinCode.length > 0) {
          enteredPinCode = enteredPinCode.slice(0, -1);
        }
      } else if (digit === 'clear') {
        enteredPinCode = '';
      } else {
        if (enteredPinCode.length < 6) {
          enteredPinCode += digit;
        }
      }

      updatePinDisplay();

      // Automatically verify when 6 digits are reached
      if (enteredPinCode.length === 6) {
        setTimeout(verifyAdminPin, 120);
      }
    }

    function handlePinKeyInput(val) {
      const numeric = val.replace(/\D/g, '').slice(0, 6);
      enteredPinCode = numeric;
      updatePinDisplay();
      if (enteredPinCode.length === 6) {
        setTimeout(verifyAdminPin, 120);
      }
    }

    function updatePinDisplay() {
      for (let i = 0; i < 6; i++) {
        const dot = document.getElementById('pinDot' + i);
        if (!dot) continue;
        dot.className = 'pin-digit-dot';
        if (i < enteredPinCode.length) {
          dot.classList.add('filled');
          dot.innerText = '●';
        } else if (i === enteredPinCode.length) {
          dot.classList.add('active-focus');
          dot.innerText = '';
        } else {
          dot.innerText = '';
        }
      }
    }

    function verifyAdminPin() {
      const correctPin = getAdminPin();
      const box = document.getElementById('pinIndicatorsBox');
      const errorMsg = document.getElementById('pinErrorMsg');

      if (enteredPinCode === correctPin) {
        // SUCCESS: PIN 115414 GRANTED
        soundSuccess();
        for (let i = 0; i < 6; i++) {
          const dot = document.getElementById('pinDot' + i);
          if (dot) {
            dot.className = 'pin-digit-dot filled success';
            dot.innerText = '✓';
          }
        }
        if (errorMsg) {
          errorMsg.style.color = '#00c980';
          errorMsg.innerText = '✓ PIN Verified! Access Granted.';
          errorMsg.style.opacity = '1';
        }

        setTimeout(() => {
          closeAdminPinModal();
          document.getElementById('adminViewport').classList.add('active');
          renderAdminWithdrawals();
          renderAdminTasks();
          updateAdminPinSectionDisplay();
          showToast('🛡️ Welcome Admin! Authorized access granted.');
        }, 350);
      } else {
        // INCORRECT PIN
        soundError();
        for (let i = 0; i < 6; i++) {
          const dot = document.getElementById('pinDot' + i);
          if (dot) dot.className = 'pin-digit-dot error';
        }
        if (box) {
          box.classList.remove('shake-anim');
          void box.offsetWidth;
          box.classList.add('shake-anim');
        }
        if (errorMsg) {
          errorMsg.style.color = '#ff4757';
          errorMsg.innerText = '❌ Incorrect PIN! Please enter master PIN (115414)';
          errorMsg.style.opacity = '1';
        }

        setTimeout(() => {
          enteredPinCode = '';
          updatePinDisplay();
          const hiddenInp = document.getElementById('adminPinHiddenInput');
          if (hiddenInp) hiddenInp.value = '';
        }, 700);
      }
    }

    function closeAdminPanel() {
      soundTap();
      document.getElementById('adminViewport').classList.remove('active');
    }

    function lockAndCloseAdmin() {
      soundTap();
      document.getElementById('adminViewport').classList.remove('active');
      enteredPinCode = '';
      showToast('🔒 Admin Panel locked safely.');
    }

    function updateAdminPinSectionDisplay() {
      const displayEl = document.getElementById('adminPinCurrentDisplay');
      if (displayEl) {
        const pin = getAdminPin();
        displayEl.innerText = isPinVisible ? pin : '••••••';
      }
    }

    function togglePinVisibility() {
      soundTap();
      isPinVisible = !isPinVisible;
      updateAdminPinSectionDisplay();
    }

    function saveNewAdminPin() {
      const input = document.getElementById('cfgNewAdminPin');
      const val = (input.value || '').trim();
      if (!/^\\d{6}$/.test(val)) {
        showToast('⚠️ PIN must be exactly 6 digits (0-9)!');
        return;
      }
      soundSuccess();
      setAdminPin(val);
      input.value = '';
      updateAdminPinSectionDisplay();
      showToast(`✅ Admin PIN updated to: ${val}`);
    }

    function resetAdminPinDefault() {
      soundTap();
      setAdminPin(DEFAULT_ADMIN_PIN);
      updateAdminPinSectionDisplay();
      showToast('🔄 PIN reset to master default: 115414');
    }"""

text = text.replace(old_admin_open_js, new_admin_open_js)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Template successfully updated with PIN 115414 protection!")
