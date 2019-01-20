import os
import subprocess
import mouseControl
import logic

c,s = logic.getShortCut('2')
mouseControl.handleShortcut(c,s)

'''
command = "C:\umlet-standalone-14.3.0\Umlet\Umlet.exe"
#os.system(command)
subprocess.Popen([command])
'''