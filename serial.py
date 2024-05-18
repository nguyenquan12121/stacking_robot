import serial
import time

def send_command(command, speed, duration, direction):
   ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
   ser.flush()

   ser.write(f"{command}-{speed}-{duration}-{direction}\n".encode())
   print(f"Sending command: {command}-{speed}-{duration}-{direction}")

   if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip()
      print(line)
