import fiftyone as fo
import fiftyone.zoo as foz
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
import shutil

# Configuration
input_dir = "Input"
output_dir = "Output"
model_name = "clip-vit-base32-torch"
threshold = 0.9

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load model
model = foz.load_zoo_model(model_name)

def process_directory(input_subdir, output_subdir):
    # Check if the directory is effectively empty (no images)
    if not any(file.endswith(('.jpg', '.png')) for file in os.listdir(input_subdir)):
        print(f"Skipping empty or non-image directory: {input_subdir}")
        return

    # Attempt to load dataset from directory
    try:
        dataset = fo.Dataset.from_dir(dataset_dir=input_subdir, dataset_type=fo.types.ImageDirectory)
    except ValueError as e:
        print(f"Error loading images from {input_subdir}: {e}")
        return

    # Compute embeddings
    embeddings = dataset.compute_embeddings(model, batch_size=32)

    # Calculate the similarity matrix
    similarity_matrix = cosine_similarity(embeddings)
    similarity_matrix -= np.identity(len(similarity_matrix))

    # Determine duplicates based on threshold
    samples_to_remove = []
    for idx, sample in enumerate(dataset):
        if np.max(similarity_matrix[idx]) > threshold:
            samples_to_remove.append(sample.id)

    num_removed = len(samples_to_remove)
    # Correct calculation of num_kept
    num_kept = len(dataset) - num_removed  # Calculate num_kept before deleting samples

    dataset.delete_samples(samples_to_remove)

    print(f"Processed {input_subdir}: {num_kept} kept, {num_removed} removed.")

    # Copy remaining images and their corresponding .txt files
    for sample in dataset:
        file_path = sample.filepath
        relative_path = os.path.relpath(file_path, input_dir)
        output_file_path = os.path.join(output_dir, relative_path)
        
        # Ensure output subdirectory exists
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        shutil.copy(file_path, output_file_path)

        # Check for and copy corresponding .txt file
        txt_path = os.path.splitext(file_path)[0] + ".txt"
        if os.path.exists(txt_path):
            shutil.copy(txt_path, os.path.splitext(output_file_path)[0] + ".txt")

# Walk through input directory and process each subdirectory
for subdir, dirs, files in os.walk(input_dir):
    output_subdir = os.path.join(output_dir, os.path.relpath(subdir, input_dir))
    process_directory(subdir, output_subdir)

print("Deduplication complete. Check the Output directory for results.")
