import serial
import time
 
run = True
speed = 240
ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
ser.flush()
while run:

    time.sleep(3)
    ser.write(b"4-240-4000-1\n")
    print("RUNNING MOTOR 2 FORWARD")
    time.sleep(5)

    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)

    time.sleep(3)
    ser.write(b"4-240-4000-2\n")
    print("RUNNING MOTOR 2 BACKWARD")
    time.sleep(5)

    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
 
    ser.write(b"2-240-4000-2\n")
    print("RUNNING MOTOR 2 BACKWARD")
    time.sleep(5)

    if ser.in_waiting > 0:
       line = ser.readline().decode('utf-8').rstrip()
       print(line)

    ser.write(b"3-240-4000-1\n")
    print("RUNNING MOTOR 3 FORWARD")
    time.sleep(5)

    if ser.in_waiting > 0:
       line = ser.readline().decode('utf-8').rstrip()
       print(line)

    ser.write(b"4-240-4000-2\n")
    print("RUNNING MOTOR 4 BACKWARD")
    time.sleep(3)

    if ser.in_waiting > 0:
       line = ser.readline().decode('utf-8').rstrip()
       print(line)
    ser.write(b"4-200-4000\n")
    print("RUNNING MOTOR 4")
    time.sleep(5)
