import cv2
import numpy as np
import mediapipe as mp
import time

# Initialize MediaPipe Hand model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Colors: (B, G, R)
colors = [(255, 0, 255), (255, 0, 0), (0, 255, 0), (0, 140, 255), (0, 0, 0)]
color_names = ['Purple', 'Blue', 'Green', 'Orange', 'Eraser']
color_index = 0

# Canvas for drawing
canvas = None

# Variables
prev_x, prev_y = 0, 0
drawing = False

# Open webcam
cap = cv2.VideoCapture(0)

# Toolbar settings
toolbar_height = 60

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Draw toolbar
    for i, color in enumerate(colors):
        x1 = i * w // len(colors)
        x2 = (i + 1) * w // len(colors)
        cv2.rectangle(frame, (x1, 0), (x2, toolbar_height), color, -1)
        cv2.putText(frame, color_names[i], (x1 + 10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255) if color != (255,255,255) else (0,0,0), 2)
    
    # Detect hands
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))
            
            # Index finger tip: 8, Middle finger tip: 12
            x1, y1 = lm_list[8]
            x2, y2 = lm_list[12]
            
            # Check which fingers are up
            fingers = []
            # Thumb
            fingers.append(lm_list[4][0] > lm_list[3][0])
            # Index
            fingers.append(lm_list[8][1] < lm_list[6][1])
            # Middle
            fingers.append(lm_list[12][1] < lm_list[10][1])
            # Ring
            fingers.append(lm_list[16][1] < lm_list[14][1])
            # Pinky
            fingers.append(lm_list[20][1] < lm_list[18][1])

            # Selection mode: Both index and middle fingers up
            if fingers[1] and fingers[2]:
                drawing = False
                prev_x, prev_y = 0, 0
                # If in toolbar area, select color
                if y1 < toolbar_height:
                    color_index = x1 * len(colors) // w
                    color_index = min(max(color_index, 0), len(colors) - 1)  # Clamp to valid range
                    time.sleep(0.3)  # Debounce
                cv2.circle(frame, (x1, y1), 15, colors[color_index], cv2.FILLED)
            # Drawing mode: Only index finger up
            elif fingers[1] and not fingers[2]:
                cv2.circle(frame, (x1, y1), 8, colors[color_index], cv2.FILLED)
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x1, y1
                if color_index == len(colors) - 1:  # Eraser
                    cv2.line(frame, (prev_x, prev_y), (x1, y1), (0,0,0), 30)
                    cv2.line(canvas, (prev_x, prev_y), (x1, y1), (0,0,0), 30)
                else:
                    cv2.line(frame, (prev_x, prev_y), (x1, y1), colors[color_index], 8)
                    cv2.line(canvas, (prev_x, prev_y), (x1, y1), colors[color_index], 8)
                prev_x, prev_y = x1, y1
                drawing = True
            else:
                prev_x, prev_y = 0, 0
                drawing = False
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    else:
        prev_x, prev_y = 0, 0
        drawing = False

    # Merge canvas and frame
    gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray_canvas, 20, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    # Instructions
    cv2.putText(frame, 'Press S to Save, Q to Quit', (10, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2)

    cv2.imshow('Hand Gesture Drawing App', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        filename = f'drawing_{int(time.time())}.png'
        cv2.imwrite(filename, canvas)
        print(f'Saved: {filename}')

cap.release()
cv2.destroyAllWindows() 