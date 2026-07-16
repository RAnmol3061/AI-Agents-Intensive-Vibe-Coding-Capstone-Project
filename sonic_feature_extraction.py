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

    np.savez_compressed(
        file=filepath[:-3] + "npz",
        arr1=chroma_mean,
        arr2=chroma_std,
        arr3=rms_mean,
        arr4=rms_std,
        arr5=mfcc_mean,
        arr6=mfcc_std,
    )
