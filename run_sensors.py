import cv2
import numpy as np
import asyncio
import signal

cam = cv2.VideoCapture(0)

cv2.namedWindow("Detection")

def monitor_area_change(frame, prev_gray, area, min_change=100, name="Change", value=0):
    x, y, w, h = area
    monitored_area = frame[y:y+h, x:x+w]
    gray = cv2.cvtColor(monitored_area, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    if prev_gray is None:
        return gray, 0
    else:
        diff = cv2.absdiff(prev_gray, gray)
        change_value = round(np.sum(diff) / (10000))
        prev_gray = gray

        if change_value > min_change:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'{name.capitalize()}: {change_value}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            with open("state.txt", "w") as f:
                f.write(str(value))

        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'{name}: {change_value}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        return gray

def detect_and_mark_objects(frame, prev_gray, area, min_contour_area=500, threshold_value=25):
    x, y, w, h = area
    monitored_area = frame[y:y + h, x:x + w]
    gray = cv2.cvtColor(monitored_area, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    if prev_gray is None:
        return gray
    else:
        diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(diff, threshold_value, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > min_contour_area:  # Minimum contour area to be considered a foreign object
                (contour_x, contour_y, contour_w, contour_h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x + contour_x, y + contour_y), (x + contour_x + contour_w, y + contour_y + contour_h), (0, 0, 255), 2)

        return gray


if __name__ == "__main__":
    prev_gray = [0, 0, 0, 0]
    monitor_area = [(0, 100, 200, 200), (200, 100, 200, 200), (400, 100, 200, 200)]
    min_change = [50, 50, 100]
    prev_gray_objects = None
    big_monitor_area = [0, 0, 800, 600]

    while True:
        #inside infinity loop
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

        if ret:
            prev_gray[0] = monitor_area_change(frame, prev_gray[0], monitor_area[0], min_change[0], "change", 1)
            prev_gray[1] = monitor_area_change(frame, prev_gray[1], monitor_area[1], min_change[1], "change", 2)
            prev_gray[2] = monitor_area_change(frame, prev_gray[2], monitor_area[2], min_change[2], "change", 3)
            prev_gray_objects = detect_and_mark_objects(frame, prev_gray_objects, big_monitor_area, 500, 50)


            
        
        cv2.imshow("Detection", frame)



    cam.release()
    cv2.destroyAllWindows()

