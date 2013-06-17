#!/usr/bin/python

import socket
import os
import subprocess
import commands
from subprocess import Popen
import ConfigParser
import time

''' replacement script for GoZBrushToMaya '''

#config
goz_base="/Users/Shared/Pixologic/"

cfg_path=goz_base+"/GoZApps/Maya/GoZ.cfg"
config = ConfigParser.RawConfigParser()
config.read(cfg_path)
goz_cfg=dict(config.items('GoZ'))

goz_linux_path = goz_cfg['goz_linux_path']
maya_ip = goz_cfg['maya_ip']
maya_port = goz_cfg['maya_port']
ssh_port =  goz_cfg['ssh_port']
ssh_user = goz_cfg['ssh_user']

#look for maya
ps = commands.getstatusoutput("ssh -p "+ssh_port+" "+(ssh_user+'@'+maya_ip)+" 'ps aux | grep /usr/autodesk/maya | wc -l'")

if(int(ps[1])<3):
    cmds = ['ssh', '-p', ssh_port, (ssh_user+'@'+maya_ip), 'DISPLAY=:0', '/usr/autodesk/maya2013-x64/bin/maya -command "commandPort -n \\"'+maya_ip+':'+maya_port+'\\" -stp \\"python\\" -po True"']
    maya = Popen(cmds)
    print ' '.join(cmds)
    print 'open maya'
    time.sleep(10)

#goz object list
path = "/Users/Shared/Pixologic/GoZBrush/GoZ_ObjectList.txt"
objList=open(path,"r")

#goz project path

gozp=goz_base+'/GoZBrush/GoZ_ProjectPath.txt'

objList=objList.read().split('\n')

objout=''
for obj in objList:
    obj=obj.replace('/Volumes/Projects/','/media/projects/')
    objout+=obj+'\n'

obj_file_out=open('/Volumes/Projects/goz_default/GoZBrush/GoZ_ObjectList.txt','wb')
obj_file_out.write(objout)
obj_file_out.close()

mayaCMD=''
mayaCMD='import maya.cmds as cmds'
mayaCMD+='\n'
mayaCMD+='import maya.mel as mel'
mayaCMD+='\n'
mayaCMD+='mel.eval(\'source "'+goz_linux_path+'GoZBrushToMaya.mel"\')'
mayaCMD+='\n'
mayaCMD+='print "SENT"'
mayaCMD+='\n'

maya = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
maya.connect((maya_ip,int(maya_port)))
maya.send(mayaCMD)
maya.close()
