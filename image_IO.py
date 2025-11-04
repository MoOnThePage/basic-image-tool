# Reading/Loading the image function
# TODO: add navigation
# TODO: add multiple file selection
# TODO: brows with Filtering

import os
import cv2

# Constant Variables
asset_folder = "sample_images/" # image samples directory

def file_browser(asset_folder):
    """
    list the files (images) in a given directory
    :param asset_folder:
    :return: image to be loaded
    """

    files = os.listdir(asset_folder)

    print("Available files:")
    for index, file in enumerate(files, 1):
        print(f"[{index}] - {file}")

    try:
        choice = int(input("\nEnter file number: ")) - 1
        if 0 <= choice < len(files):
            return files[choice]
        else:
            print("Invalid selection!")
            return None
    except ValueError:
        print("Pleas enter a valid file number!")
        return None

def load_image():
    """
    Load an image from a given index

    :return: the loaded image
    """

    image_to_process = file_browser(asset_folder)
    print(image_to_process)
    image_handler = cv2.imread(asset_folder + image_to_process)

    # Check if the image is loaded or not
    if image_handler is None:
        print(f"Error: {image_to_process} is not a valid image could not be loaded.")
        exit()
    else:
        print("Image loaded successfully.")
        return image_handler