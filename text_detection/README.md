# 📝 Text Detection & OCR Extraction

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![Tesseract](https://img.shields.io/badge/Tesseract-OCR-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**A powerful and easy-to-use text detection tool that extracts text from images using OCR technology**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Advanced](#-advanced-preprocessing)

</div>

---

## 🌟 Features

- ✨ **Simple Interface** - Extract text from images with a single command
- 🎯 **High Accuracy** - Utilizes Tesseract OCR for reliable text recognition
- 🖼️ **Multiple Formats** - Supports PNG, JPG, JPEG, BMP, and more
- 🔧 **Preprocessing** - Advanced image enhancement techniques for better accuracy
- 💾 **Auto-Save** - Automatically saves extracted text to organized output files
- ⚡ **Fast Processing** - Quick text extraction with optimized algorithms
- 🎨 **Clean Output** - Formatted and cleaned text results

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:
- Python 3.7 or higher
- Tesseract OCR installed on your system

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AlBaraa-1/Computer-vision.git
   cd Computer-vision/text_detection
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR**

   **Windows:**
   - Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
   - Install to default location: `C:\Program Files\Tesseract-OCR\`
   - Or update the path in `main.py` to match your installation

   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt-get update
   sudo apt-get install tesseract-ocr
   ```

   **macOS:**
   ```bash
   brew install tesseract
   ```

---

## 💻 Usage

### Basic Text Extraction

Run the main script and provide an image path:

```bash
python main.py
```

When prompted, enter the path to your image:
```
Enter img path: inputs/test1.png
```

### Example Output

```
Extracting text...

DETECTED TEXT:
==============================
Tesseract installer for Windows

Normally we run Tesseract on Debian GNU Linux, but there was also the need for a Windows version.
==============================

Text saved to: outputs/test1.txt
```

---

## 📁 Project Structure

```
text_detection/
│
├── main.py              # Main text extraction script
├── preprocessing.py     # Advanced image preprocessing functions
├── requirements.txt     # Python dependencies
│
├── inputs/             # Place your images here
│   ├── test1.png
│   └── test2.png
│
└── outputs/            # Extracted text files (auto-generated)
    ├── test1.txt
    └── test2.txt
```

---

## 🎯 Examples

### Example 1: Document Text Extraction

**Input Image:**
- Document or screenshot with text

**Output:**
```plaintext
Tesseract installer for Windows

Normally we run Tesseract on Debian GNU Linux...
```

### Example 2: Book Page Extraction

**Input Image:**
- Photo of a book page

**Output:**
```plaintext
It was the best of times, it was the worst
of times, it was the age of wisdom...
```

---

## 🔧 Advanced Preprocessing

The `preprocessing.py` module provides advanced image enhancement techniques to improve OCR accuracy:

### Available Functions

| Function | Description | Use Case |
|----------|-------------|----------|
| `convert_to_grayscale()` | Convert image to grayscale | Simplify image for OCR |
| `apply_thresholding()` | Apply binary thresholding | Enhance text contrast |
| `remove_noise()` | Remove image noise | Clean up noisy images |
| `enhance_contrast()` | Enhance image contrast | Improve text visibility |
| `dilate_text()` | Make text thicker | Enhance thin text |
| `erode_text()` | Make text thinner | Clean up thick text |
| `invert_image()` | Invert colors | White text on black background |
| `resize_image()` | Resize image | Improve small text detection |

### Preprocessing Methods

#### 1. **Thresholding Methods**
- `otsu` - Automatic threshold selection (default)
- `adaptive` - Good for varying lighting conditions
- `binary` - Simple binary thresholding

#### 2. **Noise Removal Methods**
- `median` - Removes salt-and-pepper noise
- `gaussian` - General smoothing
- `bilateral` - Preserves edges while smoothing

### Custom Preprocessing Example

```python
import cv2
from preprocessing import *

# Read image
img = cv2.imread('input.png')

# Apply preprocessing pipeline
img = convert_to_grayscale(img)
img = remove_noise(img, method='median')
img = enhance_contrast(img)
img = apply_thresholding(img, method='otsu')

# Now use with pytesseract
text = pytesseract.image_to_string(img)
```

---

## 🛠️ Customization

### Update Tesseract Path

If Tesseract is installed in a different location, update line 10 in `main.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r'YOUR_TESSERACT_PATH\tesseract.exe'
```

### Configure OCR Language

To detect text in different languages, install language packs and modify the OCR call:

```python
text = pytesseract.image_to_string(img, lang='eng')  # English
```

---

## 📊 Performance Tips

For better OCR accuracy:

1. **Image Quality** - Use high-resolution images (300+ DPI recommended)
2. **Text Size** - Ensure text is clearly readable (resize if needed)
3. **Contrast** - High contrast between text and background works best
4. **Orientation** - Keep text horizontal and properly aligned
5. **Lighting** - Even lighting produces better results
6. **Noise** - Use preprocessing to reduce image noise

---

## 🐛 Troubleshooting

### Common Issues

**Issue:** `TesseractNotFoundError`
- **Solution:** Ensure Tesseract is installed and the path in `main.py` is correct

**Issue:** Poor text detection accuracy
- **Solution:** Try preprocessing the image first (see Advanced Preprocessing)

**Issue:** No text detected
- **Solution:** Check image quality, ensure text is clear and properly oriented

**Issue:** Wrong characters detected
- **Solution:** Use appropriate language pack or try different preprocessing techniques

---

## 📦 Requirements

```
opencv-python >= 4.5.0
pytesseract >= 0.3.8
numpy >= 1.19.0
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - Open source OCR engine
- [OpenCV](https://opencv.org/) - Computer Vision library
- [pytesseract](https://github.com/madmaze/pytesseract) - Python wrapper for Tesseract

---

## 📧 Contact

**Author:** AlBaraa-1  
**Repository:** [Computer-vision](https://github.com/AlBaraa-1/Computer-vision)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ and Python

</div>
