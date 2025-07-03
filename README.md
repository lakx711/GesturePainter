# 🎨 GesturePainter: Hand Gesture Drawing App

Welcome to GesturePainter! This project lets you draw, erase, and switch colors in real-time using only your hand gestures and a webcam. No mouse or touchscreen needed—just your hand and your creativity! ✋🖌️

---

## 🛠️ What You Need
- 💻 A computer with Python 3.7+
- 📷 A working webcam
- 🌐 Internet connection (for installing dependencies)

---

## 📥 Step 1: Download the Project
1. **Clone or Download** this repository to your computer.
   - If using Git:
     ```bash
     git clone <your-repo-url>
     cd <project-folder>
     ```
   - Or download and extract the ZIP, then open the folder in your terminal or command prompt.

---

## 📦 Step 2: Install Dependencies
1. Make sure you are in the project directory (where `requirements.txt` is located).
2. Run:
   ```bash
   pip install -r requirements.txt
   ```
   This will install:
   - 🖼️ OpenCV (for video and drawing)
   - 🤚 MediaPipe (for hand tracking)
   - 🔢 NumPy (for image processing)

---

## 🚀 Step 3: Run the App
1. In your terminal, make sure you are in the folder containing `hand_gesture_drawing_app.py`.
2. Start the app with:
   ```bash
   python hand_gesture_drawing_app.py
   ```
3. Your webcam will turn on, and a window will appear with a color toolbar at the top.

---

## ✨ Step 4: How to Use GesturePainter
- **🖍️ Drawing:**
  - Raise only your index finger. Move it in the air to draw on the screen.
- **🎨 Change Color:**
  - Raise both your index and middle fingers. Hover your index finger over a color in the toolbar at the top to select it. The selected color will be used for drawing.
- **🧽 Eraser:**
  - Select the black color (Eraser) from the toolbar. Now, drawing will erase instead of draw.
- **💾 Save Your Drawing:**
  - Press the `S` key on your keyboard. Your artwork will be saved as a PNG file in the project folder.
- **❌ Quit the App:**
  - Press the `Q` key to exit.

---

## 🆘 Troubleshooting
- **Webcam not working?**
  - Make sure no other application is using the webcam.
  - Check that your webcam drivers are installed and up to date.
  - Try restarting your computer.
- **Hand not detected?**
  - Make sure your hand is visible and well-lit in front of the camera.
  - Try moving your hand slowly at first.
- **App crashes or errors?**
  - Double-check that all dependencies are installed.
  - Make sure you are running the correct Python version (3.7+).

---

## 📁 Project Structure
```
pp/
├── hand_gesture_drawing_app.py   # Main application script
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🙏 Credits
**Created by Lakshit Soni**

Special thanks to KODI PRAKASH SENAPATI sir for guidance in data science and AI.

---

Enjoy creating art with just your hand! If you have questions or want to contribute, feel free to reach out. 😊 
