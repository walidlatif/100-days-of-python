def _turn_right():
    for _ in range(3):
        turn_left()

def _move_left():
    move()
    turn_left()

def _move_around():
    _move_left()
    move()
    _turn_right()
    move()
    _turn_right()
    _move_left()
    
for i in range(6):
    _move_around()