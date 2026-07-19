import logging
import cv2
import threading

logger = logging.getLogger(__name__)

latest_frame = None
capture_active = threading.Event()


def _find_camera(max_index: int = 10) -> cv2.VideoCapture | None:
    for index in range(max_index):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            ok, _ = cap.read()
            if ok:
                logger.info("Camera found at index %d", index)
                return cap
            cap.release()
    logger.warning("No camera found after scanning %d indices", max_index)
    return None


_camera = _find_camera()


def capture_frames():
    global latest_frame
    if _camera is None:
        return
    while True:
        capture_active.wait()
        ok, frame = _camera.read()
        if not ok:
            continue
        ret, buf = cv2.imencode('.jpg', frame)
        if ret:
            latest_frame = buf.tobytes()


threading.Thread(target=capture_frames, daemon=True).start()
