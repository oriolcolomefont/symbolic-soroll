# Symbolic Soroll

## Setup

1. Install conda
2. Create a conda environment (I called it `soroll`, "noise" in Catalan)
3. Install dependencies (more or less the same as clamp/requirements.txt)
4. Good luck!

These dependencies worked for me:

```
transformers==4.41.2
torch==2.3.0.dev20240110
torchaudio==2.2.0.dev20240110
torchvision==0.18.0.dev20240110
tqdm==4.63.1
```

If I remember correctly, I've installed `transformers` and `unidecode` with conda instead of pip

## Usage

```bash
conda activate soroll
```

### Clamp

```bash
python clamp/clamp.py -clamp_model_name sander-wood/clamp-small-512 -query_modal text -key_modal music -top_n 100
```
