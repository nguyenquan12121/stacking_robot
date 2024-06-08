import serial
import time

def send_command(command, speed, duration, direction):
   delay = 3 
   ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
   ser.flush()
   print(f"waiting for {delay}")
   time.sleep(delay)
   ser.write(str.encode(f"{command}-{speed}-{duration}-{direction}\n"))

   print(f"Sending command: {command}-{speed}-{duration}-{direction}")

   if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip()
      print(line)
