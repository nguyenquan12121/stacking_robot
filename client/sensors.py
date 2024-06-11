import cv2
import numpy as np
from client import sendMessage

cam = cv2.VideoCapture(0)

cv2.namedWindow("Detection")

def monitor_area_change(prev, frame, prev_gray, area, min_change=100, name="=", value=0):
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
            if prev == 0:
                sendMessage.send_message(str(value))
            prev = 1

        else:
            prev = 0
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'{name}: {change_value}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        return gray, prev

def detect_and_mark_objects(last, frame, prev_gray, area, min_contour_area=500, threshold_value=25):
    x, y, w, h = area
    monitored_area = frame[y:y + h, x:x + w]
    gray = cv2.cvtColor(monitored_area, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    if prev_gray is None:
        return gray, last
    else:
        diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(diff, threshold_value, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        diff_sum = 0
        for contour in contours:
            if cv2.contourArea(contour) > min_contour_area:
                (contour_x, contour_y, contour_w, contour_h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x + contour_x, y + contour_y), (x + contour_x + contour_w, y + contour_y + contour_h), (0, 0, 255), 2)
                diff_sum += cv2.contourArea(contour)

        cv2.putText(frame, f'{diff_sum}', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        if (diff_sum > 20000):
            if (last == 0):
                sendMessage.send_message("3")
            cv2.putText(frame, f'SOMETHING IS BLOCKING', (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 5)
            last = 1
        else:
            last = 0
        return gray, last

if __name__ == "__main__":
    prev_gray = [0, 0]
    monitor_area = [(565 , 205, 55, 55), (280, 185, 55, 70)]
    min_change = [20, 10]
    prev_gray_objects = None
    big_monitor_area = [0, 0, 800, 600]
    prev = [0, 0]
    last = 0

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
        
        if k%256 == 32 or prev_gray_objects is None:
            # SPACE pressed
            prev_gray[0], prev[0] = monitor_area_change(prev[0], frame, prev_gray[0], monitor_area[0], min_change[0], "1:", 1)
            prev_gray[1], prev[1] = monitor_area_change(prev[1], frame, prev_gray[1], monitor_area[1], min_change[1], "2:", 2)
            prev_gray_objects, last = detect_and_mark_objects(last, frame, prev_gray_objects, big_monitor_area, 500, 50)

        elif ret:
            s = 0
            s, prev[0] = monitor_area_change(prev[0], frame, prev_gray[0], monitor_area[0], min_change[0], "1:", 1)
            s, prev[1] = monitor_area_change(prev[1], frame, prev_gray[1], monitor_area[1], min_change[1], "2:", 2)
            s, last = detect_and_mark_objects(last, frame, prev_gray_objects, big_monitor_area, 500, 50)
        
        cv2.imshow("Detection", frame)



    cam.release()
    cv2.destroyAllWindows()

