import userInterface
import subprocess

p = subprocess.Popen(['python','serialHandling.py','arg1','arg2'])
interface = userInterface.userInterface()
interface.buildInterface()
interface.mainloop()
p.terminate()