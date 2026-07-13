from pathlib import Path
from sonic_feature_extraction import audio_extraction
from get_lyrics import get_lyrics

folder_path = Path(
    "/mnt/Network/Github_Projects/AI-Agents-Intensive-Vibe-Coding-Capstone-Project/demo_audio_files/"
)

file_names = []
file_paths = []

for file_path in folder_path.glob("*"):
    if file_path.is_file():
        file_names.append(file_path.name)
        file_paths.append(file_path)

while True:
    i = 10
    try:
        for i in range(i):
            
