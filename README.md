# Image Extractor

ImageExtractor is a CLI tool that takes a collection of scanned images, each containing multiple individual images, and automatically crops and extracts individual images into a new folder.

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

!

Output (individual cropped images):

| Image 1 | Image 2 | Image 3 |
| ------- | ------- | ------- |
| ! | ! | ! |

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/2009miles/ie.py
   ```
2. Install the required dependencies:
   ```
   cd image_extractor
   pip install -r requirements.txt
   ```

## Usage

1. Run the python script:
    ```
    python ie.py
    ```
2. Follow the directions in the CLI and it *should* work.

**Disclaimer**: *some crops may be slightly off, work in progress*
