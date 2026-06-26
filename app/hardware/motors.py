from gpiozero import Motor

_left = Motor(forward=24, backward=25)
_right = Motor(forward=22, backward=6)
_left.stop()
_right.stop()

def handle_command(command: str):
    if command == "forward":
        _left.forward()
        _right.forward()
    elif command == "backward":
        _left.backward()
        _right.backward()
    elif command == "left":
        _left.backward()
        _right.forward()
    elif command == "right":
        _left.forward()
        _right.backward()
    elif command == "stop":
        _left.stop()
        _right.stop()
