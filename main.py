from pathlib import Path

import librosa
import numpy as np


def audio_extraction(filepath):
    y, sr = librosa.load(filepath)

    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_mean = np.mean(chroma, axis=1)  # 12
    chroma_std = np.std(chroma, axis=1)  # 12

    rms = librosa.feature.rms(y=y)
    rms_mean = np.mean(rms)  # 1
    rms_std = np.std(rms)  # 1

    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    mfcc_mean = np.mean(mfccs, axis=1)
    mfcc_std = np.std(mfccs, axis=1)

    final_vector = np.concatenate(
        (
            chroma_mean,
            chroma_std,  # 12 + 12 floats
            [rms_mean, rms_std],  # 1 + 1 float
            mfcc_mean,
            mfcc_std,  # 20 + 20 float
        )
    )

    return final_vector


folderpath = Path("/mnt/Personal_Data/Video/demo_folder/")
# Assuming that only required audio files are inside the given folder


for filepath in folderpath.iterdir():
    # print(f"Song Name: {filepath.name}")
    h = audio_extraction(filepath)
    print(h)
    print(np.shape(h))
    break
