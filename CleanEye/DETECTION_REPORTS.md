# 📋 CleanEye Detection Reports

## Overview
The `detect_report.py` script generates comprehensive **before/after** detection reports with unique IDs, statistics, and severity levels.

---

## 🚀 Quick Start

### Basic Usage
```bash
python code/detect_report.py media/garbage_5.jpg
```

### With Options
```bash
python code/detect_report.py media/garbage_1.jpg --conf 0.3 --model Weights/best.pt
```

---

## 📊 Report Components

### 1. **Unique Report ID**
Each report gets a unique identifier:
```
CLN-20251104-120709-231499D4
│   │        │      └── Random UUID (8 chars)
│   │        └────────── Time (HHMMSS)
│   └─────────────────── Date (YYYYMMDD)
└─────────────────────── CleanEye prefix
```

### 2. **Before/After Images**
- **before_[filename].jpg** - Original image
- **after_[filename].jpg** - Annotated with detections

### 3. **Status Levels**

| Waste Items | Status | Severity | Cleanliness Score |
|-------------|--------|----------|-------------------|
| 0 items | ✅ CLEAN | NONE | 100/100 |
| 1-3 items | ⚠️ LOW | MINOR | 70-90/100 |
| 4-7 items | ⚠️ MODERATE | MEDIUM | 30-60/100 |
| 8+ items | 🚨 HIGH | CRITICAL | 0-20/100 |

### 4. **Report Files**

Each report generates:
- `before_[image].jpg` - Original image
- `after_[image].jpg` - Annotated image
- `report_[ID].json` - Machine-readable data
- `report_[ID].txt` - Human-readable summary

---

## 📁 Report Structure

```
outputs/reports/CLN-20251104-120709-231499D4/
├── before_garbage_5.jpg
├── after_garbage_5.jpg
├── report_CLN-20251104-120709-231499D4.json
└── report_CLN-20251104-120709-231499D4.txt
```

---

## 📄 JSON Report Format

```json
{
  "report_id": "CLN-20251104-120709-231499D4",
  "timestamp": "2025-11-04 12:07:09",
  "image": {
    "original": "media/garbage_5.jpg",
    "before": "outputs/reports/.../before_garbage_5.jpg",
    "after": "outputs/reports/.../after_garbage_5.jpg",
    "size": {"width": 720, "height": 540}
  },
  "detection": {
    "total_items": 6,
    "status": "MODERATE",
    "severity": "MEDIUM",
    "cleanliness_score": 40,
    "confidence_threshold": 0.25
  },
  "statistics": {
    "class_counts": {"garbage": 6},
    "detections": [
      {
        "label": "garbage",
        "confidence": 0.644,
        "bbox": [x1, y1, x2, y2]
      }
    ]
  },
  "model": {
    "path": "Weights/best.pt",
    "type": "YOLOv8"
  }
}
```

---

## 🎯 Example Output

### Terminal Output:
```
================================================================================
📋 CLEANEYE DETECTION REPORT
================================================================================
Report ID: CLN-20251104-120709-231499D4
Timestamp: 2025-11-04 12:07:09
Image: garbage_5.jpg
================================================================================

📸 BEFORE DETECTION:
   Status: Analyzing image for waste...
   Image Size: 720x540 pixels
   Saved: before_garbage_5.jpg

🔍 RUNNING AI DETECTION...

🎯 AFTER DETECTION:
   Status: Detection complete!
   Saved: after_garbage_5.jpg

================================================================================
📊 DETECTION STATISTICS
================================================================================
⚠️  Status: MODERATE - Found 6 waste item(s)

Total Waste Items: 6
Severity Level: MEDIUM
Cleanliness Score: 40/100

🗑️  Breakdown by Type:
   • garbage: 6 items (100.0%)

📋 Detected Objects:
   1. garbage - Confidence: 64.4%
   2. garbage - Confidence: 62.9%
   3. garbage - Confidence: 52.0%
   4. garbage - Confidence: 40.4%
   5. garbage - Confidence: 40.4%
   6. garbage - Confidence: 32.9%
```

---

## 🎪 Use Cases for ADIPEC Demo

### 1. **Booth Demonstration**
```bash
# Show visitors before/after comparison
python code/detect_report.py visitor_photo.jpg
```

### 2. **Area Assessment**
```bash
# Check cleanliness of different zones
python code/detect_report.py zone_a.jpg
python code/detect_report.py zone_b.jpg
python code/detect_report.py zone_c.jpg
```

### 3. **Progress Tracking**
```bash
# Before cleanup
python code/detect_report.py area_before.jpg

# After cleanup
python code/detect_report.py area_after.jpg

# Compare report IDs and scores
```

---

## 📊 Cleanliness Score Calculation

```
Score = max(0, 100 - (waste_items × 10))
```

**Examples:**
- 0 items = 100/100 (Perfect!)
- 3 items = 70/100 (Good)
- 6 items = 40/100 (Needs attention)
- 10+ items = 0/100 (Critical)

---

## 💡 Tips

1. **Batch Processing**: Use wildcards to process multiple images
   ```bash
   for file in media/*.jpg; do python code/detect_report.py "$file"; done
   ```

2. **Archive Reports**: Reports are saved with timestamps - they never overwrite

3. **Share Results**: Send JSON files to dashboard or database

4. **Print Reports**: Use TXT files for hard copy printouts

---

## 🔧 Command-Line Options

| Option | Default | Description |
|--------|---------|-------------|
| `image` | Required | Path to image file |
| `--model` | `Weights/best.pt` | Model weights path |
| `--conf` | `0.25` | Confidence threshold (0.1-0.9) |

---

## 📈 Integration Ideas

### With Streamlit App:
- Upload image → Generate report → Display before/after
- Show report ID for tracking
- Export PDF summary

### With Database:
- Store report JSON in database
- Track cleanliness over time
- Generate area heatmaps

### With Mobile App:
- Scan QR code with report ID
- View full report online
- Track cleanup progress

---

**Built for ADIPEC 2025 - Making Abu Dhabi Cleaner! 🌍♻️**
