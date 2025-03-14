import os
import cv2
import argparse
import numpy as np
from scipy.ndimage import label
import multiprocessing

# Enable optimized OpenCV functions
cv2.setUseOptimized(True)
cv2.setNumThreads(multiprocessing.cpu_count())

def load_images(images_path: str) -> list[str]:
    """Load paths of supported images from a directory."""
    supported_formats = ['.jpg', '.jpeg', '.png']
    return [
        os.path.join(images_path, filename)
        for filename in os.listdir(images_path)
        if os.path.splitext(filename)[1].lower() in supported_formats
    ]

def preprocess_image(image_path: str) -> tuple[np.ndarray, np.ndarray]:
    """Preprocess an image by converting to grayscale, reducing noise, and applying threshold."""
    cv2_image = cv2.imread(image_path)
    if cv2_image is None:
        raise ValueError(f"Failed to read images from: {image_path}")

    grayscale_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    noise_reduced_image = cv2.fastNlMeansDenoising(grayscale_image)
    _, threshold_image = cv2.threshold(noise_reduced_image, 200, 255, cv2.THRESH_BINARY_INV)
    return cv2_image, threshold_image

def extract_components(threshold_image: np.ndarray) -> tuple[np.ndarray, int]:
    """Find connected components in a threshold image."""
    labeled, num_features = label(threshold_image)
    return labeled, num_features

def save_cropped_components(cv2_image: np.ndarray, labeled: np.ndarray, num_features: int, output_location: str,
                            image_path: str, padding: int = 10) -> int:
    """Save cropped components as separate images."""
    image_height, image_width = cv2_image.shape[:2]
    min_width = image_width * 0.1
    min_height = image_height * 0.1

    extracted_count = 0
    for component in range(1, num_features + 1):
        coords = np.argwhere(labeled == component)
        y_min, x_min = coords.min(axis=0)
        y_max, x_max = coords.max(axis=0)

        box_width = x_max - x_min + 1
        box_height = y_max - y_min + 1

        if box_width < min_width or box_height < min_height:
            continue

        cropped_region = cv2_image[max(0, y_min - padding):min(image_height, y_max + padding + 1),
                         max(0, x_min - padding):min(image_width, x_max + padding + 1)]

        cv2.imwrite(
            f"{output_location}/{os.path.splitext(os.path.basename(image_path))[0]}_cropped_area_{component}.png",
            cropped_region
        )
        extracted_count += 1

    return extracted_count

def process_image(image_path: str, output_location: str) -> int:
    try:
        print(f'Extracting from image: {image_path}')
        cv2_image, threshold_image = preprocess_image(image_path)
        labeled, num_features = extract_components(threshold_image)
        extracted_count = save_cropped_components(cv2_image, labeled, num_features, output_location, image_path)
        return extracted_count
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return 0

def extract_images_parallel(images_path_list: list[str], output_location: str, num_processes: int) -> int:
    with multiprocessing.Pool(processes=num_processes) as pool:
        extracted_counts = pool.starmap(process_image, [(image_path, output_location) for image_path in images_path_list])
    return sum(extracted_counts)

def extract_images(images_path: str) -> dict:
    """Extract components from images in a directory."""
    result = {
        'source_images': 0,
        'extracted_images': 0,
    }

    if not os.path.exists(images_path) or not os.path.isdir(images_path):
        print(f"Invalid directory: {images_path}")
        return result

    images_path_list = load_images(images_path)
    if len(images_path_list) == 0:
        return result
    else:
        result['source_images'] = len(images_path_list)

    print('\nInitiating image extraction...\n')

    output_location = os.path.join(images_path, 'extracted_images')
    if not os.path.exists(output_location):
        os.makedirs(output_location)

    num_processors = multiprocessing.cpu_count()
    extracted_count = extract_images_parallel(images_path_list, output_location, num_processors)
    result['extracted_images'] = extracted_count

    return result

def main():
    parser = argparse.ArgumentParser(description='''Extract components from images in a directory.
    Required argument: -id <image_directory_full_path>''')

    parser.add_argument('-id', required=True, metavar='IMAGES_DIRECTORY', type=str,
                        help='Directory containing images. Example: /path/to/images')

    args = parser.parse_args()

    result = extract_images(args.id)

    if result['source_images'] == 0:
        print('\nNo images found.\nCheck the directory and try again.\n')
        exit(1)

    print(f'\nProcessing concluded. {result["extracted_images"]} '
          f'images extracted from {result["source_images"]} images processed.\n')
    print(f'Extracted images were saved to: {os.path.join(args.id, "extracted_images", "")}')


if __name__ == '__main__':
    main()
