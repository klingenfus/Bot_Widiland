

if positions_trigo:
    for cord in positions_trigo:
        print(cord)
        offset_x = -20
        offset_y = 10
        cord_x = cord[0] + offset_x
        cord_y = cord[1] + offset_y
        print(f' cord: {cord}, cord_x: {cord_x}, cord_y: {cord_y}')
        click(cord_x , cord_y)

pyautogui.alert('This is the message to display.') 

def do_Reconnect():
    pass
def do_login():
    pass
def do_Mission():
    pass
def do_MissionCheck():
    pass
def do_Collect():
    pass
def do_Plant():
    pass