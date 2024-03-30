import shutil
import sys

def check_width():
    # Get terminal size
    terminal_size = shutil.get_terminal_size()

    # Extract width from terminal size
    width = terminal_size.columns
    
    if width < 80:
        print("Make sure terminal is at least 80 chars wide!")
        sys.exit(1)
    else:
        pass