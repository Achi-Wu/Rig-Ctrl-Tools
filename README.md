# Rig-Ctrl-Tools
This tools is use for making ctrl in rigging process 

## Installing 
You can install this tools by copy this code to script editor in maya 
>_don't forget to **change your file path**_

```python
import sys
Path = "where your file located"
#Example "D:/Python/Coding"

sys.path.append("Path")
import importlib

print ("\n".join(sys.path))

import Ctrl_Tools
importlib.reload(Ctrl_Tools)

Ctrl_Tools.main_ui()
