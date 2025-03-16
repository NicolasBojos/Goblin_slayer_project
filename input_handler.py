import keyboard

def check_keys():
    """Checks for user key presses (E for attack, Q for quit)."""
    if keyboard.is_pressed('q'):
        return "quit"
    if keyboard.is_pressed('e'):
        return "attack"
    return None
