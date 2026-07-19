from gpiozero import Motor

_left = Motor(forward=25, backward=24, pwm=False)
_right = Motor(forward=6, backward=22, pwm=False)
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
