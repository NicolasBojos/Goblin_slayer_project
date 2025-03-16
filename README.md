# 🧌🗡️ OSRS Goblin Bot  

A computer vision bot that detects and attacks goblins in Old School RuneScape (OSRS) using **YOLOv11**. This project focuses on **automating gameplay** by leveraging **real-time object detection**.  

---

## **1️⃣ Annotating Images** 🎯  

To train the bot effectively, we **annotated images** using the **Roboflow app**.  
- **AI-assisted annotations** were used to speed up the process.  
- **After ~17 manual annotations**, the AI was able to annotate the rest of the dataset **automatically**.  

This created a **high-quality dataset** for YOLO training.

---

## **2️⃣ Training YOLO on Annotated Images** 🏋️‍♂️  

We used **YOLOv11n** to train the best model, which will be used for real-time gameplay automation.

### **📌 Steps in Training YOLO:**
1. **Checking available versions** – Choosing the best YOLO version for our setup.  
2. **Downloading the dataset** – Fetching annotated images from Roboflow.  
3. **Splitting the dataset** – Dividing images into training, validation, and test sets.  
4. **Training the model** – Running YOLO training with the best hyperparameters.  
5. **Testing the model** – Evaluating its accuracy in detecting goblins.

---

## **3️⃣ Automating Gameplay – "Make the Game Play Itself"** 🤖  

With our **trained YOLO model**, we can now:  
✅ **Extract game frames in real time** with high speed and efficiency.  
✅ **Run the model on each frame** to detect goblins.  
✅ **Input actions based on detections** – moving the mouse and clicking accurately.  

---

## **⚠️ Windows vs. Linux: A Critical Issue**  

**🔴 PROBLEM:**  
At this point, we realized that **Linux cannot interact with Windows GUI**, meaning we **couldn’t automate mouse clicks** inside RuneLite from our Linux environment.

**🟢 SOLUTION:**  
We had to **switch back to Windows** for full automation.  

🚧 **Current Challenge:** Using VSCode on Windows **disables GPU acceleration** for the local environment.  
🔍 **Workaround:** Exploring ways to enable GPU support while keeping Windows compatibility.

---

## **📌 Next Steps**
- Optimize frame extraction for **real-time processing**.  
- Improve interaction speed for **seamless bot behavior**.  
- Find a way to **enable GPU acceleration** in Windows.  

🚀 **This is just the beginning! More optimizations coming soon!**  


# 🧌 RuneLite Goblin Bot

This is a **computer vision bot** that detects and attacks goblins in RuneLite using **YOLOv11n** and **Win32 screen capture**.  
The bot tracks goblins in real time, allowing you to manually attack by pressing **'E'**.

## **⚡ Features**
✅ **Real-time goblin tracking** using YOLO  
✅ **Press 'E' to attack**, 'Q' to quit  
✅ **Does NOT require the game window to be active**  
✅ **Works without GPU acceleration (CPU-only)**  

---

## **🚀 Setup & Installation**

### **1️⃣ Install Dependencies**
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Bot
```bash
python main.py
```
### 3️⃣ How to Control the Bot

**E**	Attack the nearest goblin
**Q**	Quit the bot


📂 Script Overview
📄 File	🔹 Purpose

main.py	            Starts the bot and loads YOLO
tracking.py	        Handles goblin detection & movement
screen_capture.py	Captures RuneLite’s window using Win32
detection.py	    Runs YOLO detection on captured frames
requirements.txt	Lists dependencies for installation

📌 Script Details

🟢 main.py (Entry Point)
- Loads YOLOv11n model (best.pt)
- Calls delayed_bot_and_tracking(model) from tracking.py
- Run this file to start the bot

🟡 tracking.py (Goblin Tracking & Clicking)
- Captures the RuneLite window
- Runs YOLO detection to find goblins
- Waits for you to press 'E' to attack
- Shows a live tracking window (OpenCV)

🔵 screen_capture.py (Capturing RuneLite’s Window)
- Uses Win32 API to capture RuneLite
- Returns a screenshot as an image for YOLO

🔴 detection.py (YOLO Object Detection)
- Loads YOLOv11n model (best.pt)
- Detects goblins and returns bounding boxes
- Filters goblins with confidence > 20%

⚠️ Notes
- Make sure RuneLite is running before starting the bot
- Check your YOLO model path in main.py
- If detection doesn’t work, check if class ID is correct in detection.py


👾 Troubleshooting
❌ Error: RuneLite window not found
✅ Solution: Make sure the game is open and window name is correct in tracking.py

❌ Bot not clicking?
✅ Solution: Ensure 'E' is pressed and game coordinates are correct

❌ Bounding boxes look weird?
✅ Solution: Check screen_capture.py uses cv2.COLOR_BGRA2BGR


🧌🧌🧌 **Happy botting!** 🎯🎮  

