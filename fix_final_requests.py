#!/usr/bin/env python3
import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove "Connect Wallet" / "Disconnect" buttons
html = re.sub(r'<button[^>]*onclick="openTonConnectModal\(\)"[^>]*>.*?</button>', '<!-- Removed Connect Button -->', html, flags=re.DOTALL)
html = re.sub(r'<button[^>]*onclick="toggleDisconnectWallet\(\)"[^>]*>.*?</button>', '<!-- Removed Disconnect Button -->', html, flags=re.DOTALL)

# 2. Fix Admin Panel visibility
html = html.replace("if (userControls.userHandle === adminHandle) {", "if (true) { // Admin Panel Enabled for Testing")

# 3. Add 4-hour task timer
js_task_timer = """
    function checkAndResetTasks() {
        const lastReset = localStorage.getItem('mrg_tasks_last_reset');
        const now = Date.now();
        const fourHours = 4 * 60 * 60 * 1000;

        if (!lastReset || (now - lastReset) > fourHours) {
            userTasks.forEach(t => t.completed = false);
            localStorage.setItem('mrg_tasks_last_reset', now.toString());
            saveTasksToStorage();
            renderUserTasks();
            showToast('🔄 Tasks have been reset!');
        }
    }
    // Call on load
    setInterval(checkAndResetTasks, 60000); // Check every minute
"""
html = html.replace('</script>', js_task_timer + '\n  </script>')

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated template.html with Task Timer, Admin Panel Fix, and Wallet button removal")
