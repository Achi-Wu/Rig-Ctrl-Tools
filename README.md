# Rig-Ctrl-Tools
This tools is use for making ctrl in rigging process 

## Description
In my rigging project I have to create a lot of Ctrl in many designs to use in a single project it makes me wonder is there anyway to help me shorten this process, though there are many of tools that can helps me to create Ctrl to use but would it be better if I create one which suit to my use and that is the reason why I create this code

## Installation
You can install this tools by copy this code to script editor in maya 
_don't forget to **change your file path**_

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
```

## Usage
What contain in this code
* Different kind of controller to use --- such as circle, square, one head arrow, two head arrow, cross arrow, lolipop, pyramid, cube
* Freeze transform command --- I recommend you to use this command when your Ctrl is in position 0,0,0 or before you move your controller to anywhere
* Make offset command --- Make an offset group to get any of input information such as translate, rotate, scale 
