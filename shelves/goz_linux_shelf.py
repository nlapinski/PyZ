import commands
import subprocess
import maya.mel as mel

mel.eval('source "/media/projects/goz_default/GoZBrushFromMaya.mel";')

#set your target osx machine IP, user account, ssh port, and goz
working dir here
commands.getstatusoutput("ssh -X -p 6669 nkl32@129.25.142.68
'/Users/Shared/Pixologic/GoZBrush/GoZBrushFromApp.py'")
subprocess.call(['/media/projects/goz_default/ch.sh'])
