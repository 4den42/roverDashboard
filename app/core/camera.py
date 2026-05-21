import cv2
import threading

camera = cv2.VideoCapture(0)

latest_frame = None

def capture_frames():
    global latest_frame

    while True:
        success, frame = camera.read()
        if not success:
            continue

        # encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        if ret:
            latest_frame = buffer.tobytes()

threading.Thread(target=capture_frames, daemon=True).start()
