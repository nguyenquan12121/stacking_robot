import pytest
import cv2
import numpy as np
from unittest.mock import MagicMock, patch
from client.sensors import monitor_area_change, detect_and_mark_objects

# Helper function to create a test image
def create_test_image(width, height, color=(0, 0, 0)):
    return np.full((height, width, 3), color, dtype=np.uint8)

# Test the monitor_area_change function
def test_monitor_area_change():
    frame = create_test_image(800, 600, (255, 255, 255))
    area = (100, 100, 50, 50)
    prev_gray = None
    prev = 0
    
    gray, updated_prev = monitor_area_change(prev, frame, prev_gray, area, min_change=10, name="test", value=1)
    assert updated_prev == 0  # No change expected in a blank white image
    assert gray is not None

    frame_with_change = frame.copy()
    cv2.rectangle(frame_with_change, (110, 110), (140, 140), (0, 0, 0), -1)  # Create a black square
    with pytest.raises(Exception):
        gray, updated_prev = monitor_area_change(prev, frame_with_change, gray, area, min_change=10, name="test", value=1)

# Test the detect_and_mark_objects function
def test_detect_and_mark_objects():
    frame = create_test_image(800, 600, (255, 255, 255))
    area = (0, 0, 800, 600)
    prev_gray = None

    gray = detect_and_mark_objects(frame, prev_gray, area, min_contour_area=500, threshold_value=25)
    assert gray is not None

    frame_with_objects = frame.copy()
    cv2.rectangle(frame_with_objects, (300, 300), (400, 400), (0, 0, 0), -1)  # Add a black square

    gray = detect_and_mark_objects(frame_with_objects, gray, area, min_contour_area=500, threshold_value=25)
    assert gray is not None

