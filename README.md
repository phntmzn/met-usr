```markdown
# 🎛️ met-usr-main

`met-usr-main` is a high-performance macOS audio/MIDI generation and rendering pipeline that uses Metal for real-time GPU-accelerated post-processing of WAV files rendered from MIDI. It combines custom harmonic structures with efficient parallel processing.

---

## 🚀 Features

- ✅ **GPU Audio Effects** — Real-time processing with Metal shaders (gain, distortion, stutter, glitch, inversion)
- 🎼 **Layered MIDI Generator** — Generates triads, basslines, and FX notes across multiple tracks
- 🧠 **Parallel Rendering** — Converts hundreds of MIDI files to WAVs using `ProcessPoolExecutor`
- 🔁 **Metal Shader Pipeline** — On-the-fly compilation and dispatch of Metal kernels for audio post-effects
- 🧪 **Batch Audio Generation** — Generate and process hundreds of WAV files with randomized harmonies and FX

---

## 📁 Project Structure

```
met-usr-main/
├── a.py                 # Main generator: MIDI → WAV → GPU FX
├── b.py                 # Definitions: notes, scales, durations, chords
├── README.md            # This file
```

---

## 🧰 Requirements

- macOS 12+
- Python 3.9+
- [PyObjC](https://pypi.org/project/pyobjc/)
- [midiutil](https://pypi.org/project/MIDIUtil/)
- [FluidSynth](https://github.com/FluidSynth/fluidsynth)
- Metal compiler tools (`xcrun` from Xcode)

Install Python dependencies:

```bash
pip install pyobjc midiutil numpy scipy tqdm
```

Install FluidSynth (if needed):

```bash
brew install fluidsynth
```

---

## ⚙️ Configuration

Inside `a.py`, update the following paths to match your system:

```python
SOUNDFONT_PATH = "/path/to/your/soundfont.sf2"
FLUIDSYNTH_PATH = "/opt/homebrew/bin/fluidsynth"
```

---

## 🛠️ Usage

To generate 200 GPU-processed `.wav` files to your Desktop:

```bash
python3 a.py
```

The script:
1. Generates MIDI with layered harmonies.
2. Renders it to WAV using FluidSynth.
3. Applies one of several GPU audio effects using Metal.

Output will be saved to:

```
~/Desktop/wav_only_200/
```

---

## 🎨 GPU Audio Effects (Metal)

The following post-effects are available and applied randomly per file:

| Effect ID | Description        |
|-----------|--------------------|
| 1         | Gain reduction     |
| 2         | Distortion         |
| 3         | Glitch/stutter     |
| 4         | Inversion          |
| 5         | Circular buffer FX |

---

## ⚠️ Disclaimer

This project is for **educational and research** use only. Use responsibly and test only on authorized systems.

---

## 📄 License

MIT License © 2025 [`phntmzn`](https://github.com/phntmzn)
```
