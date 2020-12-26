import sys
import os

s = os.path.split(sys.executable)
print(s[0] + "/Library/bin")
#os.startfile(s[0] + "/Library/bin")    apre direttamente la cartella