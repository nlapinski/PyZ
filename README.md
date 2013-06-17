PyZ
===

Patch to modify GoZ to work over commandport and ssh to communicate between OSX (zbrush) and Linux (maya)

files go /Users/Shared/Pixologic/ for OSX
and in can be loaded as a Maya shelf for Linux (maya)

A network projects folder should be setup ex. /your/network/share/goz_artistname/

This folder must contain ch.sh, a GoZBrush folder, GoZBrush/GoZ_Applicaiton.txt, GoZBrushFromMaya.mel, GoZBrushToMaya.mel

*I need to make a script to set up/configure the system
*public RSA ssh keys are needed for this to work, they can be made via ssh-keygen -t rsa, ssh-add, and then appended to .ssh/authorized_keys (cat id_rsa.pub >> .ssh/authorized_keys)


ZBrush OSX -> Maya Linux:
-----------------------------------
1. Read config, net paths
2. Write file to network
3. Check for open copy of Maya (or launch via ssh)
4. Write GoZ txt files (to network)
5. Maya loads ascii from txt files (command port) (GoZBrushToMaya.app) 

Note:
GoZBrushToMaya.mel is still used and must be available to the linux machine

Maya Linux -> ZBrush OSX:
-----------------------------------
1. Check for open Zbrush
2. Write selected file names to GoZ txt files (network path)
3. Start new helper app via ssh to copy networked files to Zbrush
local obj list (GoZ_ObjectList.txt)
4. chmod maya ascii files to allow ZBrush acess on OSX side
5. Start GoZBrushFromApp.app via ssh to load objs from local GoZ data

This works around the issue of ZBrush needing all files on one local machine


