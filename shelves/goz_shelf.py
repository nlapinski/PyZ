import maya.cmds as cmds
import maya.mel as mel
import os

path = cmds.getAttr('GoZID.path')

cmds.delete(constructionHistory=True)

save='file -op "v=0" -typ "mayaAscii" -es "'+path+'";'

mel.eval(save)

open(path+'.aaa', 'w').close()

