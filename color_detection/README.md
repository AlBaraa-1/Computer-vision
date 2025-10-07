# Color Detection with OpenCV

This project demonstrates real-time color detection using OpenCV and Python. The main focus is on detecting yellow objects in a video stream from your webcam, drawing bounding boxes around detected areas, and displaying both the original frame and the color mask.

## Features
- Real-time video capture from webcam
- HSV color space conversion for robust color detection
- Dynamic mask creation for a target color (yellow by default)
- Bounding box visualization for detected regions
- Modular code for easy extension to other colors

## Project Structure

```
color_detection/
  main.py           # Main application for color detection
  util.py           # Utility functions (color limits)
  requirements.txt  # Python dependencies
```

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/AlBaraa-1/Computer-vision.git
   cd Computer-vision/color_detection
   ```
2. Install dependencies (preferably in a virtual environment):
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the main script to start color detection:
```bash
python main.py
```
Press `q` to exit the application.

## How It Works
1. Captures video from your webcam.
2. Converts each frame to HSV color space.
3. Applies a mask to isolate the target color (yellow).
4. Finds the bounding box of the detected area and draws it on the frame.
5. Displays both the original frame and the mask in real time.

## Customization
- To detect a different color, change the `yellow` variable in `main.py` to the desired BGR color value.
- The detection range can be adjusted in `util.py` by modifying the `get_limits` function.

## Requirements
- Python 3.7+
- OpenCV
- NumPy
- Pillow

All dependencies are listed in `requirements.txt`.

## License
This project is for educational and experimental purposes.

---
*Developed by AlBaraa*
