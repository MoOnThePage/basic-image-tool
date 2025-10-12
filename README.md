# Basic Image Tool - Mini Image Processing App (OpenCV + Python)

## Project Overview
**Basic Image Tool** is a beginner-friendly image process project
built with Python and OpenCV. It provides a simple command-line interface
that allows users to perform essential image operations, from loading and
editing images to saving them in different formats.

This project was developed as a practical application of **Module 1: Getting
Started with Images** from OpenCV University "_Mastering OpenCV with Python_"
course.

## Project Goals
Create a hands-hon tool that helps beginners:
- Load and display images
- Apply basic operations such as:
  - Convert color / grayscale
  - Crop and resize
  - Recolor
  - Annotate (draw shapes, add text)
  - Save images or export to a new formate (e.g., .jpg ➡️ .png)
- Understand how OpenCV handles image data, color spaces, and file I/O.

## Concepts Demonstrated
- Image reading & writing: `cv2.imread()`, `cv2.imwrite()`
- Color space conversion: `cv2.cvtColor()`
- Resizing: `cv2.resize()`
- Cropping: Numpy array slicing
- Drawing and annotation: `cv2.putText()`, `cv2.rectangle()`, `cv2.circle()`
- Format conversion: `.jpg` ➡️ `.png`

## Tech Stack
- Programming Langauge: Python 3.xx
- Libraries: OpenCV (cv2), NumPy
- Platform: Command Line (CLI)
- Future: GUI version with Tkinter, PyQt or PySide

## How to USE
1. Clone the repository
2. Runs the script
3. Follow the on-screen menu to choose operations
4. Press `q` to quite the program

## Future Improvements
- Add a GUI and effects (blur, sharpen, etc.)
- Add batch processing for multiple images
- Integrate file explorer for easer navigation
- Include mdBoo documentation once the project expands

## Images Credits
All sample images used in this project are from [Pexels.com](https://www.pexels.com/).
They are used for educational and non-commercial purpose only.
Check out the `CREDITS.md` file to know more about each image.

## Concept Source
This project is inspired by the lessons from:
> Module 1 - Getting Started with Images
> Course: Mastering OpenCV with Python
> Platform: [OpenCV University](https://opencv.org/university/)