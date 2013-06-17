#!/usr/bin/python

import socket
import os
import subprocess
import commands
import ConfigParser
import time

#these should be defined if in non standard install locations
#goz_base
#maya_path
#goz_obj_list

'''replacement script for GoZBrushToMaya

Reads config file and creates connection with Maya over command port
Re-writes GoZ_ObjectList.txt with linux paths

'''


def config_goz():
    #config
    goz_base="/Users/Shared/Pixologic/"
    cfg_path=goz_base+"/GoZApps/Maya/GoZ.cfg"
    config = ConfigParser.RawConfigParser()
    config.read(cfg_path)
    goz_cfg=dict(config.items('GoZ'))
    goz_cfg['goz_base']=goz_base
    
    return goz_cfg

def find_maya(ssh_user,ssh_port,maya_ip,maya_port):
    #look for maya

    ps_cmd=['ssh -p',
            (ssh_port),
            (ssh_user+'@'+maya_ip),
            '\'',
            'ps aux',
            '| grep',
            '/usr/autodesk/maya',
            '| wc -l',
            '\'']

    ps_cmd=' '.join(ps_cmd)
    ps = commands.getstatusoutput(ps_cmd)
    
    maya_path = '/usr/autodesk/maya2013-x64/bin/maya -command "commandPort -n \\"'

    if(int(ps[1])<3):
        print 'starting maya....'
        cmds = ['ssh',
                '-p',
                ssh_port,
                (ssh_user+'@'+maya_ip),
                'DISPLAY=:0',
                maya_path+maya_ip+':'+maya_port+'\\" -stp \\"python\\" -po True"']
        
        maya = Popen(cmds)
        print ' '.join(cmds)
        print 'open maya'
        time.sleep(10)
    print 'found maya!'

def parse_goz_objs(goz_base):
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
    print 'updated GoZ_ObjectList'

def send_to_maya(maya_ip,maya_port,goz_linux_path):
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
    print 'loading goz *.ma'

def main():
    print 'init main'
    goz_cfg=config_goz()
    print goz_cfg

    goz_linux_path = goz_cfg['goz_linux_path']
    maya_ip = goz_cfg['maya_ip']
    maya_port = goz_cfg['maya_port']
    ssh_port =  goz_cfg['ssh_port']
    ssh_user = goz_cfg['ssh_user']
    goz_base = goz_cfg['goz_base']

    find_maya(ssh_user,ssh_port,maya_ip,maya_port)
    parse_goz_objs(goz_base)
    send_to_maya(maya_ip,maya_port,goz_linux_path)

if __name__ == '__main__':
    main()
