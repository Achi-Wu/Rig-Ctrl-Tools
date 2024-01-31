from maya import cmds

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
    #Optional tools#

def freeze_transform(*args):
    cmds.makeIdentity( apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1 )

def make_offset_group_command(*args):
    result_group_list = cmds.ls(selection=True)
    select_ctrl = result_group_list[0]
    make_group = cmds.group(em=True)
    naming_group = cmds.rename(make_group,select_ctrl + "_Offset")
    cmds.parent(select_ctrl,naming_group)

def close_window(*args):
    cmds.deleteUI("my_window", window=True)

def main_ui(*args):
    #Check exists window    
    if cmds.window( "my_window", query=True, exists=True):
        cmds.deleteUI("my_window", window=True)

    # Make a new window
    my_window = cmds.window( "my_window" ,title="Controller Tools", iconName='Short Name', wh =(400, 500) )
    cmds.columnLayout( adjustableColumn=True )
    cmds.rowLayout(numberOfColumns=2)
    cmds.text( '    Input Ctrl Name    : ', w = 120, h = 50 )
    cmds.textField( "input_name", w = 200 )
    cmds.setParent( '..' )
    cmds.separator( w = 50, h = 20 , style='out' )

    cmds.rowLayout(numberOfColumns=2)
    cmds.button( "Circle_Command", label='Circle Ctrl', c =(build_circle_ctrl_command), w=200, h = 40 )
    cmds.button( "Square_Command", label='Square Ctrl', c =(build_square_ctrl_command), w=200, h = 40 )
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2)
    cmds.button( "One head_arrow_Command", label='One head Ctrl', c =(build_one_head_arrow_ctrl_command), w=200, h = 40 ) 
    cmds.button( "Two_heads_arrow_Command", label='Two heads arrow Ctrl', c =(build_two_heads_arrow_ctrl_command), w=200, h = 40 )
    cmds.setParent( '..' )
    cmds.rowLayout(numberOfColumns=2)
    cmds.button( "Cross_arrow_Command", label='Cross arrow Ctrl', c =(build_cross_arrow_ctrl_command), w=200, h = 40 ) 
    cmds.button( "Lolipop_Command", label='Lolipop Ctrl', c =(build_lolipop_ctrl_command), w=200, h = 40 )
    cmds.setParent( '..' ) 
    cmds.rowLayout(numberOfColumns=2)
    cmds.button( "Pyramid_Command", label='Pyramid Ctrl', c =(build_pyramid_ctrl_command), w=200, h = 40 )
    cmds.button( "Cube_Command", label='Cube Ctrl', c =(build_cube_ctrl_command), w=200, h = 40 ) 
    cmds.setParent( '..' ) 
    cmds.separator( w = 50, h = 20 , style='out' )

    cmds.button( "Freeze Transform" ,label='Freeze Transform', c = (freeze_transform) )
    cmds.button( "Make offset Group" ,label='Make offset Group', c = (make_offset_group_command) ) 
    cmds.button( "Close" ,label='Close', c = (close_window) )
    cmds.setParent( '..' )
    cmds.showWindow( my_window )