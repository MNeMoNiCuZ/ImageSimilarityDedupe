# Image Similarity Finder / Duplicate Image Finder / Image Deduper

This script is designed to streamline the process of identifying and segregating duplicate or highly similar images within a given dataset. It effectively scans through all images within a specified input folder, supporting both JPG and PNG formats. The core functionality involves filtering out and relocating images deemed significantly unique or dissimilar to an Output folder, based on a customizable similarity threshold.

Additionally, this utility extends its convenience by automatically copying associated .txt files found within the same directory as the processed images. This feature is particularly beneficial for datasets accompanied by auto-generated captions, facilitating a streamlined management of image-caption pairs.

## Installation Instructions
Follow these steps to set up and run the Image Similarity Finder:

1. Initialize a virtual environment (VENV) for project isolation. An easy-to-use tool for creating a VENV can be found [here](https://github.com/MNeMoNiCuZ/create_venv).
2. Install the required Python packages by executing: `pip install -r requirements.txt` in your terminal.
3. For Pytorch installation, which is necessary for the script to function, refer to the official [Pytorch installation guide](https://pytorch.org/).
4. Prepare your dataset by placing image files within the Input-folder. The script is designed to accommodate images located either in the root directory or nested within subfolders. It's worth noting that images in each subfolder are compared exclusively against others in the same subfolder.
5. Adjust the script's configuration settings in `dedupe.py` to suit your specific needs. The similarity threshold, in particular, is a critical parameter that determines which images are considered duplicates. Fine-tuning this setting will allow for more precise control over the deduplication process.
6. To execute the script, navigate to the project directory in your terminal and run `py dedupe.py`. This will initiate the scanning and deduplication process based on the parameters you've set.
