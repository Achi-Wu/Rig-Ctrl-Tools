import json
import maya.cmds as cmds

# You can change your starting directory path by insert in " " below
#           
Json_file_path = r"D:"
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# You can resize your tools window and color picker size here
width = 400
color_size = (25,25)
#
#

####################################################
    #Get input command#

def get_input_name(*args):
    result_text_list = cmds.ls(selection=True)
    if result_text_list:
        result_text = result_text_list[0]
        result_name = (result_text + "_Ctrl")
        return result_name
    
    else:
        result_text = cmds.textField( "input_name", query=True, text=True)
        print(result_text)
        result_name = (result_text + "_Ctrl")
        print(result_name)
        return result_name
    
####################################################
    #Make CTRL#
            
def circle_ctrl(circle_name):
    cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), r=2 , n=circle_name )
    cmds.delete( 'makeNurbCircle1' )

def square_ctrl(square_name):
    cmds.curve(d = 1, p = [(-2, 0, 2), (-2, 0, -2), (2, 0, -2), (2, 0, 2), (-2, 0, 2)], n=square_name)
    
def one_head_arrow_ctrl(one_head_arrow_name):
    cmds.curve(d = 1, p = [( -1, 0, 3), (-1, 0, -1), (-2, 0, -1), (0, 0, -3), (2, 0, -1), (1, 0, -1), (1, 0, 3), (-1, 0, 3)], n=one_head_arrow_name)

def two_heads_arrow_ctrl(two_heads_arrow_name):
    cmds.curve(d = 1, p = [(-1, 0, -3), (-2, 0, -3), (0, 0, -5), (2, 0, -3), (1, 0, -3), (1, 0, 3)
    , (2, 0, 3), (0, 0, 5), (-2, 0, 3), (-1, 0, 3), (-1, 0, -3) ], n=two_heads_arrow_name)

def cross_arrow_ctrl(cross_arrow_name):
    cmds.curve(d = 1, p = [(-1, 0, -3), (-2, 0, -3), (0, 0, -5), (2, 0, -3), (1, 0, -3), (1, 0, -1), (3, 0, -1)
    , (3, 0, -2), (5, 0, 0), (3, 0, 2), (3, 0, 1), (1, 0, 1), (1, 0, 3), (2, 0, 3), (0, 0, 5), (-2, 0, 3), (-1, 0, 3)
    , (-1, 0, 1), (-3, 0, 1), (-3, 0, 2), (-5, 0, 0), (-3, 0, -2), (-3, 0, -1), (-1, 0, -1), (-1, 0, -3)], n=cross_arrow_name )

def lolipop_ctrl(lolipop_name):
    cmds.curve(d = 3, p = [( 0, 0, 9), (0, 0, 4), (0, 0, 1), (0, 0, 0), (-1, 0, -1), (-3, 0, -2), (-4, 0, -4)
    , (-3, 0, -7), (0, 0, -8.5), (3, 0, -7), (4, 0, -4), (3, 0, -2), (1, 0, -1), (0, 0, 0), (0, 0, 1), (0, 0, 9)], n=lolipop_name )
    lolipop_transform = lolipop_name
    cmds.setAttr(lolipop_transform + '.scalePivotZ', 9 )
    cmds.setAttr(lolipop_transform + '.rotatePivotZ', 9 )
    cmds.setAttr(lolipop_transform + '.scaleX' , 0.25)
    cmds.setAttr(lolipop_transform + '.scaleY' , 0.25)
    cmds.setAttr(lolipop_transform + '.scaleZ' , 0.25)
    cmds.setAttr(lolipop_transform + '.translateZ' , -7)
    cmds.makeIdentity( apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1 )

def pyramid_ctrl(pyramid_name):
    cmds.curve(d = 1, p = [( -1, 0, 1), (-1, 0, -1), (1, 0, -1), (1, 0, 1), (-1, 0, 1), (0, 2, 0)
    , (1, 0, -1), (-1, 0, -1), (0, 2, 0), (1, 0, 1)], n=pyramid_name)

def cube_ctrl(cube_name):
    cmds.curve(d = 1, p = [( -1, 0, 1), (-1, 2, 1), (-1, 2, -1), (-1, 0, -1), (1, 0, -1), (1, 2, -1), (1, 2, 1)
    , (1, 0, 1), (-1, 0, 1), (-1, 0, -1), (-1, 2, -1), (1, 2, -1), (1, 0, -1), (1, 0, 1), (1, 2, 1), (-1, 2, 1)], n=cube_name)

####################################################
    #Naming CTRL#
    
def build_circle_ctrl_command(*args):
    Ctrl_name = get_input_name()
    circle_ctrl(circle_name = Ctrl_name)
    
def build_square_ctrl_command(*args):
    Ctrl_name = get_input_name()
    square_ctrl(square_name = Ctrl_name)
    
def build_one_head_arrow_ctrl_command(*args):
    Ctrl_name = get_input_name()
    one_head_arrow_ctrl(one_head_arrow_name = Ctrl_name)

def build_two_heads_arrow_ctrl_command(*args):
    Ctrl_name = get_input_name()
    two_heads_arrow_ctrl(two_heads_arrow_name = Ctrl_name)

def build_cross_arrow_ctrl_command(*args):
    Ctrl_name = get_input_name()
    cross_arrow_ctrl(cross_arrow_name = Ctrl_name)

def build_lolipop_ctrl_command(*args):
    Ctrl_name = get_input_name()
    lolipop_ctrl(lolipop_name = Ctrl_name)

def build_pyramid_ctrl_command(*args):
    Ctrl_name = get_input_name()
    pyramid_ctrl(pyramid_name = Ctrl_name)

def build_cube_ctrl_command(*args):
    Ctrl_name = get_input_name()
    cube_ctrl(cube_name = Ctrl_name)

####################################################
    #Color tools#
    #Brows file

def brows_file():
    brows_result = cmds.fileDialog2(
        fileFilter="json (*.json)", 
        okCaption = "Brows", 
        fileMode = 1, 
        dialogStyle = 2,
        startingDirectory = Json_file_path )
    
    if brows_result :
        path = brows_result[0]
        create_button(path=path)
        print (path)     
    else :
        print ("no selection")

#Get json data      
def read_data(path):
    with open (path, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object

def create_button(path):
    #clear old item
    clear_item()
    
    #read data from json file
    data = read_data(path)

        #reorder json data
    reorder_data = []
    for color_name, color_info in data.items():
        order_index = color_info.get("order", 0)
        order_data = [order_index, color_name, color_info]
        reorder_data.append(order_data)

    #data ordered
    for color_name,color_info in data.items():
        order_index = color_info.get("order", 0)
        color_label = color_info.get("label", "")        
        color_index = color_info.get("maya_color_index", "")
        color_display = color_info.get("color", "")

        #for checking
        print (order_index,color_index,color_label, color_display, color_name)
        #make button
        cmds.button("{}_button".format(color_name), bgc = color_display, label = color_label,
        c = "add_color_command(color_index='{}')".format(color_index) , parent = "color_Layout")

def add_color_command(color_index):
    #Enable Overrides
    ctrl_color_list = (cmds.ls(selection = True)[0])
    get_ctrl_shape = cmds.listRelatives(ctrl_color_list, shapes = True)
    ctrl_shape = get_ctrl_shape[0]
    cmds.setAttr(ctrl_shape + '.overrideEnabled', 1)
    
    index = "{}".format(color_index)
    retype_index = float(index)
    #Add color
    cmds.setAttr(ctrl_shape + '.overrideColor', retype_index)
    print (type(index), type(retype_index))

def clear_item():
    item_list = cmds.gridLayout("color_Layout", q=True, childArray=True) or []
    for item in item_list:
        if "_button" in item:
            cmds.deleteUI(item, control = True)   
    print ()

####################################################
    #Optional tools#

def freeze_transform(*args):
    cmds.makeIdentity( apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1 )

def make_offset_group_command(*args):
    result_group_list = cmds.ls(selection=True)
    select_ctrl = result_group_list[0]
    make_group = cmds.group(em=True)
    naming_group = cmds.rename(make_group,select_ctrl + "_Offset")
    cmds.parent(select_ctrl,naming_group)

def match_transform_command(*args):
    result_match_list = cmds.ls(selection=True)
    modify_target = result_match_list[0]
    modify_source = result_match_list[1]
    cmds.MatchTranslation(modify_target,modify_source)
    cmds.MatchRotation(modify_target,modify_source)

def close_window(*args):
    cmds.deleteUI("my_window", window=True)

def main_ui(*args):
    #Check exists window    
    if cmds.window( "my_window", query=True, exists=True):
        cmds.deleteUI("my_window", window=True)

    # Make a new window
    my_window = cmds.window( "my_window" ,title="Controller Tools", iconName='Short Name', wh =(width, 500) )
    master_layout = "main_layout"
    cmds.rowColumnLayout(master_layout, numberOfColumns = 1, adjustableColumn=True )
    cmds.rowLayout("Name_layout", numberOfColumns=2, adjustableColumn=2, p = master_layout)
    cmds.text( '    Input Ctrl Name    : ', w = width/2.5, h = 50, p ="Name_layout" )
    cmds.textField( "input_name", w = width/2, p ="Name_layout" )
    cmds.separator( h = 20 , style='out', p = master_layout )
    
    
    cmds.rowLayout(numberOfColumns=2, adjustableColumn=(1,2), p = master_layout)
    cmds.button( "Circle_Command", label='Circle Ctrl', c =(build_circle_ctrl_command), h = 40 )
    cmds.button( "Square_Command", label='Square Ctrl', c =(build_square_ctrl_command), h = 40 )
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2, adjustableColumn=(1,2), p = master_layout)
    cmds.button( "One head_arrow_Command", label='One head Ctrl', c =(build_one_head_arrow_ctrl_command), h = 40 ) 
    cmds.button( "Two_heads_arrow_Command", label='Two heads arrow Ctrl', c =(build_two_heads_arrow_ctrl_command), h = 40 )
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2, adjustableColumn=(1,2), p = master_layout)
    cmds.button( "Cross_arrow_Command", label='Cross arrow Ctrl', c =(build_cross_arrow_ctrl_command), h = 40 ) 
    cmds.button( "Lolipop_Command", label='Lolipop Ctrl', c =(build_lolipop_ctrl_command), h = 40 )
    cmds.setParent( '..' ) 
    cmds.rowLayout(numberOfColumns=2, adjustableColumn=(1,2), p = master_layout)
    cmds.button( "Pyramid_Command", label='Pyramid Ctrl', c =(build_pyramid_ctrl_command), h = 40 )
    cmds.button( "Cube_Command", label='Cube Ctrl', c =(build_cube_ctrl_command), h = 40 ) 
    cmds.setParent( '..' ) 
    cmds.separator( w = 50, h = 20 , style='out', p = master_layout )

    cmds.button("brows_btn", label = "BrowsFile", c = "brows_file()", h=25, p = master_layout )
    cmds.gridLayout("color_Layout",columnsResizable= True, cellWidthHeight = color_size, p = master_layout )
    cmds.separator( w = 50, h = 20 , style='out', p = master_layout )

    cmds.button( "Freeze Transform" ,label='Freeze Transform', c = (freeze_transform), h = 40, p = master_layout )
    cmds.button( "Make offset Group" ,label='Make offset Group', c = (make_offset_group_command), h = 40, p = master_layout ) 
    cmds.button( "Match Transform" ,label='Match Transform', c = (match_transform_command), h = 40, p = master_layout ) 
    cmds.separator( w = 50, h = 20 , style='out', p = master_layout )
    cmds.button( "Close" ,label='Close', c = (close_window), h = 30, p = master_layout )
    cmds.showWindow( my_window )
