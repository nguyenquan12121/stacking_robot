import serial
import time

def send_command(command, speed, duration, direction):
   delay = 3 
   ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
   ser.flush()
   print(f"waiting for {delay}")
   time.sleep(delay)
   ser.write(str.encode(f"{command}-{speed}-{duration}-{direction}\n"))
   if (command == 4): # conveyor active
      # write to send.txt
      
      with open("send.txt", "w") as f:
         f.write("")
   
   elif (command == 2): # elevator 2
      with open("send.txt", "w") as f:
         f.write("elevator 2")
   
   elif (command == 3): # pusher 3
      with open("send.txt", "w") as f:
         f.write("pusher 3")

   print(f"Sending command: {command}-{speed}-{duration}-{direction}")

   if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').rstrip()
      print(line)
