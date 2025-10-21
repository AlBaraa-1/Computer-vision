"""
Simple Text Detection - Extract text from any image
Just run: python main.py
"""
import cv2
import pytesseract
import os

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text(image_path):
    """Extract text from an image"""

    # Read image
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Could not read image: {image_path}")
        print("Make sure the file path is correct")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to make text clearer
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Extract text using OCR
    print("\nExtracting text...")
    text = pytesseract.image_to_string(threshold)
    
    # Clean up the text
    text = text.strip()
    
    if text:
        print("\nDETECTED TEXT:")
        print("="*30)
        print(text)
        print("="*30)

        # Create outputs folder if it doesn't exist
        os.makedirs("outputs", exist_ok=True)
        
        # Get image filename without extension
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        
        # Save to file in outputs folder with same name as image
        output_file = os.path.join("outputs", f"{image_name}.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"\nText saved to: {output_file}")
        
        return text
    else:
        print("\nNo text detected in the image")
        return None


def main():
    """Main function"""
    
    print("\nSimple Text Detection Tool")
    
    image_path = input("\nEnter img path: ").strip()
    
    # Remove quotes if user copied path with quotes
    image_path = image_path.strip('"').strip("'")
    
    # Check if file exists
    if not os.path.exists(image_path):
        print(f"\nFile not found: {image_path}")
        print(" Please check the path and try again")
        return
    
    # Extract text
    extract_text(image_path)


if __name__ == "__main__":
    main()
