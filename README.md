# Image Similarity Finder / Duplicate Image Finder / Deduper

This script searches through all images in an input folder (JPG and PNG), and copies the ones that are more different / unique to an Output folder.

It includes a threshold setting so you can choose how different the images need to be to make the cut.

It will also copy any matching .txt files in the same directory as the images. This is useful for automatically captioned datasets.


## Installation Instructions
1. Create a VENV ([here's an automatic tool](https://github.com/MNeMoNiCuZ/create_venv))
2. Run `pip install -r requirements.txt`
3. Manually install Pytorch, follow instructions: https://pytorch.org/
4. Place dataset in the Input-folder. Images can go in the root or subfolders just fine. Each subfolder will be compared against itself.
5. Tweak configuration in dedupe.py. Threshold need to be tweaked to your preferences.
6. Run `py dedupe.py`
