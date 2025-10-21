# 📝 Simple Text Detection

Extract text from any image using OCR (Optical Character Recognition).

## 🎯 What It Does

Input an image → Get the text from it → Save to file

Simple as that!

## 📁 Files

```
text_detection/
├── main.py              # Main script - run this!
├── preprocessing.py     # Image processing helpers
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## �️ Setup

### 1. Install Tesseract OCR
- **Windows:** Download from [here](https://github.com/UB-Mannheim/tesseract/wiki)
- Install to: `C:\Program Files\Tesseract-OCR`

### 2. Install Python Packages
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install opencv-python pytesseract numpy
```

### 3. Test Installation
```bash
python test_tesseract.py
```

## 🚀 Usage

### Simple - Run and Enter Path
```bash
python main.py
```
Then enter your image path when asked.

### Example
```bash
python main.py
# Enter: inputs/image.png
```

## 📝 Example

**Input Image:** Screenshot with text  
**Output:** Text file with detected text

```
Image: image.png
Size: 869 x 296 pixels

DETECTED TEXT:
Mix - antent - homesick (super slowed)
Mixes are playlists YouTube makes for you

✅ Text saved to: output.txt
```

## 🎓 How It Works

1. **Load Image** - Read the image file
2. **Preprocess** - Convert to grayscale and enhance
3. **OCR** - Extract text using Tesseract
4. **Save** - Write text to output.txt

## 📊 What's Included

- **1 sample image** in `inputs/` folder for testing
- Works with any image format (PNG, JPG, etc.)
- Clean and minimal - perfect for learning!

## 💡 Tips

- Works best with clear, high-contrast images
- Screenshots work great
- Photos might need better lighting
- Larger images = better accuracy

## � Next Steps

Once you understand this basic version, you can:
- Add preprocessing options
- Batch process multiple images
- Add confidence scores
- Try different languages

---

*Simple text detection for learning* 🎓
