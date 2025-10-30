# Basic Image Tool - Mini Image Processing App (OpenCV + Python)

## Project Overview
**Basic Image Tool** is a beginner-friendly image processing project built with Python and OpenCV. It provides a simple
command-line interface that allows users to perform essential image operations, from loading and editing images to saving
them in different formats.

This project was developed as a practical application of the **Mastering OpenCV with Python** course from OpenCV University,
evolving through learning modules as new concepts are learned and applied.

## Project Goals
Create a hands-on tool that helps beginners:
- Load and display images with propper window controls
- Apply basic operations such as:
  - Convert color / grayscale
  - Adjust brightness and contrast
  - Crop and resize
  - Annotate (draw shapes, add text)
  - Save images or export to a new formate (e.g., .jpg ➡️ .png)
- Understand how OpenCV handles image data, color spaces, pixel operations, and file I/O.

## Project Evolution

### Module 1: Getting Started with Images (Foundation)
Initial version focused on fundamental image operations:
- Loading, displaying, and saving images
- Color space conversions (BGR, Grayscale, HSV, LAB)
- Basic resizing with aspect ratio preservation
- Center cropping
- Text annotation
- Format conversion

**Key Concepts**: Image I/O, NumPy arrays, color spaces, basic transformations

### Module 2: Basic Image Manipulation (Current)
After completing Module 2, the tool expanded to include:
- Brightness Control: Adjust image brightness using `cv2.add()` and `cv2.subtract()`
  - Understanding additive pixel operations
  - Proper saturation handling (0-255 clipping)
- Contrast Control: Modify image contrast using `cv2.multiply()`
  - Understanding multiplicative scaling
  - Proportional vs uniform pixel adjustments
- Improved Display Management: Better window control with `cv2.namedWindow()` and `cv2.WINDOW_NORMAL`
  - Resizable windows
  - Controlled display sizes

**Key Learning**: Understanding the fundamental difference between additive operations (brightness - uniform change) and
multiplicative operations (contrast - proportional change), and why OpenCV's arithmetic functions handle saturation better
than Pythons's native operators.

## Concepts Demonstrated
### Module 1 Concepts
- Image reading & writing: `cv2.imread()`, `cv2.imwrite()`
- Color space conversion: `cv2.cvtColor()`
- Resizing: `cv2.resize()`
- Cropping: Numpy array slicing
- Drawing and annotation: `cv2.putText()`, `cv2.rectangle()`, `cv2.circle()`
- Format conversion: `.jpg` ➡️ `.png`

### Module 2 Concepts
- Brightness adjustment: `cv2.add()`, `cv2.subtract()`
- Contrast adjustment: `cv2.multiply()`
- Saturation handling and pixels value clipping
- Understanding scalar vs. matrix operations

## Tech Stack
- Programming Langauge: Python 3.xx
- Libraries: OpenCV (cv2), NumPy
- Platform: Command Line (CLI)
- Future: GUI version with Tkinter, PyQt or PySide

## Features
- Load images from a curated sample collection
- Display images with controlled window sizing
- Convert between multiple color spaces
- Adjust image brightness
- Adjust image contrast
- Resize images to Instagram vertical post format (1080x1350)
- Center crop with 80% retention
- Add text annotations
- Save processed images
- Export to different formats

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

## Future Improvements
- [x] Brightness and contrast controls
- [x] Improved display window management
- Add image filters and effects (blur, sharpen, edge detection)
- Implement histogram equalization
- Add batch processing for multiple images
- Integrate file explorer for easier navigation
- Channel-specific adjustments (suing tuples for pre-channel control)
- Region-specific adjustments (using matrices for spatial control)
- Build GUI interface
- Add before/after comparison view
- Implement undo/redo functionality

## Learning Resources
This project is inspired by following the curriculum of:
> **Course**: Mastering OpenCV with Python  
> **Platform**: [OpenCV University](https://opencv.org/university/)  
> **Current Progress**: Module 2 - Basic Image Manipulation

## Images Credits
All sample images used in this project are from [Pexels.com](https://www.pexels.com/). They are used for educational and 
non-commercial purpose only. Check out the `CREDITS.md` file to know more about each image.

## Project Status
**Active Development** - Currently implementing Module 2 concepts and preparing for Module 3.

Last Update: Wednesday, October 22, 2025


# Testing Git settings