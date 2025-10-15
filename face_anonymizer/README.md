# FaceGuard 🛡️

> AI-powered face anonymization tool for images, videos, and real-time webcam feeds using MediaPipe and OpenCV.

A powerful and easy-to-use face detection and anonymization tool built with MediaPipe and OpenCV. This application automatically detects and blurs faces in images, videos, or real-time webcam feeds to protect privacy.

## 🔧 Tech Stack

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.10-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- **Multiple Input Modes**: Process images, videos, or live webcam feed
- **Accurate Detection**: Utilizes Google's MediaPipe for robust face detection
- **Customizable Blur**: Adjustable blur intensity for different use cases
- **Fast Processing**: Efficient real-time performance
- **User-Friendly CLI**: Easy-to-use command-line interface
- **Automatic Directory Management**: Organized input/output structure

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Command-Line Arguments](#command-line-arguments)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository** (or navigate to the project directory):
```bash
cd Computer-vision/face_anonymizer
```

2. **Install required dependencies**:
```bash
pip install -r requirements.txt
```

## 📖 Usage

FaceGuard supports three different modes: **image**, **video**, and **webcam**.

### Basic Usage

#### Image Mode (Default)
```bash
python face_guard.py --mode image --filePath path/to/image.jpg
```

#### Video Mode
```bash
python face_guard.py --mode video --filePath path/to/video.mp4
```

#### Webcam Mode
```bash
python face_guard.py --mode webcam
```

### Custom Blur Intensity
```bash
python face_guard.py --mode image --filePath input.jpg --blur 50
```

## 💡 Examples

### Example 1: Anonymize a Single Image
```bash
python face_guard.py --mode image --filePath inputs/photo.jpg --blur 30
```
Output automatically saved to `outputs/output.png`

### Example 2: Process a Video File
```bash
python face_guard.py --mode video --filePath inputs/meeting.mp4 --blur 40
```
Output automatically saved to `outputs/output_video.mp4`

### Example 3: Real-time Webcam Anonymization
```bash
python face_guard.py --mode webcam
```
Press `q` to quit the webcam feed.

## ⚙️ Command-Line Arguments

| Argument | Type | Choices | Default | Description |
|----------|------|---------|---------|-------------|
| `--mode` | str | `image`, `video`, `webcam` | `image` | Select input type |
| `--filePath` | str | Any valid path | `inputs/me.jpg` | Path to input file (not required for webcam mode) |
| `--blur` | int | Any positive integer | 20 (image), 35 (video/webcam) | Blur intensity level |

## 📁 Project Structure

```
face_anonymizer/
│
├── face_guard.py          # Main application script
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── inputs/               # Place your input files here
│   └── me.jpg           # Default input image
│
└── outputs/              # Processed files are saved here
    ├── output.png       # Processed image output
    └── output_video.mp4 # Processed video output
```

## 🔍 How It Works

1. **Face Detection**: Uses MediaPipe's Face Detection model to locate faces in the frame
2. **Bounding Box Extraction**: Extracts relative coordinates and converts them to pixel coordinates
3. **Region Blurring**: Applies Gaussian blur to detected face regions
4. **Output Generation**: Saves or displays the anonymized result

### Technical Details

- **Face Detection Model**: MediaPipe Face Detection (model_selection=0 for short-range detection)
- **Detection Confidence**: Minimum threshold of 0.5
- **Blur Algorithm**: OpenCV's blur function with configurable kernel size
- **Video Codec**: MP4V for video output

## 📦 Requirements

```
mediapipe==0.10.14
opencv-python==4.10.0.84
protobuf>=4.25.3,<5.0.0
numpy>=1.24.0,<2.0.0
```

## 🎯 Use Cases

- **Privacy Protection**: Anonymize faces in photos before sharing
- **GDPR Compliance**: Blur faces in surveillance footage
- **Social Media**: Prepare images for public posting
- **Research**: Create anonymized datasets
- **Content Creation**: Protect bystander privacy in videos

## ⚡ Performance Tips

- **Image Mode**: Use lower blur values (15-25) for faster processing
- **Video Mode**: Use higher blur values (30-40) for better anonymization
- **Webcam Mode**: Ensure good lighting for better face detection
- **Batch Processing**: Process multiple files by running the script in a loop

## 🐛 Troubleshooting

### Common Issues

**Issue**: Faces not detected
- **Solution**: Ensure good lighting and face visibility. Adjust `min_detection_confidence` in the code if needed.

**Issue**: Video output not playing
- **Solution**: Try different video codecs or use a media player that supports MP4V codec.

**Issue**: Import errors
- **Solution**: Reinstall dependencies: `pip install -r requirements.txt --upgrade`

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Google MediaPipe](https://mediapipe.dev/) for the face detection model
- [OpenCV](https://opencv.org/) for image processing capabilities
- The open-source community for continuous support

## 📧 Contact

For questions, suggestions, or feedback, please open an issue in the repository.

---

**⭐ If you find this project useful, please consider giving it a star!**
