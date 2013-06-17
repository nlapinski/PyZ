#!/usr/bin/python

import subprocess

ol_src='/Volumes/Projects/goz_default/GoZBrush/GoZ_ObjectList.txt'
op_src='/Volumes/Projects/goz_default/GoZBrush/GoZ_ObjectPath.txt'

op_dst='/Users/Shared/Pixologic/GoZBrush/GoZ_ObjectPath.txt'
ol_dst='/Users/Shared/Pixologic/GoZBrush/GoZ_ObjectList.txt'

linux='/media/projects/'
osx='/Volumes/Projects/'

objlist=open(ol_src).read().replace(linux,osx)
objpath=open(op_src).read().replace(linux,osx)

print objlist
print objpath

open(op_dst,'w').write(objpath)
open(ol_dst,'w').write(objlist)

subprocess.call(['/Users/Shared/Pixologic/GoZBrush/GoZBrushFromApp.app/Contents/MacOS/GoZBrushFromApp'])
