import threading
import os

def run_script(script):
    os.system(f'python {script}')

file1 = 'sensors.py'
file2 = 'sendMessage.py'
file3 = 'recieve.py'


if __name__ == '__main__':
    with open("state.txt", "w") as f:
            f.write("-1")
    # Create threads
    thread1 = threading.Thread(target=run_script, args=(file1,))
    thread2 = threading.Thread(target=run_script, args=(file2,))
    thread3 = threading.Thread(target=run_script, args=(file3,))

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    thread3.join()