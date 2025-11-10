# Reading/Loading the image function

import os
from pathlib import Path
import cv2


def fileBrowser(startDirectory = '.'):
    """
    FIle Browser with Navigation
    :param startDirectory:
    :return: selected image
    """
    currentDirectory = Path(startDirectory).resolve()

    while True:
        print('\033[2J\033[H', end='')  # clear screen

        print(f"Current directory: {currentDirectory}")
        print('-' * 50)

        # Get items and separate files from directories
        items = os.listdir(currentDirectory)
        directories = []
        files = []

        for item in items:
            itemPath = currentDirectory / item
            if itemPath.is_dir():
                directories.append(item)
            else:
                files.append(item)

        # Display directory first
        print("\nDirectories:")
        for i, directoryName in enumerate(directories, 1):
            print(f"{i}. {directoryName}/")

        # Display files
        print("\nFiles:")
        for i, fileName in enumerate(files, len(directories) + 1):
            print(f"{i}. {fileName}")

        print(f"\n{len(directories) + len(files) + 1}. Go Up")
        print(f"\n{len(directories) + len(files) + 2}. Exit browser")

        try:
            choice = int(input("\nEnter your choice: "))
            if choice == len(directories) + len(files) + 1:
                # Go Up
                currentDirectory = currentDirectory.parent
            elif choice == len(directories) + len(files) + 2:
                # Exit
                return None
            elif 1 <= choice <= len(directories):
                # Select directory
                selectedDirectory = directories[choice - 1]
                currentDirectory = currentDirectory / selectedDirectory
            elif len(directories) < choice <= len(directories) + len(files):
                # Select File
                selectedFile = files[choice - len(directories) - 1]
                return currentDirectory / selectedFile
            else:
                input("Invalid choice! Press Enter to continue...")
        except ValueError:
            input("Pleas enter a valid number! Press Enter to continue...")

def loadImage():
    """
    Load an image from a given index

    :return: the loaded image
    """

    image_to_process = fileBrowser()
    print(image_to_process)
    image_handler = cv2.imread(image_to_process)

    # Check if the image is loaded or not
    if image_handler is None:
        print(f"Error: {image_to_process} is not a valid image could not be loaded.")
        exit()
    else:
        print("Image loaded successfully.")
        return image_handler