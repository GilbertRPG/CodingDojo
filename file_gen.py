import os
path = "python_intro/fundamentals"
path2 = "python_intro/OOP"

try:
    os.makedirs(path)
    os.makedirs(path2)
except OSError:
    print ("Failed task of %s" % path, path2)
else:
    print ("Successful task of %s" % path, path2)