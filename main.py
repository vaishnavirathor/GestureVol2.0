import cv2
import numpy as np
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

# MediaPipe hands setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75)
mp_draw = mp.solutions.drawing_utils

# Pycaw (Windows only)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]

# Volume control variables
vol = 0
vol_bar = 400
vol_percent = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip for mirror view
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            if lm_list:
                x1, y1 = lm_list[4]   # Thumb tip
                x2, y2 = lm_list[8]   # Index tip
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                # Draw elements
                cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
                cv2.circle(img, (cx, cy), 8, (0, 255, 0), cv2.FILLED)

                # Distance calculation
                length = math.hypot(x2 - x1, y2 - y1)

                # Volume mapping
                vol = np.interp(length, [30, 200], [min_vol, max_vol])
                vol_bar = np.interp(length, [30, 200], [400, 150])
                vol_percent = np.interp(length, [30, 200], [0, 100])
                volume.SetMasterVolumeLevel(vol, None)

                if length < 35:
                    cv2.circle(img, (cx, cy), 12, (0, 0, 255), cv2.FILLED)

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Volume bar + text
    cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 0), 3)
    cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(vol_percent)} %', (40, 430), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 0, 0), 3)

    # Display
    cv2.imshow("GestureVol2.0", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
