# GestureVol2.0 🎛️✋

A real-time hand gesture-based volume controller using Python, OpenCV, and MediaPipe.

---

## 🎯 Aim of the Project

To create a fun, touchless, and interactive system that adjusts your system’s volume using **hand gestures** captured from your webcam. This project combines **Computer Vision**, **Hand Tracking**, and **Audio Control** in a smooth, responsive application.

---

## 🛠️ Tech Stack / Dependencies

### 📦 Python Libraries Used:

| Library       | Purpose |
|---------------|---------|
| **OpenCV** (`opencv-python`) | Captures video from the webcam and processes each frame. |
| **MediaPipe** | Detects hand landmarks in real-time with high accuracy. |
| **NumPy** | Used for efficient array handling and mathematical operations. |
| **PyCaw** | A Python library to control system audio on Windows. |
| **Comtypes** | Dependency of PyCaw for Windows audio API interaction. |

---

## 🧩 Installation Steps

1. 🔁 Install Python **3.10.x** (Recommended)
   - https://www.python.org/downloads/release/python-31011/

2. 🐍 Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows

pip install opencv-python mediapipe numpy pycaw comtypes
python main.py

✋ How It Works
The webcam captures your hand.

MediaPipe tracks the hand and gives the positions of your thumb and index fingertips.

The distance between the fingertips controls the system volume.

Close = low volume 🔇

Far = high volume 🔊

A volume bar is displayed on screen for feedback.

GestureVol2.0/
│
├── main.py           # Main application file
├── README.md         # Project documentation
├── requirements.txt  # (Optional) List of dependencies
└── gesturevol-env/   # Your virtual environment (don't push to GitHub)

🤖 Future Ideas
Add a GUI using Tkinter or PyQt

Integrate gesture-based media controls (play/pause)

Add voice prompts for feedback

Multi-hand support

```bash
# requirements.txt
opencv-python
mediapipe
numpy
pycaw
comtypes

py -3.10 -m venv gesturevol-env
gesturevol-env\Scripts\activate
pip install mediapipe opencv-python numpy pycaw comtypes
pip install mediapipe==0.10.0
pip list
Look for:

mediapipe

opencv-python

pycaw

numpy

comtypes
python main.py

