PyZ
===

Patch to modify GoZ to work over commandport and ssh to communicate between OSX (zbrush) and Linux (maya)

files go /Users/Shared/Pixologic/ for OSX
and in can be loaded as a Maya shelf for Linux (maya)

A network projects folder should be setup ex. /your/network/share/goz_artistname/

This folder must contain ch.sh, a GoZBrush folder, GoZBrush/GoZ_Applicaiton.txt, GoZBrushFromMaya.mel, GoZBrushToMaya.mel

*public RSA ssh keys are needed for this to work, 
they can be made via ssh-keygen -t rsa, ssh-add,  
and then appended to .ssh/authorized_keys (cat id_rsa.pub >> .ssh/authorized_keys)  

*this requires a standard install of GoZ on OSX, that is setup to work with maya  

ZBrush OSX -> Maya Linux (install):
-----------------------------------
1.setup ssh pub key and add it to the linux machine  
2. create a goz_name folder on a network share  
3. move /Users/Shared/Pixologic to Pixologic_bk  
5. clone the repo to /Users/Shared  
6. symlink the repo to Pixologic  
7. copy GoZBrushToMaya.app  into the repo/GoZApps/Maya/ folder (this a standard goz *.app file I cant redistibute it)  
8. modify values in GoZ.cfg and GoZ_Config.txt to match your install  
9. copy GoZBrushFromApp.app, GoZMakeObjectPath.app, GoZ_Application.txt, GoZ_Config.txt, and the /Scripts folder from the Pixologic_bk   
10. modify GoZ_ProjectPath.txt to match your network project folder   

Note:
GoZBrushToMaya.mel is still used and must be available to the linux machine

Maya Linux -> ZBrush OSX (install):
-----------------------------------
1. setup ssh pubket and add it to the osx machine
2. add goz_linux_shelf.py to your maya shelf
3. copy GoZBrushFromMaya.mel and GoZBrushToMaya.mel to your network project (from Pixologic_bk)
4. modify the 'GoZPublicPath' to your network path (in both mel scripts)
5. create a GoZBrush folder in your network directory with GoZ_ProjectPath.txt, and GoZ_Application.txt (project path file should contain linux paths)
6. place ch.sh in the network project 
