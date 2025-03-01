# server/file_utils.py
import os

def delete_image_file(image_path: str):
    """
    Deletes an image file from the given path.
    """
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Deleted file: {image_path}")
    else:
        print(f"File not found: {image_path}")
