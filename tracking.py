import cv2
import pyautogui
import keyboard
import numpy as np
from PIL import Image
from collections import deque
from screen_capture import capture_runeLite_window
from detection import detect_goblins

# **RuneLite Window Title**
window_name = "RuneLite - <username>"

def delayed_bot_and_tracking(model):
    """Tracks goblins but only clicks when 'E' is pressed."""

    print("✅ Tracking started. Press 'E' to attack. Press 'Q' to exit.")

    cv2.namedWindow("RuneLite - Goblin Tracking", cv2.WINDOW_NORMAL)  # Create OpenCV window
    track_history = deque(maxlen=5)
    last_goblin_position = None

    while True:
        frame, game_region = capture_runeLite_window(window_name)
        if frame is None:
            print("❌ Error: Could not capture RuneLite window.")
            continue

        # **Run YOLO Detection**
        goblins = detect_goblins(frame, model)

        if not goblins:
            print("⚠️ No goblins detected.")
            last_goblin_position = None
            continue  # Skip this frame

        # **Draw Bounding Boxes**
        for box, confidence in goblins:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"Goblin {confidence:.2f}", (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # **Show OpenCV Window**
        cv2.imshow("RuneLite - Goblin Tracking", frame)
        if cv2.getWindowProperty("RuneLite - Goblin Tracking", cv2.WND_PROP_VISIBLE) < 1:
            print("❌ OpenCV window closed. Exiting bot.")
            break

        cv2.waitKey(1)  # Keep OpenCV window responsive

        # **Check for Key Presses**
        if keyboard.is_pressed('q'):
            print("❌ Stopping bot & tracking.")
            break

        # **Find Closest Goblin**
        best_goblin = min(goblins, key=lambda g: g[1])  # Lowest confidence value
        x1, y1, x2, y2 = map(int, best_goblin[0])
        last_goblin_position = (game_region[0] + (x1 + x2) // 2,
                                game_region[1] + (y1 + y2) // 2)

        # **Click only when 'E' is pressed**
        if keyboard.is_pressed('e') and last_goblin_position:
            print(f"🎯 Attacking goblin at {last_goblin_position}...")
            pyautogui.moveTo(*last_goblin_position, duration=np.random.uniform(0.1, 0.2))
            pyautogui.click()
            print("✅ Clicked on goblin.")

    cv2.destroyAllWindows()
    print("✅ Bot & tracking loop exited safely.")
