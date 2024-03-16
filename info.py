import sys
import math
from simple_term_menu import TerminalMenu
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

def format(s, max_line_length=50):
    words = s.split()  # Split the string into words
    lines = []
    current_line = ""

    for word in words:
        if len(current_line + word) <= max_line_length:
            current_line += word + " "
        else:
            lines.append(current_line.strip())  # Append the current line to the list of lines
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())  # Append the last line if it's not empty

    return '\n'.join(lines)

def format_seconds(seconds):
    minutes = seconds / 60
    if seconds % 60 >= 30:
        minutes = math.ceil(minutes)
    else:
        minutes = math.floor(minutes)
    return f"{minutes} Minutes"


def info(ep_num, metadata, season):
    from episodes import episodes
    episode_info = metadata[f"e{ep_num}"]["info"]
    episode_info = format(episode_info)
    length = metadata[f"e{ep_num}"]["length"]
    current_pos = metadata[f"e{ep_num}"]["current_pos"]
    print(episode_info)
    print(f"\n{format_seconds(length)}")
    print(f"Current position: {format_seconds(current_pos)}\n")
    options = ["Resume", "Restart", "", "Back"]
    terminal_menu = TerminalMenu(options, clear_screen=False, cycle_cursor=False, menu_cursor=None, skip_empty_entries=True)
    VIDEO_PATH = Path(f"./{season}e{ep_num}")
    try:
        while True:
            menu_entry_index = terminal_menu.show()
            if menu_entry_index is None:
                raise KeyboardInterrupt
            selection = options[menu_entry_index]
            if selection == "Back":
                raise KeyboardInterrupt
            elif selection == "Restart":
                player = OMXPlayer(VIDEO_PATH)
                sleep(length + 1)
                player.quit()
            elif selection == "Resume":
                player = OMXPlayer(VIDEO_PATH)
                sleep(length - current_pos + 1)
                player.quit()
    except KeyboardInterrupt:
        episodes(season)

    sys.exit()
