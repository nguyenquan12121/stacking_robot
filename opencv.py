import cv2
import numpy as np
import requests

URL = "http://192.168.178.59"
AWB = True

cap = cv2.VideoCapture(URL + ":81/stream")

def set_resolution(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
            resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")

def set_quality(url: str, value: int=1, verbose: bool=False):
    try:
        if value >= 10 and value <=63:
            requests.get(url + "/control?var=quality&val={}".format(value))
    except:
        print("SET_QUALITY: something went wrong")

def set_awb(url: str, awb: int=1):
    try:
        awb = not awb
        requests.get(url + "/control?var=awb&val={}".format(1 if awb else 0))
    except:
        print("SET_QUALITY: something went wrong")
    return awb

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
                # cv2.rectangle(frame, (x + contour_x, y + contour_y), (x + contour_x + contour_w, y + contour_y + contour_h), (0, 0, 255), 2)

        return gray

if __name__ == '__main__':
    set_resolution(URL, index=8)
    set_quality(URL, value=15)

    prev_gray = [0, 0, 0, 0]
    monitor_area = [(0, 100, 200, 200), (200, 100, 200, 200), (400, 100, 200, 200)]
    min_change = [100, 100, 100]
    prev_gray_objects = None
    big_monitor_area = [0, 0, 800, 600]


    while True:
        if cap.isOpened():
            ret, frame = cap.read()

            if ret:
                prev_gray[0] = monitor_area_change(frame, prev_gray[0], monitor_area[0], min_change[0], "change", 0)
                prev_gray[1] = monitor_area_change(frame, prev_gray[1], monitor_area[1], min_change[1], "change", 1)
                prev_gray[2] = monitor_area_change(frame, prev_gray[2], monitor_area[2], min_change[2], "change", 2)
                prev_gray_objects = detect_and_mark_objects(frame, prev_gray_objects, big_monitor_area, 500, 50)

            cv2.imshow("frame", frame)

            key = cv2.waitKey(1)

    cv2.destroyAllWindows()
    cap.release()