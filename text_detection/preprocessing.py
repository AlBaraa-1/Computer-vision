"""
Preprocessing functions to improve OCR accuracy
Includes various image enhancement techniques
"""
import cv2
import numpy as np


def convert_to_grayscale(img):
    """Convert image to grayscale"""
    if len(img.shape) == 3:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def apply_thresholding(img, method='otsu'):
    """
    Apply thresholding to image
    
    Methods:
        - 'otsu': Otsu's automatic thresholding
        - 'adaptive': Adaptive thresholding
        - 'binary': Simple binary thresholding
    """
    gray = convert_to_grayscale(img)
    
    if method == 'otsu':
        # Otsu's thresholding - automatic threshold selection
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    elif method == 'adaptive':
        # Adaptive thresholding - good for varying lighting
        thresh = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 11, 2
        )
    
    elif method == 'binary':
        # Simple binary thresholding
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    else:
        thresh = gray
    
    return thresh


def remove_noise(img, method='median'):
    """
    Remove noise from image
    
    Methods:
        - 'median': Median blur (good for salt-and-pepper noise)
        - 'gaussian': Gaussian blur (general smoothing)
        - 'bilateral': Bilateral filter (preserves edges)
    """
    if method == 'median':
        return cv2.medianBlur(img, 3)
    
    elif method == 'gaussian':
        return cv2.GaussianBlur(img, (5, 5), 0)
    
    elif method == 'bilateral':
        return cv2.bilateralFilter(img, 9, 75, 75)
    
    return img


def dilate_text(img, kernel_size=(1, 1)):
    """Dilate text to make it thicker"""
    kernel = np.ones(kernel_size, np.uint8)
    return cv2.dilate(img, kernel, iterations=1)


def erode_text(img, kernel_size=(1, 1)):
    """Erode text to make it thinner"""
    kernel = np.ones(kernel_size, np.uint8)
    return cv2.erode(img, kernel, iterations=1)


def invert_image(img):
    """Invert image colors (useful if text is white on black)"""
    return cv2.bitwise_not(img)


def enhance_contrast(img):
    """Enhance image contrast using CLAHE"""
    gray = convert_to_grayscale(img)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(gray)


def resize_image(img, scale=2.0):
    """
    Resize image for better OCR
    Larger images often work better with Tesseract
    """
    height, width = img.shape[:2]
    new_width = int(width * scale)
    new_height = int(height * scale)
    return cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)


def add_border(img, border_size=10, color=255):
    """Add white border around image"""
    return cv2.copyMakeBorder(
        img, border_size, border_size, border_size, border_size,
        cv2.BORDER_CONSTANT, value=color
    )


def preprocess_pipeline(img, config='default'):
    """
    Complete preprocessing pipeline
    
    Configs:
        - 'default': Standard preprocessing
        - 'aggressive': More aggressive preprocessing
        - 'light': Light preprocessing
        - 'custom': Custom pipeline
    """
    if config == 'default':
        # Standard pipeline
        processed = convert_to_grayscale(img)
        processed = remove_noise(processed, 'median')
        processed = apply_thresholding(processed, 'otsu')
        processed = add_border(processed, 10)
        
    elif config == 'aggressive':
        # Aggressive preprocessing
        processed = convert_to_grayscale(img)
        processed = enhance_contrast(processed)
        processed = remove_noise(processed, 'bilateral')
        processed = apply_thresholding(processed, 'adaptive')
        processed = dilate_text(processed, (2, 2))
        processed = add_border(processed, 15)
        
    elif config == 'light':
        # Light preprocessing
        processed = convert_to_grayscale(img)
        processed = apply_thresholding(processed, 'otsu')
        
    elif config == 'upscale':
        # Upscale and process
        processed = resize_image(img, scale=3.0)
        processed = convert_to_grayscale(processed)
        processed = remove_noise(processed, 'median')
        processed = apply_thresholding(processed, 'otsu')
        processed = add_border(processed, 20)
    
    else:
        # No preprocessing
        processed = img
    
    return processed


def preprocess_for_ocr(img, show_steps=False):
    """
    Optimized preprocessing for OCR
    Returns preprocessed image ready for Tesseract
    """
    steps = {}
    
    # Step 1: Convert to grayscale
    gray = convert_to_grayscale(img)
    if show_steps:
        steps['1_grayscale'] = gray.copy()
    
    # Step 2: Upscale image (Tesseract works better with larger images)
    upscaled = resize_image(gray, scale=2.5)
    if show_steps:
        steps['2_upscaled'] = upscaled.copy()
    
    # Step 3: Remove noise
    denoised = remove_noise(upscaled, 'bilateral')
    if show_steps:
        steps['3_denoised'] = denoised.copy()
    
    # Step 4: Apply thresholding
    thresh = apply_thresholding(denoised, 'otsu')
    if show_steps:
        steps['4_threshold'] = thresh.copy()
    
    # Step 5: Add border
    bordered = add_border(thresh, 20)
    if show_steps:
        steps['5_bordered'] = bordered.copy()
    
    if show_steps:
        return bordered, steps
    
    return bordered
