from pathlib import Path

import librosa
import numpy as np


def audio_extraction(filepath):
    y, sr = librosa.load(filepath)

    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_mean = np.mean(chroma, axis=0)
    chroma_std = np.std(chroma, axis=0)
    print(chroma)


folderpath = Path("/mnt/Personal_Data/Video/demo_folder/")
# Assuming that only required audio files are inside the given folder


for filepath in folderpath.iterdir():
    # print(f"Song Name: {filepath.name}")
    audio_extraction(filepath)
