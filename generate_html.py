import json

with open('app/src/main/assets/coin.b64') as f: coin_b64 = f.read().strip()
with open('app/src/main/assets/trophy.b64') as f: trophy_b64 = f.read().strip()
with open('app/src/main/assets/purse.b64') as f: purse_b64 = f.read().strip()
with open('app/src/main/assets/heart.b64') as f: heart_b64 = f.read().strip()
with open('app/src/main/assets/flame.b64') as f: flame_b64 = f.read().strip()

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>MRG Miner Bot</title>
  <style>
    :root {{
      --bg-dark: #0e141f;
      --card-bg: #162030;
      --card-bg-light: #1b273b;
      --card-border: #223048;
      --accent-blue: #2997ff;
      --accent-blue-hover: #1e87eb;
      --accent-gold: #f4b638;
      --accent-green: #00c980;
      --text-white: #ffffff;
      --text-gray: #8899ac;
      --text-muted: #5e7288;
      --danger-red: #ff4757;
      --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
      user-select: none;
    }}

    body {{
      background-color: var(--bg-dark);
      color: var(--text-white);
      font-family: var(--font-family);
      overflow-x: hidden;
      overflow-y: auto;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      position: relative;
    }}

    /* Telegram Top Bar */
    .tg-topbar {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(14, 20, 31, 0.95);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }}

    .tg-close-btn {{
      display: flex;
      align-items: center;
      gap: 6px;
      color: #ffffff;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      opacity: 0.9;
    }}
    .tg-close-btn:active {{ opacity: 0.6; }}

    .tg-top-pills {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .user-avatar-small {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 1.5px solid var(--accent-blue);
      object-fit: cover;
      background: #253347;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: bold;
      color: #fff;
    }}

    .balance-capsule {{
      display: flex;
      align-items: center;
      background: #192334;
      border: 1px solid #23344d;
      border-radius: 20px;
      padding: 4px 10px 4px 6px;
      gap: 6px;
      cursor: pointer;
    }}
    .balance-capsule img.coin-icon {{
      width: 20px;
      height: 20px;
      border-radius: 50%;
    }}
    .balance-capsule .val {{
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
    }}
    .balance-capsule .currency {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-gray);
      margin-left: 2px;
    }}
    .balance-capsule .plus-btn {{
      background: var(--accent-blue);
      color: white;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: bold;
      margin-left: 2px;
    }}

    .level-capsule {{
      display: flex;
      align-items: center;
      background: #192334;
      border: 1px solid #23344d;
      border-radius: 20px;
      padding: 4px 12px;
      gap: 5px;
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
      cursor: pointer;
    }}
    .level-capsule .bolt {{
      color: var(--accent-gold);
      font-size: 13px;
    }}

    .tg-right-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
      color: var(--text-gray);
      cursor: pointer;
    }}

    /* Main Container */
    .app-viewport {{
      flex: 1;
      padding: 14px 16px 85px 16px;
      max-width: 480px;
      margin: 0 auto;
      width: 100%;
    }}

    .tab-content {{
      display: none;
      animation: fadeIn 0.25s ease forwards;
    }}
    .tab-content.active {{
      display: block;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Shared Card Styles */
    .hero-card {{
      background: linear-gradient(180deg, #162234 0%, #121b29 100%);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 22px;
      padding: 22px 18px;
      text-align: center;
      position: relative;
      overflow: hidden;
      margin-bottom: 20px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }}

    .hero-title {{
      font-size: 23px;
      font-weight: 800;
      letter-spacing: -0.3px;
      margin-bottom: 6px;
      color: #ffffff;
    }}

    .hero-subtitle {{
      font-size: 13px;
      color: #92a4b8;
      line-height: 1.45;
      max-width: 310px;
      margin: 0 auto;
    }}

    .section-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin: 20px 4px 12px 4px;
    }}
    .section-title {{
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.8px;
      color: var(--text-muted);
      text-transform: uppercase;
    }}
    .section-badge {{
      font-size: 12px;
      font-weight: 600;
      color: var(--text-gray);
    }}

    .content-box {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 16px;
      margin-bottom: 12px;
    }}

    /* ====================================================
       TAB 1: MINE (Cloud Mining)
    ==================================================== */
    .mine-header-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
    }}
    .mine-level-tag {{
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 600;
    }}
    .mine-title {{
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
    }}
    .mine-status-pill {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 201, 128, 0.12);
      border: 1px solid rgba(0, 201, 128, 0.3);
      color: var(--accent-green);
      font-size: 13px;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 20px;
    }}
    .mine-status-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--accent-green);
      animation: pulse 1.8s infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); opacity: 1; }}
      50% {{ transform: scale(1.4); opacity: 0.6; }}
    }}

    /* Concentric Rings Mascot */
    .mining-coin-stage {{
      position: relative;
      width: 250px;
      height: 250px;
      margin: 15px auto 20px auto;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .outer-glow-ring {{
      position: absolute;
      width: 240px;
      height: 240px;
      border-radius: 50%;
      border: 2px solid rgba(41, 151, 255, 0.2);
      box-shadow: 0 0 35px rgba(41, 151, 255, 0.25);
    }}

    .orbit-ring {{
      position: absolute;
      width: 220px;
      height: 220px;
      border-radius: 50%;
      border: 3px solid transparent;
      border-top-color: var(--accent-blue);
      border-right-color: rgba(41, 151, 255, 0.3);
      animation: rotateOrbit 6s linear infinite;
    }}

    @keyframes rotateOrbit {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}

    .inner-blue-rim {{
      position: absolute;
      width: 196px;
      height: 196px;
      border-radius: 50%;
      border: 4px solid var(--accent-blue);
      box-shadow: inset 0 0 20px rgba(41, 151, 255, 0.4), 0 0 15px rgba(41, 151, 255, 0.4);
    }}

    .mascot-coin {{
      width: 176px;
      height: 176px;
      border-radius: 50%;
      object-fit: cover;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6);
      cursor: pointer;
      transition: transform 0.12s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      z-index: 5;
    }}
    .mascot-coin:active {{
      transform: scale(0.93);
    }}

    .tap-particle {{
      position: absolute;
      pointer-events: none;
      font-weight: 800;
      color: var(--accent-gold);
      font-size: 18px;
      animation: floatUp 0.8s cubic-bezier(0.215, 0.61, 0.355, 1) forwards;
      z-index: 20;
      text-shadow: 0 0 8px rgba(244, 182, 56, 0.7);
    }}
    @keyframes floatUp {{
      0% {{ opacity: 1; transform: translate(-50%, 0) scale(0.8); }}
      100% {{ opacity: 0; transform: translate(-50%, -65px) scale(1.3); }}
    }}

    .unclaimed-label {{
      font-size: 13px;
      color: var(--text-gray);
      margin-bottom: 4px;
    }}
    .unclaimed-amount {{
      font-size: 34px;
      font-weight: 900;
      letter-spacing: -0.5px;
      color: #ffffff;
      font-variant-numeric: tabular-nums;
    }}
    .unclaimed-amount span.curr {{
      font-size: 18px;
      font-weight: 700;
      color: var(--text-gray);
      margin-left: 4px;
    }}
    .unclaimed-subrate {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 3px;
      margin-bottom: 20px;
    }}

    .btn-claim {{
      width: 100%;
      background: linear-gradient(180deg, #329fff 0%, #1781e6 100%);
      color: #ffffff;
      border: none;
      border-radius: 28px;
      padding: 16px 20px;
      font-size: 17px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 8px 24px rgba(41, 151, 255, 0.4);
      transition: all 0.15s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}
    .btn-claim:active {{
      transform: scale(0.98);
      box-shadow: 0 4px 12px rgba(41, 151, 255, 0.3);
    }}
    .btn-claim.disabled {{
      background: #253347;
      color: #6d8199;
      box-shadow: none;
      cursor: not-allowed;
    }}

    .miner-stat-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }}
    .miner-stat-row:last-child {{
      border-bottom: none;
      padding-bottom: 4px;
    }}
    .miner-stat-left {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 15px;
      font-weight: 600;
      color: #ffffff;
    }}
    .miner-icon-box {{
      width: 36px;
      height: 36px;
      border-radius: 10px;
      background: #1e2c40;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--accent-blue);
      font-size: 18px;
    }}
    .miner-stat-val {{
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
    }}

    /* ====================================================
       TAB 2: TASKS (Earn Rewards)
    ==================================================== */
    .trophy-hero-img {{
      width: 100px;
      height: 100px;
      margin: 0 auto 12px auto;
      object-fit: contain;
      filter: drop-shadow(0 8px 16px rgba(244, 182, 56, 0.3));
    }}

    /* 7-Day Streak Row */
    .streak-grid {{
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 6px;
      margin-bottom: 16px;
    }}
    .streak-day-card {{
      background: #182232;
      border: 1px solid #233146;
      border-radius: 12px;
      padding: 8px 4px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
    }}
    .streak-day-card.completed {{
      background: rgba(0, 201, 128, 0.1);
      border-color: rgba(0, 201, 128, 0.4);
    }}
    .streak-day-card.today {{
      border-color: var(--accent-blue);
      box-shadow: 0 0 10px rgba(41, 151, 255, 0.3);
    }}
    .streak-day-label {{
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
    }}
    .streak-day-card.completed .streak-day-label {{
      color: var(--accent-green);
    }}
    .streak-icon-circle {{
      width: 24px;
      height: 24px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: bold;
    }}
    .streak-day-card.completed .streak-icon-circle {{
      background: var(--accent-green);
      color: white;
    }}
    .streak-day-card.pending .streak-icon-circle {{
      background: rgba(244, 182, 56, 0.15);
      color: var(--accent-gold);
    }}
    .streak-reward-text {{
      font-size: 11px;
      font-weight: 700;
      color: var(--text-gray);
    }}
    .streak-day-card.completed .streak-reward-text {{
      color: var(--accent-green);
    }}

    .btn-streak-checkin {{
      width: 100%;
      background: #253347;
      color: #8da2ba;
      border: none;
      border-radius: 14px;
      padding: 13px;
      font-size: 15px;
      font-weight: 700;
      cursor: not-allowed;
      margin-bottom: 10px;
    }}
    .btn-streak-checkin.active-claim {{
      background: var(--accent-blue);
      color: white;
      cursor: pointer;
      box-shadow: 0 6px 18px rgba(41, 151, 255, 0.3);
    }}

    .streak-footer-note {{
      font-size: 12px;
      color: var(--text-muted);
      text-align: center;
    }}

    /* Task Items */
    .task-item {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 14px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
      cursor: pointer;
      transition: background 0.15s ease;
    }}
    .task-item:active {{
      background: var(--card-bg-light);
    }}
    .task-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .task-logo {{
      width: 42px;
      height: 42px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
    }}
    .task-logo.tg {{ background: #26a5e4; color: white; }}
    .task-logo.tw {{ background: #000000; color: white; }}
    .task-logo.yt {{ background: #ff0000; color: white; }}
    .task-logo.boost {{ background: #a855f7; color: white; }}

    .task-info-title {{
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 3px;
    }}
    .task-info-reward {{
      font-size: 13px;
      color: var(--text-gray);
    }}
    .task-info-reward span.gold {{
      color: var(--accent-gold);
      font-weight: 700;
    }}

    .task-timer-badge {{
      display: flex;
      align-items: center;
      gap: 5px;
      background: #1b2637;
      border: 1px solid #28374d;
      color: var(--text-gray);
      font-size: 12px;
      font-weight: 600;
      padding: 6px 10px;
      border-radius: 20px;
    }}
    .task-claim-btn {{
      background: var(--accent-blue);
      color: white;
      font-size: 13px;
      font-weight: 700;
      padding: 7px 14px;
      border-radius: 18px;
      border: none;
      cursor: pointer;
    }}

    /* ====================================================
       TAB 3: MINERS (Miners Store)
    ==================================================== */
    .flame-hero-img {{
      width: 90px;
      height: 90px;
      margin: 0 auto 10px auto;
      object-fit: contain;
      filter: drop-shadow(0 6px 20px rgba(244, 182, 56, 0.4));
    }}

    .stats-trio {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin: 18px 0;
    }}
    .stat-trio-card {{
      background: #172233;
      border: 1px solid #23334a;
      border-radius: 14px;
      padding: 12px 6px;
      text-align: center;
    }}
    .stat-trio-val {{
      font-size: 22px;
      font-weight: 900;
      color: #ffffff;
      margin-bottom: 2px;
    }}
    .stat-trio-val.green {{
      color: var(--accent-green);
    }}
    .stat-trio-label {{
      font-size: 11px;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .level-progress-bar-wrap {{
      margin-top: 14px;
      text-align: left;
    }}
    .level-progress-labels {{
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      font-weight: 700;
      margin-bottom: 6px;
    }}
    .level-progress-labels span.next {{
      color: #ffffff;
    }}
    .level-progress-labels span.remain {{
      color: var(--text-gray);
      font-weight: 500;
    }}
    .progress-track {{
      width: 100%;
      height: 7px;
      background: #1e2b3e;
      border-radius: 10px;
      overflow: hidden;
    }}
    .progress-fill {{
      height: 100%;
      width: 76%;
      background: linear-gradient(90deg, #268aff, #3ad4ff);
      border-radius: 10px;
    }}

    .action-nav-item {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 15px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
      cursor: pointer;
    }}
    .action-nav-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .action-nav-icon {{
      width: 38px;
      height: 38px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
    }}
    .action-nav-icon.blue {{ background: #1a314d; color: #2997ff; }}
    .action-nav-icon.gold {{ background: #3d3319; color: #f4b638; }}
    .action-nav-icon.green {{ background: #17382c; color: #00c980; }}

    .action-nav-text-title {{
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
    }}
    .action-nav-text-sub {{
      font-size: 12px;
      color: var(--text-gray);
      margin-top: 2px;
    }}
    .action-nav-arrow {{
      color: var(--text-muted);
      font-size: 16px;
    }}

    /* ====================================================
       TAB 4: FRIENDS (Squad Mining & Profile)
    ==================================================== */
    .user-profile-banner {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 18px 16px;
      margin-bottom: 14px;
    }}
    .user-profile-row {{
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 14px;
    }}
    .user-profile-pic-box {{
      position: relative;
      width: 62px;
      height: 62px;
    }}
    .user-profile-pic {{
      width: 62px;
      height: 62px;
      border-radius: 50%;
      object-fit: cover;
      background: #23344d;
      border: 2px solid var(--accent-blue);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      font-weight: bold;
      color: white;
    }}
    .tg-badge-overlay {{
      position: absolute;
      bottom: -2px;
      right: -2px;
      background: #26a5e4;
      color: white;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      border: 2px solid var(--card-bg);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
    }}

    .user-profile-info {{
      flex: 1;
      overflow: hidden;
    }}
    .user-profile-name {{
      font-size: 17px;
      font-weight: 800;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .user-profile-handle {{
      font-size: 13px;
      color: var(--text-gray);
      margin-top: 2px;
      margin-bottom: 6px;
    }}
    .badge-chips-row {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }}
    .badge-chip {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 12px;
    }}
    .badge-chip.nft {{
      background: #1e2c3e;
      color: var(--text-gray);
      border: 1px solid #283a52;
    }}
    .badge-chip.verified {{
      background: rgba(41, 151, 255, 0.15);
      color: var(--accent-blue);
      border: 1px solid rgba(41, 151, 255, 0.3);
    }}

    .lang-selector-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #172233;
      border: 1px solid #23334a;
      border-radius: 14px;
      padding: 10px 14px;
      cursor: pointer;
    }}
    .lang-selector-left {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
    }}
    .lang-globe-icon {{
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #ff4757;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 14px;
    }}
    .lang-selector-right {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-gray);
    }}

    .heart-hero-img {{
      width: 90px;
      height: 90px;
      margin: 0 auto 10px auto;
      object-fit: contain;
      filter: drop-shadow(0 6px 18px rgba(255, 71, 87, 0.35));
    }}

    .invite-action-buttons {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-top: 18px;
      margin-bottom: 14px;
    }}
    .btn-copy-ref {{
      background: #1d2a3d;
      color: #ffffff;
      border: 1px solid #2a3c57;
      border-radius: 14px;
      padding: 12px 14px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .btn-share-ref {{
      background: var(--accent-blue);
      color: #ffffff;
      border: none;
      border-radius: 14px;
      padding: 12px 14px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      box-shadow: 0 4px 14px rgba(41, 151, 255, 0.35);
    }}
    .ref-link-display {{
      font-size: 12px;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-top: 4px;
    }}

    /* ====================================================
       TAB 5: WALLET (In-App & TON/GRAM)
    ==================================================== */
    .purse-hero-img {{
      width: 95px;
      height: 95px;
      margin: 0 auto 10px auto;
      object-fit: contain;
      filter: drop-shadow(0 8px 20px rgba(235, 47, 150, 0.35));
    }}

    .wallet-action-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-top: 18px;
    }}
    .btn-withdraw {{
      background: linear-gradient(180deg, #329fff 0%, #1781e6 100%);
      color: #ffffff;
      border: none;
      border-radius: 24px;
      padding: 14px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .btn-buy-mrg {{
      background: #172435;
      color: #63b3ff;
      border: 1px solid #233852;
      border-radius: 24px;
      padding: 14px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}

    .wallet-info-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 13px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }}
    .wallet-info-row:last-child {{
      border-bottom: none;
      padding-bottom: 2px;
    }}
    .wallet-info-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .wallet-icon-box {{
      width: 36px;
      height: 36px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 17px;
    }}
    .wallet-icon-box.blue {{ background: #192c45; color: #2997ff; }}
    .wallet-icon-box.purple {{ background: #2f2147; color: #a855f7; }}
    .wallet-icon-box.red {{ background: #3d1c23; color: #ff4757; }}
    .wallet-icon-box.green {{ background: #163628; color: #00c980; }}

    .wallet-info-title {{
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
    }}
    .wallet-info-sub {{
      font-size: 12px;
      color: var(--text-gray);
      margin-top: 1px;
    }}
    .btn-copy-address {{
      background: #1e2c3e;
      border: 1px solid #2a3c54;
      color: #ffffff;
      padding: 6px 10px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
    }}


    /* Transaction History Styles */
    .history-filter-row {{
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: none;
    }}
    .history-filter-row::-webkit-scrollbar {{ display: none; }}
    .history-filter-chip {{
      background: #172233;
      border: 1px solid #23334a;
      color: var(--text-gray);
      padding: 6px 14px;
      border-radius: 16px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }}
    .history-filter-chip.active {{
      background: var(--accent-blue);
      color: #ffffff;
      border-color: var(--accent-blue);
      box-shadow: 0 2px 8px rgba(41, 151, 255, 0.3);
    }}

    .tx-item-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 13px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
      cursor: pointer;
      transition: background 0.15s ease, transform 0.1s ease;
    }}
    .tx-item-card:active {{
      background: var(--card-bg-light);
      transform: scale(0.99);
    }}
    .tx-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .tx-icon-box {{
      width: 40px;
      height: 40px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
    }}
    .tx-icon-box.claim {{ background: rgba(244, 182, 56, 0.15); color: var(--accent-gold); }}
    .tx-icon-box.withdraw {{ background: rgba(255, 71, 87, 0.15); color: var(--danger-red); }}
    .tx-icon-box.deposit {{ background: rgba(0, 201, 128, 0.15); color: var(--accent-green); }}
    .tx-icon-box.reward {{ background: rgba(168, 85, 247, 0.15); color: #a855f7; }}

    .tx-title {{
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 2px;
    }}
    .tx-meta {{
      font-size: 11px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .tx-badge-status {{
      font-size: 10px;
      padding: 1px 6px;
      border-radius: 8px;
      font-weight: 600;
    }}
    .tx-badge-status.completed {{
      background: rgba(0, 201, 128, 0.12);
      color: var(--accent-green);
    }}
    .tx-badge-status.pending {{
      background: rgba(244, 182, 56, 0.12);
      color: var(--accent-gold);
    }}

    .tx-right {{
      text-align: right;
    }}
    .tx-amount {{
      font-size: 14px;
      font-weight: 800;
      font-variant-numeric: tabular-nums;
    }}
    .tx-amount.positive {{
      color: var(--accent-green);
    }}
    .tx-amount.negative {{
      color: #ffffff;
    }}
    .tx-sub {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 1px;
    }}
    .empty-history-box {{
      text-align: center;
      padding: 28px 16px;
      color: var(--text-muted);
      font-size: 13px;
      background: var(--card-bg);
      border: 1px dashed var(--card-border);
      border-radius: 16px;
    }}

    /* Bottom Navigation Bar */
    .bottom-nav {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(14, 20, 31, 0.96);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      display: flex;
      align-items: center;
      justify-content: space-around;
      padding: 8px 10px 14px 10px;
      z-index: 100;
      max-width: 480px;
      margin: 0 auto;
    }}

    .nav-tab {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      cursor: pointer;
      color: var(--text-muted);
      transition: all 0.15s ease;
      min-width: 56px;
    }}
    .nav-tab.active {{
      color: var(--accent-blue);
    }}
    .nav-tab-icon-wrap {{
      width: 44px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 16px;
      transition: all 0.15s ease;
      position: relative;
    }}
    .nav-tab.active .nav-tab-icon-wrap {{
      background: rgba(41, 151, 255, 0.18);
    }}
    .nav-tab svg {{
      width: 22px;
      height: 22px;
      fill: currentColor;
    }}
    .nav-tab-label {{
      font-size: 11px;
      font-weight: 600;
    }}

    /* Toast Notification */
    .toast-msg {{
      position: fixed;
      top: 65px;
      left: 50%;
      transform: translateX(-50%) translateY(-20px);
      background: rgba(22, 32, 48, 0.95);
      border: 1px solid rgba(41, 151, 255, 0.4);
      color: #ffffff;
      padding: 10px 20px;
      border-radius: 24px;
      font-size: 13px;
      font-weight: 700;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      opacity: 0;
      pointer-events: none;
      transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toast-msg.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}

    /* Modal / Bottom Sheet */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      z-index: 500;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease;
      display: flex;
      align-items: flex-end;
      justify-content: center;
    }}
    .modal-backdrop.show {{
      opacity: 1;
      pointer-events: auto;
    }}
    .modal-sheet {{
      background: #162030;
      border-top-left-radius: 24px;
      border-top-right-radius: 24px;
      width: 100%;
      max-width: 480px;
      padding: 24px 20px 32px 20px;
      border: 1px solid rgba(255, 255, 255, 0.08);
      transform: translateY(100%);
      transition: transform 0.25s cubic-bezier(0.2, 0.9, 0.3, 1);
    }}
    .modal-backdrop.show .modal-sheet {{
      transform: translateY(0);
    }}
    .modal-title {{
      font-size: 19px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 8px;
      text-align: center;
    }}
    .modal-desc {{
      font-size: 13px;
      color: var(--text-gray);
      text-align: center;
      margin-bottom: 20px;
      line-height: 1.4;
    }}
    .modal-input {{
      width: 100%;
      background: #0f1622;
      border: 1px solid #23344d;
      border-radius: 14px;
      padding: 14px;
      color: #ffffff;
      font-size: 15px;
      outline: none;
      margin-bottom: 12px;
    }}
    .modal-input:focus {{
      border-color: var(--accent-blue);
    }}
    .modal-btn-confirm {{
      width: 100%;
      background: var(--accent-blue);
      color: #ffffff;
      border: none;
      border-radius: 14px;
      padding: 14px;
      font-size: 16px;
      font-weight: 700;
      cursor: pointer;
    }}
  </style>
</head>
<body>

  <!-- Top Telegram Bar -->
  <div class="tg-topbar">
    <div class="tg-close-btn" onclick="handleTgClose()">
      <span>✕</span>
      <span>Close</span>
    </div>

    <div class="tg-top-pills">
      <div class="user-avatar-small" title="GW Foisal">GW</div>
      <div class="balance-capsule" onclick="openBuyDEXModal()">
        <img class="coin-icon" src="data:image/jpeg;base64,{coin_b64}" alt="Coin">
        <span class="val" id="topBalance">2.1K</span>
        <span class="currency">MRG</span>
        <div class="plus-btn">+</div>
      </div>
      <div class="level-capsule" onclick="switchTab('miners')">
        <span class="bolt">⚡</span>
        <span>Level 83</span>
      </div>
    </div>

    <div class="tg-right-actions">
      <span onclick="toggleLanguage()">⌵</span>
      <span onclick="showToast('MRG Miner Bot v2.4 (TON Network)')">⋮</span>
    </div>
  </div>

  <!-- Viewport -->
  <div class="app-viewport">

    <!-- TAB 1: MINE -->
    <div class="tab-content active" id="tab-mine">
      <div class="hero-card">
        <div class="mine-header-row">
          <div>
            <div class="mine-level-tag">Level 83 Miner</div>
            <div class="mine-title">Cloud Mining</div>
          </div>
          <div class="mine-status-pill">
            <span class="mine-status-dot"></span>
            <span id="miningTimer">23:59:57</span>
          </div>
        </div>

        <!-- Concentric Circular Stage -->
        <div class="mining-coin-stage" id="coinStage">
          <div class="outer-glow-ring"></div>
          <div class="orbit-ring"></div>
          <div class="inner-blue-rim"></div>
          <img class="mascot-coin" id="mascotCoin" src="data:image/jpeg;base64,{coin_b64}" alt="Cat Miner">
        </div>

        <div class="unclaimed-label">Unclaimed reward</div>
        <div class="unclaimed-amount">
          <span id="unclaimedVal">0.002938</span>
          <span class="curr">MRG</span>
        </div>
        <div class="unclaimed-subrate">≈ $0.0000 · 3.19 TH/s</div>

        <button class="btn-claim" id="btnClaim" onclick="claimMiningReward()">
          <span>Claim Reward · <span id="btnClaimVal">0.00</span> MRG</span>
        </button>
      </div>

      <div class="section-header">
        <span class="section-title">MINER</span>
      </div>

      <div class="content-box">
        <div class="miner-stat-row">
          <div class="miner-stat-left">
            <div class="miner-icon-box">⏱</div>
            <span>Mining Speed</span>
          </div>
          <div class="miner-stat-val">3.19 TH/s</div>
        </div>
        <div class="miner-stat-row">
          <div class="miner-stat-left">
            <div class="miner-icon-box" style="color: var(--accent-gold);">⚡</div>
            <span>Current Miner</span>
          </div>
          <div class="miner-stat-val">Level 83</div>
        </div>
      </div>
    </div>

    <!-- TAB 2: TASKS -->
    <div class="tab-content" id="tab-tasks">
      <div class="hero-card">
        <img class="trophy-hero-img" src="data:image/jpeg;base64,{trophy_b64}" alt="Trophy">
        <h2 class="hero-title">Earn Rewards</h2>
        <p class="hero-subtitle">Complete tasks and check in every day to earn free MRG.</p>
      </div>

      <div class="section-header">
        <span class="section-title">DAILY CHECK-IN</span>
        <span class="section-badge" id="streakBadge">Day 2 of 7</span>
      </div>

      <div class="content-box">
        <div class="streak-grid">
          <div class="streak-day-card completed">
            <span class="streak-day-label">D1</span>
            <div class="streak-icon-circle">✓</div>
            <span class="streak-reward-text">+5</span>
          </div>
          <div class="streak-day-card completed">
            <span class="streak-day-label">D2</span>
            <div class="streak-icon-circle">✓</div>
            <span class="streak-reward-text">+6</span>
          </div>
          <div class="streak-day-card today pending" id="streakD3" onclick="claimStreakDay(3)">
            <span class="streak-day-label">D3</span>
            <div class="streak-icon-circle">🪙</div>
            <span class="streak-reward-text">+7</span>
          </div>
          <div class="streak-day-card pending">
            <span class="streak-day-label">D4</span>
            <div class="streak-icon-circle">🪙</div>
            <span class="streak-reward-text">+8</span>
          </div>
          <div class="streak-day-card pending">
            <span class="streak-day-label">D5</span>
            <div class="streak-icon-circle">🪙</div>
            <span class="streak-reward-text">+9</span>
          </div>
          <div class="streak-day-card pending">
            <span class="streak-day-label">D6</span>
            <div class="streak-icon-circle">🪙</div>
            <span class="streak-reward-text">+10</span>
          </div>
          <div class="streak-day-card pending">
            <span class="streak-day-label">★</span>
            <div class="streak-icon-circle">⭐</div>
            <span class="streak-reward-text">+15</span>
          </div>
        </div>

        <button class="btn-streak-checkin" id="btnDailyCheckin" onclick="claimStreakDay(3)">
          Checked in today
        </button>
        <p class="streak-footer-note">Day 2 of 7. Miss a day and streak restarts.</p>
      </div>

      <div class="section-header">
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
      </div>
    </div>

    <!-- TAB 3: MINERS -->
    <div class="tab-content" id="tab-miners">
      <div class="hero-card">
        <img class="flame-hero-img" src="data:image/jpeg;base64,{flame_b64}" alt="Flame">
        <h2 class="hero-title">Miners Store</h2>
        <p class="hero-subtitle">Hold more MRG to unlock faster miners. Nothing is spent — your level follows what you hold.</p>

        <div class="stats-trio">
          <div class="stat-trio-card">
            <div class="stat-trio-val">83</div>
            <div class="stat-trio-label">Level</div>
          </div>
          <div class="stat-trio-card">
            <div class="stat-trio-val">103</div>
            <div class="stat-trio-label">Peak</div>
          </div>
          <div class="stat-trio-card">
            <div class="stat-trio-val green">+71.5</div>
            <div class="stat-trio-label">Today's P&amp;L</div>
          </div>
        </div>

        <div class="level-progress-bar-wrap">
          <div class="level-progress-labels">
            <span class="next">Level 84</span>
            <span class="remain">3.0 MRG to go</span>
          </div>
          <div class="progress-track">
            <div class="progress-fill"></div>
          </div>
        </div>
      </div>

      <div class="action-nav-item" onclick="showToast('All-Time Mined: 2,348 MRG')">
        <div class="action-nav-left">
          <div class="action-nav-icon blue">📈</div>
          <div>
            <div class="action-nav-text-title">Performance &amp; P&amp;L</div>
            <div class="action-nav-text-sub">All-Time Mined: 2.3K MRG</div>
          </div>
        </div>
        <div class="action-nav-arrow">›</div>
      </div>

      <div class="action-nav-item" onclick="showToast('Peak Record: Level 103')">
        <div class="action-nav-left">
          <div class="action-nav-icon gold">🏆</div>
          <div>
            <div class="action-nav-text-title">All-time high</div>
            <div class="action-nav-text-sub">Peak Level 103</div>
          </div>
        </div>
        <div class="action-nav-arrow">›</div>
      </div>

      <div class="action-nav-item" onclick="openBuyDEXModal()">
        <div class="action-nav-left">
          <div class="action-nav-icon green">🔗</div>
          <div>
            <div class="action-nav-text-title">Buy MRG on DEX</div>
            <div class="action-nav-text-sub">Swap GRAM for MRG on STON.fi</div>
          </div>
        </div>
        <div class="action-nav-arrow">›</div>
      </div>

      <div class="content-box" style="margin-top: 14px;">
        <div style="font-size: 14px; font-weight: 700; color: #fff; margin-bottom: 8px;">Active Rig</div>
        <div style="font-size: 13px; color: var(--text-gray); line-height: 1.4;">
          Your current rig: <strong style="color: var(--accent-blue);">Level 83 Miner (3.19 TH/s)</strong>.
          Accumulating 0.0000085 MRG/sec. Maintain on-chain holdings to stay at Level 83.
        </div>
      </div>
    </div>

    <!-- TAB 4: FRIENDS -->
    <div class="tab-content" id="tab-friends">
      <!-- Profile Header Box -->
      <div class="user-profile-banner">
        <div class="user-profile-row">
          <div class="user-profile-pic-box">
            <div class="user-profile-pic">GF</div>
            <div class="tg-badge-overlay">✈</div>
          </div>
          <div class="user-profile-info">
            <div class="user-profile-name">GW FOISAL 100K | INFLUENCER</div>
            <div class="user-profile-handle">@GwFoisal</div>
            <div class="badge-chips-row">
              <span class="badge-chip nft">💎 Non-NFT Holder</span>
              <span class="badge-chip verified">✓ Verified</span>
            </div>
          </div>
        </div>

        <div class="lang-selector-bar" onclick="toggleLanguage()">
          <div class="lang-selector-left">
            <div class="lang-globe-icon">🌐</div>
            <span id="langLabel">Select Language</span>
          </div>
          <div class="lang-selector-right">
            <span id="curLangDisplay">🇬🇧 English</span>
            <span>›</span>
          </div>
        </div>
      </div>

      <!-- Invite Hero Card -->
      <div class="hero-card">
        <img class="heart-hero-img" src="data:image/jpeg;base64,{heart_b64}" alt="Heart">
        <h2 class="hero-title">Invite Friends</h2>
        <p class="hero-subtitle">Get +100 MRG for every friend who starts mining, plus 10% of their mining output — forever.</p>

        <div class="invite-action-buttons">
          <button class="btn-copy-ref" onclick="copyRefLink()">
            <span>📋</span>
            <span>Copy</span>
          </button>
          <button class="btn-share-ref" onclick="shareRefLink()">
            <span>✈</span>
            <span>Share</span>
          </button>
        </div>

        <div class="ref-link-display" id="refLinkText">t.me/mrgminerbot/app?startapp=ref_DDAWR83</div>
      </div>

      <div class="section-header">
        <span class="section-title">SQUAD MINING</span>
        <span class="badge-chip verified" style="font-size: 11px;">10%</span>
      </div>

      <div class="content-box">
        <div style="font-size: 26px; font-weight: 800; color: #fff; margin-bottom: 2px;">
          0.00 <span style="font-size: 16px; color: var(--text-gray);">MRG</span>
        </div>
        <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 14px;">≈ $0.000 earned from squad</div>

        <div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 12px;">
          <div style="display: flex; justify-content: space-between; font-size: 13px; color: var(--text-gray); margin-bottom: 8px;">
            <span>Alex Miner (@alex_ton)</span>
            <span style="color: var(--accent-green); font-weight: 700;">+24.5 MRG</span>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 13px; color: var(--text-gray); margin-bottom: 8px;">
            <span>CryptoPro (@cryptokid)</span>
            <span style="color: var(--accent-green); font-weight: 700;">+18.2 MRG</span>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 13px; color: var(--text-gray);">
            <span>Rakib TON (@rakib_dhaka)</span>
            <span style="color: var(--accent-green); font-weight: 700;">+12.0 MRG</span>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 5: WALLET -->
    <div class="tab-content" id="tab-wallet">
      <div class="hero-card">
        <img class="purse-hero-img" src="data:image/jpeg;base64,{purse_b64}" alt="Purse">
        <div class="unclaimed-label">In-App Wallet Balance</div>
        <div class="unclaimed-amount" style="font-size: 40px; margin: 4px 0;">
          <span id="walletMRGBalance">94.0</span>
          <span class="curr">MRG</span>
        </div>
        <div class="unclaimed-subrate" style="margin-bottom: 0;">≈ $0.12</div>

        <div class="wallet-action-row">
          <button class="btn-withdraw" onclick="openWithdrawModal()">
            <span>↗</span>
            <span>Withdraw</span>
          </button>
          <button class="btn-buy-mrg" onclick="openBuyDEXModal()">
            <span>🔄</span>
            <span>Buy MRG</span>
          </button>
        </div>
      </div>

      <div class="section-header">
        <span class="section-title">GRAM WALLET</span>
      </div>

      <div class="content-box">
        <div class="wallet-info-row">
          <div class="wallet-info-left">
            <div class="wallet-icon-box blue">👛</div>
            <div>
              <div class="wallet-info-title" id="tonAddress">UQBFoM...y-deRH</div>
              <div class="wallet-info-sub">2.0K MRG on-chain</div>
            </div>
          </div>
          <button class="btn-copy-address" onclick="copyAddress()">Copy</button>
        </div>

        <div class="wallet-info-row">
          <div class="wallet-info-left">
            <div class="wallet-icon-box purple">💎</div>
            <div>
              <div class="wallet-info-title">Total MRG Holding</div>
              <div class="wallet-info-sub">In-App + On-Chain</div>
            </div>
          </div>
          <div class="miner-stat-val" style="color: #fff;">2.1K MRG</div>
        </div>

        <div class="wallet-info-row" style="cursor: pointer;" onclick="toggleDisconnectWallet()">
          <div class="wallet-info-left">
            <div class="wallet-icon-box red">🚪</div>
            <div>
              <div class="wallet-info-title" style="color: var(--danger-red);" id="walletStatusText">Disconnect</div>
              <div class="wallet-info-sub">TON Connect v2</div>
            </div>
          </div>
        </div>
      </div>


      <div class="section-header">
        <span class="section-title">TRANSACTION HISTORY</span>
        <span class="section-badge" id="txCountBadge">5 entries</span>
      </div>

      <div class="history-filter-row">
        <div class="history-filter-chip active" onclick="setTxFilter('all', this)">All</div>
        <div class="history-filter-chip" onclick="setTxFilter('claim', this)">Claims</div>
        <div class="history-filter-chip" onclick="setTxFilter('withdraw', this)">Withdrawals</div>
        <div class="history-filter-chip" onclick="setTxFilter('deposit', this)">Deposits</div>
      </div>

      <div id="txHistoryContainer"></div>

      <div class="section-header">
        <span class="section-title">ACCOUNT</span>
      </div>

      <div class="content-box">
        <div class="wallet-info-row" onclick="showToast('Your on-chain identity is Verified')">
          <div class="wallet-info-left">
            <div class="wallet-icon-box green">🛡</div>
            <div>
              <div class="wallet-info-title">Account Verification</div>
              <div class="wallet-info-sub">Soulbound KYC on TON</div>
            </div>
          </div>
          <span style="color: var(--accent-green); font-size: 13px; font-weight: 700;">Verified ›</span>
        </div>
        <p style="font-size: 12px; color: var(--text-muted); margin-top: 10px; line-height: 1.4;">
          Verify on-chain to withdraw. Genesis NFT holders receive priority mempool processing and zero protocol fees.
        </p>
      </div>
    </div>

  </div>

  <!-- Bottom Navigation Bar -->
  <div class="bottom-nav">
    <div class="nav-tab active" id="nav-mine" onclick="switchTab('mine')">
      <div class="nav-tab-icon-wrap">
        <svg viewBox="0 0 24 24"><path d="M21.71 20.29l-1.42 1.42a1 1 0 0 1-1.41 0L14 16.83l-3 3-1.42-1.42 3-3-4.88-4.88A3 3 0 0 1 7.2 6.13L10.6 9.53l1.41-1.41-3.4-3.4a3 3 0 0 1 4.4 0l4.88 4.88 3-3 1.42 1.42-3 3 4.88 4.88a1 1 0 0 1 0 1.41zM2.29 8.71L8.7 2.3a1 1 0 0 1 1.41 0l1.42 1.41-5 5a1 1 0 0 1-1.41 0z"/></svg>
      </div>
      <span class="nav-tab-label">Mine</span>
    </div>

    <div class="nav-tab" id="nav-tasks" onclick="switchTab('tasks')">
      <div class="nav-tab-icon-wrap">
        <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-9 14l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
      </div>
      <span class="nav-tab-label">Tasks</span>
    </div>

    <div class="nav-tab" id="nav-miners" onclick="switchTab('miners')">
      <div class="nav-tab-icon-wrap">
        <svg viewBox="0 0 24 24"><path d="M11 21h-1l1-7H7.5c-.88 0-.33-.75-.31-.78C8.48 10.94 10.42 7.54 13.01 3h1l-1 7h3.51c.4 0 .62.19.4.66C14.73 14.71 12.82 18.06 11 21z"/></svg>
      </div>
      <span class="nav-tab-label">Miners</span>
    </div>

    <div class="nav-tab" id="nav-friends" onclick="switchTab('friends')">
      <div class="nav-tab-icon-wrap">
        <svg viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
      </div>
      <span class="nav-tab-label">Friends</span>
    </div>

    <div class="nav-tab" id="nav-wallet" onclick="switchTab('wallet')">
      <div class="nav-tab-icon-wrap">
        <svg viewBox="0 0 24 24"><path d="M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>
      </div>
      <span class="nav-tab-label">Wallet</span>
    </div>
  </div>

  <!-- Toast Notification -->
  <div class="toast-msg" id="toastMsg">
    <span id="toastIcon">✨</span>
    <span id="toastText">Message</span>
  </div>


  <!-- Transaction Details Modal -->
  <div class="modal-backdrop" id="txDetailModal">
    <div class="modal-sheet">
      <div class="modal-title" id="modalTxTitle">Transaction Details</div>
      <div class="modal-desc" id="modalTxDesc">Confirmed on TON Network</div>
      <div style="background: #101724; border-radius: 14px; padding: 14px; margin-bottom: 16px; border: 1px solid #23344d;">
        <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 10px;">
          <span style="color: var(--text-gray);">Amount:</span>
          <strong id="modalTxAmount" style="color: var(--accent-green);">+0.00 MRG</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 10px;">
          <span style="color: var(--text-gray);">Type:</span>
          <strong id="modalTxType" style="color: #fff;">Mining Claim</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 10px;">
          <span style="color: var(--text-gray);">Status:</span>
          <strong id="modalTxStatus" style="color: var(--accent-green);">Completed ✓</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 10px;">
          <span style="color: var(--text-gray);">Date &amp; Time:</span>
          <span id="modalTxTime" style="color: #fff; font-size: 13px;">Today</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 13px;">
          <span style="color: var(--text-gray);">Hash / ID:</span>
          <span id="modalTxHash" style="color: var(--accent-blue); font-family: monospace;">ton_tx_91823</span>
        </div>
      </div>
      <button class="modal-btn-confirm" onclick="viewOnExplorer()">View on TonScan</button>
      <button class="modal-btn-confirm" style="background: transparent; color: var(--text-muted); margin-top: 8px;" onclick="closeTxModal()">Close</button>
    </div>
  </div>

  <!-- Withdraw Modal -->
  <div class="modal-backdrop" id="withdrawModal">
    <div class="modal-sheet">
      <div class="modal-title">Withdraw MRG</div>
      <div class="modal-desc">Transfer your in-app MRG tokens directly to your TON / GRAM wallet address.</div>
      <input type="text" class="modal-input" id="withdrawAddress" placeholder="Enter TON Wallet (UQ... / EQ...)" value="UQBFoMy-deRHYz842P39910">
      <input type="number" class="modal-input" id="withdrawAmount" placeholder="Amount (MRG)" value="50.0">
      <div style="display: flex; justify-content: space-between; font-size: 13px; color: var(--text-gray); margin-bottom: 14px;">
        <span>Network Gas Fee:</span>
        <span style="color: #fff; font-weight: 700;">0.05 TON (Sponsored)</span>
      </div>
      <button class="modal-btn-confirm" onclick="confirmWithdraw()">Confirm Transfer</button>
      <button class="modal-btn-confirm" style="background: transparent; color: var(--text-muted); margin-top: 8px;" onclick="closeWithdrawModal()">Cancel</button>
    </div>
  </div>

  <!-- Buy MRG DEX Modal -->
  <div class="modal-backdrop" id="buyModal">
    <div class="modal-sheet">
      <div class="modal-title">Buy MRG on STON.fi</div>
      <div class="modal-desc">Swap GRAM or TON for MRG tokens via the leading decentralized exchange on The Open Network.</div>
      <div style="background: #101724; border-radius: 14px; padding: 14px; margin-bottom: 16px; border: 1px solid #23344d;">
        <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 8px;">
          <span style="color: var(--text-gray);">Pair:</span>
          <strong style="color: #fff;">MRG / GRAM</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 8px;">
          <span style="color: var(--text-gray);">Rate:</span>
          <strong style="color: var(--accent-green);">1 MRG ≈ 0.00125 TON</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 14px;">
          <span style="color: var(--text-gray);">Slippage:</span>
          <strong style="color: #fff;">0.5%</strong>
        </div>
      </div>
      <button class="modal-btn-confirm" onclick="simulateSwap()">Open STON.fi DEX</button>
      <button class="modal-btn-confirm" style="background: transparent; color: var(--text-muted); margin-top: 8px;" onclick="closeBuyModal()">Close</button>
    </div>
  </div>

  <!-- Audio Synthesizer via Web Audio API -->
  <script>
    let audioCtx = null;
    function playTone(freq, type = 'sine', duration = 0.12, vol = 0.15) {{
      try {{
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(vol, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      }} catch (e) {{}}
    }}

    function soundTap() {{ playTone(540, 'triangle', 0.08, 0.1); }}
    function soundClaim() {{
      playTone(440, 'sine', 0.1, 0.2);
      setTimeout(() => playTone(660, 'sine', 0.15, 0.25), 80);
      setTimeout(() => playTone(880, 'sine', 0.25, 0.3), 160);
    }}
    function soundSuccess() {{
      playTone(523.25, 'triangle', 0.1, 0.15);
      setTimeout(() => playTone(659.25, 'triangle', 0.15, 0.2), 100);
      setTimeout(() => playTone(783.99, 'triangle', 0.2, 0.25), 200);
    }}

    // State
    const state = {{
      currentTab: 'mine',
      topMRG: 2100.0,
      walletMRG: 94.0,
      unclaimedMRG: 0.002938,
      miningRatePerSec: 0.0000085,
      streakDay: 2,
      lang: 'en'
    }};

    // Load persisted state
    try {{
      const saved = localStorage.getItem('mrg_miner_state');
      if (saved) {{
        const parsed = JSON.parse(saved);
        state.walletMRG = parsed.walletMRG ?? state.walletMRG;
        state.unclaimedMRG = parsed.unclaimedMRG ?? state.unclaimedMRG;
        state.topMRG = parsed.topMRG ?? state.topMRG;
        state.streakDay = parsed.streakDay ?? state.streakDay;
        state.lang = parsed.lang ?? state.lang;
      }}
    }} catch (e) {{}}

    function saveState() {{
      try {{
        localStorage.setItem('mrg_miner_state', JSON.stringify(state));
      }} catch (e) {{}}
    }}


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

    // Real-time ticking mining rate
    setInterval(() => {{
      state.unclaimedMRG += (state.miningRatePerSec / 10);
      document.getElementById('unclaimedVal').innerText = state.unclaimedMRG.toFixed(6);
      document.getElementById('btnClaimVal').innerText = state.unclaimedMRG.toFixed(4);
    }}, 100);

    // Countdown Timer in Mine Card
    let secondsRemaining = 23 * 3600 + 59 * 60 + 57;
    setInterval(() => {{
      if (secondsRemaining > 0) secondsRemaining--;
      const h = String(Math.floor(secondsRemaining / 3600)).padStart(2, '0');
      const m = String(Math.floor((secondsRemaining % 3600) / 60)).padStart(2, '0');
      const s = String(secondsRemaining % 60).padStart(2, '0');
      const timerEl = document.getElementById('miningTimer');
      if (timerEl) timerEl.innerText = `${{h}}:${{m}}:${{s}}`;
    }}, 1000);

    // Switch Tabs
    function switchTab(tabId) {{
      soundTap();
      state.currentTab = tabId;
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-tab').forEach(el => el.classList.remove('active'));

      const targetTab = document.getElementById(`tab-${{tabId}}`);
      const targetNav = document.getElementById(`nav-${{tabId}}`);
      if (targetTab) targetTab.classList.add('active');
      if (targetNav) targetNav.classList.add('active');

      window.scrollTo({{ top: 0, behavior: 'smooth' }});

      // Telegram haptic
      if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {{
        window.Telegram.WebApp.HapticFeedback.impactOccurred('light');
      }}
    }}

    // Tap on Mascot Coin
    const mascotCoin = document.getElementById('mascotCoin');
    const coinStage = document.getElementById('coinStage');
    if (mascotCoin && coinStage) {{
      mascotCoin.addEventListener('click', (e) => {{
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

        if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {{
          window.Telegram.WebApp.HapticFeedback.impactOccurred('medium');
        }}
      }});
    }}

    // Claim Mining Reward
    function claimMiningReward() {{
      if (state.unclaimedMRG <= 0) {{
        showToast('No rewards to claim right now!');
        return;
      }}
      soundClaim();
      const claimed = state.unclaimedMRG;
      state.walletMRG += claimed;
      state.topMRG += claimed;
      state.unclaimedMRG = 0.000000;

      document.getElementById('unclaimedVal').innerText = '0.000000';
      document.getElementById('btnClaimVal').innerText = '0.00';
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';

      showToast(`🎉 Claimed +${{claimed.toFixed(4)}} MRG to In-App Wallet!`);
      saveState();

      if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.HapticFeedback) {{
        window.Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      }}
    }}

    // Streak Check-in
    function claimStreakDay(day) {{
      if (state.streakDay >= day) {{
        showToast('Already checked in for today!');
        return;
      }}
      soundClaim();
      state.streakDay = day;
      const reward = 5 + day;
      state.walletMRG += reward;
      state.topMRG += reward;

      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';

      const dCard = document.getElementById(`streakD${{day}}`);
      if (dCard) {{
        dCard.classList.remove('pending');
        dCard.classList.add('completed');
        dCard.querySelector('.streak-icon-circle').innerText = '✓';
      }}
      document.getElementById('streakBadge').innerText = `Day ${{day}} of 7`;
      document.getElementById('btnDailyCheckin').innerText = 'Checked in today';
      document.getElementById('btnDailyCheckin').classList.remove('active-claim');

      showToast(`🔥 Day ${{day}} Check-in complete! +${{reward}} MRG added`);
      saveState();
    }}

    // Tasks Execution
    function executeTask(itemEl, taskTitle, reward) {{
      soundTap();
      showToast(`Checking task: ${{taskTitle}}...`);
      setTimeout(() => {{
        soundSuccess();
        state.walletMRG += reward;
        state.topMRG += reward;
        document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
        document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';
        itemEl.style.opacity = '0.5';
        itemEl.style.pointerEvents = 'none';
        const rightBadge = itemEl.querySelector('.task-timer-badge') || itemEl.querySelector('.task-claim-btn');
        if (rightBadge) rightBadge.innerText = 'Completed ✓';
        showToast(`✅ Task Completed! +${{reward}} MRG added.`);
        saveState();
      }}, 1200);
    }}

    // Referral Copy & Share
    function copyRefLink() {{
      soundTap();
      const link = 'https://t.me/mrgminerbot/app?startapp=ref_DDAWR83';
      if (navigator.clipboard) {{
        navigator.clipboard.writeText(link).then(() => {{
          showToast('📋 Referral link copied to clipboard!');
        }}).catch(() => {{
          showToast('Referral: t.me/mrgminerbot/app?startapp=ref_DDAWR83');
        }});
      }} else {{
        showToast('Referral link copied!');
      }}
    }}

    function shareRefLink() {{
      soundTap();
      const link = 'https://t.me/mrgminerbot/app?startapp=ref_DDAWR83';
      const text = 'Join MRG Cloud Mining with me and earn daily free MRG tokens!';
      if (navigator.share) {{
        navigator.share({{ title: 'MRG Miner Bot', text: text, url: link }}).catch(() => {{}});
      }} else {{
        copyRefLink();
      }}
    }}

    function copyAddress() {{
      soundTap();
      const addr = 'UQBFoMy-deRHYz842P39910y-deRH';
      if (navigator.clipboard) {{
        navigator.clipboard.writeText(addr);
      }}
      showToast('Wallet address copied to clipboard!');
    }}

    function toggleDisconnectWallet() {{
      soundTap();
      const txt = document.getElementById('walletStatusText');
      if (txt.innerText === 'Disconnect') {{
        txt.innerText = 'Connect Wallet';
        txt.style.color = 'var(--accent-blue)';
        showToast('Wallet Disconnected.');
      }} else {{
        txt.innerText = 'Disconnect';
        txt.style.color = 'var(--danger-red)';
        showToast('Wallet Connected: UQBFoM...y-deRH');
      }}
    }}

    // Modals
    function openWithdrawModal() {{
      soundTap();
      document.getElementById('withdrawModal').classList.add('show');
    }}
    function closeWithdrawModal() {{
      document.getElementById('withdrawModal').classList.remove('show');
    }}
    function confirmWithdraw() {{
      const amt = parseFloat(document.getElementById('withdrawAmount').value) || 0;
      if (amt <= 0 || amt > state.walletMRG) {{
        showToast('⚠️ Invalid amount! Insufficient in-app balance.');
        return;
      }}
      soundSuccess();
      state.walletMRG -= amt;
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      closeWithdrawModal();
      showToast(`🚀 Withdrawal of ${{amt}} MRG submitted to TON mempool!`);
      saveState();
    }}

    function openBuyDEXModal() {{
      soundTap();
      document.getElementById('buyModal').classList.add('show');
    }}
    function closeBuyModal() {{
      document.getElementById('buyModal').classList.remove('show');
    }}
    function simulateSwap() {{
      closeBuyModal();
      showToast('Opening STON.fi DEX swap pool...');
    }}

    // Language Toggle
    function toggleLanguage() {{
      soundTap();
      if (state.lang === 'en') {{
        state.lang = 'bn';
        document.getElementById('curLangDisplay').innerText = '🇧🇩 বাংলা';
        document.getElementById('langLabel').innerText = 'ভাষা নির্বাচন করুন';
        showToast('বাংলা ভাষা সক্রিয় করা হয়েছে');
      }} else {{
        state.lang = 'en';
        document.getElementById('curLangDisplay').innerText = '🇬🇧 English';
        document.getElementById('langLabel').innerText = 'Select Language';
        showToast('Language changed to English');
      }}
      saveState();
    }}

    function handleTgClose() {{
      soundTap();
      if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.close) {{
        window.Telegram.WebApp.close();
      }} else {{
        showToast('Telegram Mini App active');
      }}
    }}

    // Toast Helper
    let toastTimeout;
    function showToast(msg) {{
      const toast = document.getElementById('toastMsg');
      const text = document.getElementById('toastText');
      text.innerText = msg;
      toast.classList.add('show');
      clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {{
        toast.classList.remove('show');
      }}, 2600);
    }}

    // Init Telegram WebApp API if inside Telegram
    window.addEventListener('DOMContentLoaded', () => {{
      if (window.Telegram && window.Telegram.WebApp) {{
        window.Telegram.WebApp.ready();
        window.Telegram.WebApp.expand();
      }}
      // Render initial values
      document.getElementById('walletMRGBalance').innerText = state.walletMRG.toFixed(1);
      document.getElementById('topBalance').innerText = (state.topMRG / 1000).toFixed(1) + 'K';
      renderTransactions();
      if (state.lang === 'bn') {{
        document.getElementById('curLangDisplay').innerText = '🇧🇩 বাংলা';
        document.getElementById('langLabel').innerText = 'ভাষা নির্বাচন করুন';
      }}
    }});
  </script>
</body>
</html>
'''

with open('app/src/main/assets/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('telegram_miner_bot.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated single-file HTML! Size: {len(html_content)} bytes")
