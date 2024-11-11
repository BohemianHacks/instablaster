import cv2
import numpy as np

def generate_frame(frame_number):
    # Create a blank image
    image = np.zeros((1080, 1920, 3), dtype=np.uint8)

    # Set background color (adjust as needed)
    image[:] = (255, 255, 255)  # White background

    # Add text (adjust font, size, color, and position as needed)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f"Frame {frame_number}"
    cv2.putText(image, text, (100, 100), font, 2, (0, 0, 0), 2, cv2.LINE_AA)

    return image
