from gpiozero import LED

_light = LED(23)

def set_light(state: bool):
    if state:
        _light.on()
    else:
        _light.off()

def get_light() -> bool:
    return _light.is_active
