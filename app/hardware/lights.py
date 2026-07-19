from gpiozero import LED

_lights = [LED(23), LED(5)]

def set_light(state: bool):
    for light in _lights:
        light.on() if state else light.off()

def get_light() -> bool:
    return _lights[0].is_active
