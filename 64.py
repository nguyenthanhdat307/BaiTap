import os.path, time

print("Last modified: %s" % time.ctime(os.path.getmtime("12.py")))

print("Created: %s" % time.ctime(os.path.getctime("12.py")))