# Image Extractor (ie)

Image Extractor is a CLI tool that takes a collection of scanned images, each containing multiple individual images, and automatically crops and extracts individual images into a new folder.

## Features

- Batch processing of scanned image files
- Automatic detection and cropping of individual images
- Creates a new folder with the extracted individual images (on the same directory)
- Supports common image formats (JPEG, JPG, PNG)

## Usage

1. Place your scanned images (e.g., JPEG, JPG, PNG) in directory of your choice.
2. Run the ie tool and follow the prompts (providing the input folder path).
3. The tool will create a new output folder, in the same directory, with the individual cropped images.

## Example

Input (scanned image containing multiple individual images):

<p align="center">
   <img src="https://github.com/user-attachments/assets/27c7fd9b-93c8-4311-87fe-082dfe64d178" width=30%>
</p>

Output (individual cropped images):

| Image 1 | Image 2 | Image 3 | Image 4 |
| ------- | ------- | ------- | ------- |
| ![Scan21082024173106_001_cropped_area_1](https://github.com/user-attachments/assets/72bb975b-227b-4b0c-84d5-4393d90bd941) | ![Scan21082024173106_001_cropped_area_43](https://github.com/user-attachments/assets/1f12e801-0b18-4d85-816a-bba5979a125c) | ![Scan21082024173106_001_cropped_area_179](https://github.com/user-attachments/assets/f967c2e2-3f9a-4d02-b138-210d7e04f8a2) | ![Scan21082024173106_001_cropped_area_180](https://github.com/user-attachments/assets/a0e5e630-da25-4e48-9e4b-4653d1f1ccb6) |

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/2009miles/ie.git
   ```
2. Install the required dependencies:
   (in the corresponding directory)
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the python script:
    ```
    python ie.py
    ```
2. Follow the directions in the CLI.
3. Wait for processing.
4. In the folder where your original images were, you'll find a new folder with the cropped pictures.

**Disclaimer**: *some crops may be off, work in progress*
