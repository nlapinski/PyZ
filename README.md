PyZ
===

Patch to modify GoZ to work over commandport and ssh to communicate between OSX (zbrush) and Linux (maya)

files go /Users/Shared/Pixologic/ for OSX
and in can be loaded as a Maya shelf for Linux (maya)

ZBrush OSX -> Maya Linux:
-----------------------------------
1. Read config, net paths
2. Write file to network
3. Check for open copy of Maya (or launch via ssh)
4. Write goz_obj_list.txt (to network)
5. Maya loads files from goz_obj_list.txt (command port) (GoZBrushToMaya.app)

Maya Linux -> ZBrush OSX:
-----------------------------------
1. Check for open Zbrush
2. Read config from goz locator object (in maya)
3. Write selected file names to goz_obj_list.txt (network path on
locator or default path)
4. Start new helper app via ssh to copy goz_obj_list.txt to Zbrush
local obj list (GoZ_ObjectList.txt)
5. Start GoZBrushFromApp.app via ssh to load objs from local GoZ data
