returnPath =''

import maya.cmds as cmds
try:
    cmds.commandPort(cl=True,n="129.25.140.197:6667")
except:
    print "noport"
finally:
    cmds.commandPort( n="129.25.140.197:6667",stp="python",po=True,nr=True )



