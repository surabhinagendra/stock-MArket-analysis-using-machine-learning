import project
import time
import threading
from tkinter import *
#import gui





t = threading.Thread(target=project.bgrun)
t.daemon = True
t.start()

