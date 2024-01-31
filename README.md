# Rig-Ctrl-Tools
This tools is use for making ctrl in rigging process 

## Installing 
You can install this tools by copy this code to script editor in maya 
>_don't forget to **change your file path**_

For maya 2018-2020
```python
import sys
Path = "where your file located"
#Example "D:/Python/Coding"

sys.path.append("Path")

import Ctrl_Tools
reload(Ctrl_Tools)

Ctrl_Tools.main_ui()
```

For maya 2021-2024
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
