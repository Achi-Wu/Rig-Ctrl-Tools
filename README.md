# Rig-Ctrl-Tools
This tools is use for making controller in rigging process 

## Description
In my rigging project I have to create a lot of controller in many designs to use in a single project it makes me wonder is there anyway to help me shorten this process, though there are many of tools that can helps me to create controller but would it be better if I create one which suit to my use and that is the reason why I create this code

## Installation
You can install this tools by copy this code to script editor in maya 
_don't forget to **change your file path**_

For maya 2018-2020
```python
import sys
Path = "where your file located"
#Example "D:/Python/Coding"

sys.path.append(Path)

import Ctrl_Tools
reload(Ctrl_Tools)

Ctrl_Tools.main_ui()
```

For maya 2021-2024
```python
import sys
Path = "where your file located"
#Example "D:/Python/Coding"

sys.path.append(Path)
import importlib

print ("\n".join(sys.path))

import Ctrl_Tools
importlib.reload(Ctrl_Tools)

Ctrl_Tools.main_ui()
```

## Usage
What contain in this code
* Different shape of controller to use --- such as circle, square, one head arrow, two head arrow, cross arrow, lolipop, pyramid, cube
  * Controller will be create at zero position
  * You can naming your controller after the first thing you choose in outliner or viewport, your contorller will get "_Ctrl" in subfix automatically
  * You can naming your controller by input a name in a text box then choose your controller shape, your contorller will get "_Ctrl" in subfix automatically
* Freeze transform command --- To make the selected object’s current transformations be the zero position.
  > If you use this command with your controller directly make sure to use it before you translate(move) your controller to anywhere
* Make offset command --- Make an offset group for your selected object to get any of input information such as translate, rotate, scale
  * Your offset group will naming after the first thing you choose, your group will get "_Offset" in subfix automatically
  * Your group will contain only the first thing you choose
  > Recommend you to use this command before you translate(move) your controller to anywhere

## Video Guide
You can watch how to install it on your maya and usage of this code in [this video](https://youtu.be/Oewfj-9AopA)

## Contact
You can contact me on this mail - achiraya.w03@gmail.com
