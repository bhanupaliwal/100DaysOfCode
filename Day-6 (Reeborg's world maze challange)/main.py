# This challange is Reeborgs world maze challange. You can access this challange here : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json 
# In this challange you have to write a python code in editor to pass the robot through the maze and reach to the goal points. Below is the python code for this. 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()