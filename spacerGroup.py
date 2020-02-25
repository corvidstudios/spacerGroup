import maya.cmds as cmds
#LETS GOOO

#list selection
sel = cmds.ls(sl=1, fl=1)

#query transforms of selected node. This info will be given to the spacer node in order to inherit the transforms of the selected node. 
selPos = cmds.xform(sel, query=1, worldSpace=1, translation=1)
selRot = cmds.xform(sel, query=1, worldSpace=1,rotation=1)
selScl = cmds.xform(sel, query=1, worldSpace=1, scale=1)

#clear selection so the new group about to be created won't be put into the hierarchy right away. 
cmds.select(cl=1)
#create spacer group which will be a null group. Create a name using a combination of the name of the selected node and _SPC. 
#You can change _SPC to _GRP or whatever tickles your pickle. 
spcGrp = cmds.group(empty=1, n=sel[0] + '_SPC')
#set the spacer groups transforms to the selected nodes transforms using the variable we created before. 
cmds.xform(spcGrp, ws=1, t=selPos)
cmds.xform(spcGrp, ws=1, ro=selRot)
cmds.xform(spcGrp, ws=1, s=selScl)

#parent spacer group to the current parent of the selected node and finally the selected node to the spacer group.
parSel = cmds.listRelatives(sel, p=1)
cmds.parent(spcGrp, parSel)
cmds.parent(sel, spcGrp)
#All DONE   ( ^o^)ノ＼(^_^ )