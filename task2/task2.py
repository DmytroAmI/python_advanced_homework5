import threading
import os
import time


def find_text(text, filename):
    """Find text in file and sets the event"""
    try:
        with open(filename, 'r') as f:
            result = f.read()
            if text in result:
                print("Text found")
                product.set()
            else:
                time.sleep(5)
    except FileNotFoundError:
        print("File not found")
        time.sleep(5)


def remove_file(filename):
    """Wait and remove file"""
    product.wait()
    if os.path.exists(filename):
        os.remove(filename)
        print("File removed")
    else:
        print("The file does not exist")


product = threading.Event()

task1 = threading.Thread(target=find_text("wow!", "data.txt"))
task2 = threading.Thread(target=remove_file("data.txt"))

task1.start()
task2.start()

task1.join()
task2.join()
