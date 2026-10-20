import os

with open('app/src/main/assets/coin.b64') as f: coin_b64 = f.read().strip()
with open('app/src/main/assets/trophy.b64') as f: trophy_b64 = f.read().strip()
with open('app/src/main/assets/purse.b64') as f: purse_b64 = f.read().strip()
with open('app/src/main/assets/heart.b64') as f: heart_b64 = f.read().strip()
with open('app/src/main/assets/flame.b64') as f: flame_b64 = f.read().strip()

with open('template.html', 'r', encoding='utf-8') as f:
    template = f.read()

template = template.replace('__COIN_B64__', coin_b64)
template = template.replace('__TROPHY_B64__', trophy_b64)
template = template.replace('__PURSE_B64__', purse_b64)
template = template.replace('__HEART_B64__', heart_b64)
template = template.replace('__FLAME_B64__', flame_b64)

with open('app/src/main/assets/index.html', 'w', encoding='utf-8') as f:
    f.write(template)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(template)

with open('telegram_miner_bot.html', 'w', encoding='utf-8') as f:
    f.write(template)

print("Generated HTML successfully! File size:", len(template))

