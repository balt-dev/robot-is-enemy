import glob
import os
import sys
from pathlib import Path
import shutil


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage:\n\tsetup.py <path to MSB install>")
        return
    path = Path(args[1]) / 'Data'
    if Path("data/vanilla").exists():
        shutil.rmtree("data/vanilla")
    os.mkdir("data/vanilla")
    os.mkdir("data/vanilla/sprites")
    os.system(f"lua converter.lua {path / 'values.lua'} data/vanilla/tiles.json")
    for file in (path / 'assets' / 'default' / 'sprites').glob('*.png'):
        shutil.copy2(file, "data/vanilla/sprites/")
    shutil.copytree(path / 'assets' / 'default' / 'sprites' / 'terrain', "data/vanilla/sprites/", dirs_exist_ok=True)
    print("Done")


if __name__ == "__main__":
    main()
