from pathlib import Path

import numpy as np


def chroma_to_notes(npz_files: list):
    notes_array = np.array(
        ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    )
    for file in npz_files:
        with np.load(file) as data:
            chroma_mean = data["arr1"]
            top_chroma_mean = np.argpartition(chroma_mean, -3)[-3:]
            mapped_notes = notes_array[top_chroma_mean]
            print(mapped_notes)


def feature_to_text(filepath: str):
    npz_files = list(Path(filepath).glob("*.npz"))
    chroma_to_notes(npz_files)  # Chroma to Notes


feature_to_text("./demo_audio_files/")
