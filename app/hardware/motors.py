def handle_command(command: str):
    if command == "forward":
        print("Motor: FORWARD")

    elif command == "backward":
        print("Motor: BACKWARD")

    elif command == "left":
        print("Motor: LEFT")

    elif command == "right":
        print("Motor: RIGHT")

    elif command == "stop":
        print("Motor: STOP")

    else:
        print("Unknown command:", command)
