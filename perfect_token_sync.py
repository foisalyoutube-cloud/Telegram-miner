with open('template.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update applyGlobalConfig to be comprehensive
old_cfg_func = """    function applyGlobalConfig() {
      // 1. App Title
      document.title = appConfig.appName + ' Bot';
      const pageTitleEl = document.getElementById('pageTitle');
      if (pageTitleEl) pageTitleEl.innerText = appConfig.appName + ' Bot';

      // 2. Token Symbol across all elements
      document.querySelectorAll('.token-sym').forEach(el => {
        el.innerText = appConfig.tokenSymbol;
      });"""

new_cfg_func = """    function applyGlobalConfig() {
      const sym = appConfig.tokenSymbol || 'MRG';

      // 1. App Title
      document.title = appConfig.appName + ' Bot';
      const pageTitleEl = document.getElementById('pageTitle');
      if (pageTitleEl) pageTitleEl.innerText = appConfig.appName + ' Bot';

      // 2. Token Symbol across all elements
      document.querySelectorAll('.token-sym').forEach(el => {
        el.innerText = sym;
      });

      // 2b. Subtitles and text descriptions
      const tasksSubtitle = document.querySelector('#tab-tasks .hero-subtitle');
      if (tasksSubtitle) {
        tasksSubtitle.innerText = `Complete tasks and check in every day to earn free ${sym}.`;
      }
      const minersSubtitle = document.querySelector('#tab-miners .hero-subtitle');
      if (minersSubtitle) {
        minersSubtitle.innerText = `Hold more ${sym} to unlock faster miners. Nothing is spent — your level follows what you hold.`;
      }
      const withdrawInput = document.getElementById('withdrawAmount');
      if (withdrawInput) {
        withdrawInput.placeholder = `Amount (${sym})`;
      }"""

text = text.replace(old_cfg_func, new_cfg_func)

# Also ensure autoUpdateTokenName updates localStorage right away
old_auto_token = """    function autoUpdateTokenName(val) {
      const sym = val.trim().toUpperCase() || 'MRG';
      appConfig.tokenSymbol = sym;
      applyGlobalConfig();
      renderUserTasks();
      renderAdminTasks();
      renderTransactions();
    }"""

new_auto_token = """    function autoUpdateTokenName(val) {
      const sym = val.trim().toUpperCase() || 'MRG';
      appConfig.tokenSymbol = sym;
      try {
        localStorage.setItem('mrg_app_config', JSON.stringify(appConfig));
      } catch (e) {}
      applyGlobalConfig();
      renderUserTasks();
      renderAdminTasks();
      renderTransactions();
    }"""

text = text.replace(old_auto_token, new_auto_token)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied perfect token sync patch!")
