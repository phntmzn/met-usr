import os
import random
from itertools import product

# --- Aesthetic Components ---
emotions = ['glitch', 'cry', 'drain', 'vibe', 'bliss', 'crash', 'fade', 'burn', 'melt', 'dream']
targets = ['luv', 'core', 'ghost', '404', 'bleed', 'nite', 'angel', 'void', 'rage', 'shine']
symbols = ['<3', 'xX', '_', '~', '!']
digits = ['03am', '666', '143', '999', '777', '001', '777x', '0ver', 'xoxo', 'xx']
http_codes = ['200ok', '301move', '302fast', '403deny', '404loop', '500error', '503fail', '204none', '100ping', '429limit']

# --- Generate all unique name combinations and shuffle ---
all_combinations = list(product(emotions, targets, digits, symbols, http_codes))
random.shuffle(all_combinations)
combo_index = 0

# --- Folder path (update this) ---
folder = '/Users/macbookair/Desktop/wav_only_200'  # ← CHANGE THIS

# --- Get list of files to rename ---
audio_files = [f for f in os.listdir(folder) if f.lower().endswith(('.mp3', '.wav'))]

# --- Name generator ---
def generate_unique_name():
    global combo_index
    if combo_index >= len(all_combinations):
        raise Exception("Ran out of unique hyperpop hacker names 💀💔")
    emo, tgt, dig, sym, code = all_combinations[combo_index]
    combo_index += 1
    return f"x86<3_{emo}{sym}{tgt}_{dig}-{code}"

# --- Rename files ---
for filename in audio_files:
    base, ext = os.path.splitext(filename)
    new_name = generate_unique_name() + ext
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} → {new_name}")
