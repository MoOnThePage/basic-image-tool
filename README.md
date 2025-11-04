# Basic Image Tool - Mini Image Processing App (OpenCV + Python)

## Project Overview
**Basic Image Tool** is a beginner-friendly image processing project built with Python and OpenCV. It provides a simple
command-line interface that allows users to perform essential image operations, from loading and editing images to saving
them in different formats.

This project was developed as a practical application of the **Mastering OpenCV with Python** course from OpenCV University,
evolving through learning modules as new concepts are learned and applied.

## Project Goals
- Provide a practical way for learner to experiment with OpenCV.
- Demonstrate fundamental image operations in a runnable tool.
- Build clean, modular, and maintainable code, starting from scripts toward structured software

## Tech Stack
- Programming Langauge: Python 3.xx
- Libraries: OpenCV (cv2), NumPy
- Platform: Command Line (CLI)
- Future: GUI version with PySide using Qt Creator

## Features
- Interactive file browser, dynamically list images from the "sample_images/" directory
- Convert between color spaces (BGR, Grayscale, HSV, LAB)
- Resize images
- Center crop
- Add text annotations
- Save or export to different formats

> All operations are applied toa single image in the memory and previewed via resizable OpenCV windows.

## How to USE
1. Clone the repository
2. Install dependencies: OpenCV and NumPy
3. Runs the script: `python basic_image_tool.py`
4. Follow the on-screen menu to choose operations
5. Press `q` to quite the program

## Menu Options
```
[1] Load an image
[2] Display an image
[3] Control Contrast
[4] Control Brightness
[5] Convert a color space to another color space
[6] Resize an image
[7] Crop an image
[8] Annotate an image
[9] Save an image
[10] Save an image to another format
```
## Project Current Structure
- `basic_image_tool.py` - main CLI interface
- `image_IO.py` - image loading with dynamic file browser
- `image_resize_utils.py` - modular resize functions

> The code is being refactored incrementally to support futures like batch processing, filters, and GUI.

## Future Improvements
- Add common image filters (blur, sharpen, edge detection)
- Implement histogram equalization
- Support batch processing
- Replace hardcoded paths with user-configurable directions
- Add channel-and region-specific adjustments
- Build a GUI version
- Implement undo/redo and before/after preview

## Learning Resources
This project is inspired by following the curriculum of:
> **Course**: Mastering OpenCV with Python  
> **Platform**: [OpenCV University](https://opencv.org/university/)  
> **Current Progress**: Completed Modules 1 - 3, Now exploring Module 4 - Video Processing and Analysis in a new project

## Images Credits
All sample images used in this project are from [Pexels.com](https://www.pexels.com/). They are used for educational and 
non-commercial purpose only. Check out the `CREDITS.md` file to know more about each image.

## Project Status
**Active Development** - Core image operations are implemented and modularized
**Next** - Building a video processing tool to apply Module 4 concepts.

Last Update: Tuesday, November 04, 2025
