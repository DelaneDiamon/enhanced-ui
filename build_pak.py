import os, sys, zipfile
MODS_DIR = 'mods'
PAK_NAME = 'enhanced_ui.pak'
PAK_PATH = MODS_DIR + '/' + PAK_NAME
SRC_DIR = 'ssl'
if not os.path.isdir(SRC_DIR):
    print('nothing to pack: ssl directory missing', file=sys.stderr)
    sys.exit(1)
os.makedirs(MODS_DIR, exist_ok=True)
if os.path.exists(PAK_PATH):
    os.remove(PAK_PATH)
with zipfile.ZipFile(PAK_PATH, 'w', zipfile.ZIP_STORED) as z:
    for base, _, files in os.walk(SRC_DIR):
        for f in files:
            p = os.path.join(base, f)
            z.write(p, p)
print('Built', PAK_PATH)
game_mods = '/mnt/c/Games/Steam/steamapps/common/Space Marine 2/client_pc/root/mods'
os.makedirs(game_mods, exist_ok=True)
cfg = game_mods + '/pak_config.yaml'
lines = []
if os.path.exists(cfg):
    with open(cfg,'r',encoding='utf-8',errors='ignore') as f:
        lines = [ln.rstrip('\n') for ln in f]
entry = '- pak: ' + PAK_NAME
if entry not in lines:
    lines.append(entry)
with open(cfg,'w',encoding='utf-8') as f:
    f.write('\n'.join([ln for ln in lines if ln]) + '\n')
