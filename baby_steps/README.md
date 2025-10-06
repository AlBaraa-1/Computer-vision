# Baby Steps: Basic OpenCV Examples

This folder contains simple starter scripts to get familiar with basic image and video I/O operations using OpenCV.

## Files

- `io_img.py` – Load an image (`test.png`), optionally save a copy as `output.png`, and display it.
- `crop.py` – Load `test.png` and show a cropped region of the image.
- `resizing.py` – Load `test.png`, print original shape, resize it to one‑third of original hard‑coded dimensions, and display both.
- `io_vidoe.py` – (typo in name kept) Play back frames from `test.mp4` until it ends or you press `q`.
- `io_webcam.py` – Open your default webcam (index 0) and show the live feed until you press `q`.
- `test.py` – Currently empty placeholder for experimentation.

## Prerequisites

Install OpenCV for Python:

```bash
pip install opencv-python
```

Ensure you have `test.png` (and optionally `test.mp4`) either copied into this `baby_steps` folder or run scripts from a directory where those files exist (the code uses relative `./test.png` and `./test.mp4`).

## How to Run

From inside the `Computer-vision` repository root:

```bash
cd baby_steps
python io_img.py
```

Press `q` in a window showing video/webcam to quit those loops.

## Next Ideas

- Add error handling when files/webcam are not found.
- Normalize path handling so assets can live in a shared `assets/` folder.
- Refactor repeated image path code into a helper.
