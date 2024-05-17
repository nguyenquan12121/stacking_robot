 54 import serial
 53 import time
 52
 51 run = True
 50 speed = 240
 49 ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
 48 ser.flush()
 47 while run:
 46
 45     time.sleep(3)
 44     ser.write(b"4-240-4000-1\n")
 43     print("RUNNING MOTOR 2 FORWARD")
 42     time.sleep(5)
 41
 40     if ser.in_waiting > 0:
 39         line = ser.readline().decode('utf-8').rstrip()
 38         print(line)
 37
 36     time.sleep(3)
 35     ser.write(b"4-240-4000-2\n")
 34     print("RUNNING MOTOR 2 BACKWARD")
 33     time.sleep(5)
 32
 31     if ser.in_waiting > 0:
 30         line = ser.readline().decode('utf-8').rstrip()
 29         print(line)
 28
 27 #    ser.write(b"2-240-4000-2\n")
 26 #    print("RUNNING MOTOR 2 BACKWARD")
 25 #    time.sleep(5)
 24 #
 23 #    if ser.in_waiting > 0:
 22 #        line = ser.readline().decode('utf-8').rstrip()
 21 #        print(line)
 20 #
 19 #    ser.write(b"3-240-4000-1\n")
 18 #    print("RUNNING MOTOR 3 FORWARD")
 17 #    time.sleep(5)
 16 #
 15 #    if ser.in_waiting > 0:
 14 #        line = ser.readline().decode('utf-8').rstrip()
 13 #        print(line)
 12 #
 11 #    ser.write(b"4-240-4000-2\n")
 10 #    print("RUNNING MOTOR 4 BACKWARD")
  9 #    time.sleep(3)
  8 #
  7 #    if ser.in_waiting > 0:
  6 #        line = ser.readline().decode('utf-8').rstrip()
  5 #        print(line)
  4 ##    ser.write(b"4-200-4000\n")
  3 #    print("RUNNING MOTOR 4")
  2 #    time.sleep(5)
  1
55  #print("TURNING OFF NOW...")
