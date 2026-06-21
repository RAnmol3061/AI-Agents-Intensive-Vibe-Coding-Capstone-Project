from pathlib import Path

folderpath = Path("/mnt/Personal_Data/Video/demo_folder/")
# Assuming that only required audio files are inside the given folder
for filepath in folderpath.iterdir():
    print(f"Song Name: {filepath.name}")
