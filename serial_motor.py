"Script for sending a command to the Arduino to control the motors"
import serial
import time

from serial import SerialException

def send_command(command, speed, duration, direction):
   "Function for sending a command to the Arduino to control the motors"
   delay = 3 
   ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) # Open the serial port
   ser.flush() # Flush the serial port
   print(f"waiting for {delay}")
   time.sleep(delay)
   try:
      ser.write(str.encode(f"{command}-{speed}-{duration}-{direction}\n")) # Send the command to the Arduino
   except:
      raise SerialException

   print(f"Sending command: {command}-{speed}-{duration}-{direction}")

   if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip() # Read the response from the Arduino
      print(line)
