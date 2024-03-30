from simple_term_menu import TerminalMenu
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import pickle
import os
import psutil
import json

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def info(ep_num, metadata, season, main):
    options = ["Resume", "Restart", "", "Back"]
    terminal_menu = TerminalMenu(options, clear_screen=False, cycle_cursor=False, menu_cursor=None, skip_empty_entries=True)
    VIDEO_PATH = Path(f"{os.getcwd()}/assets/gilmore/video/{season}e{ep_num}")
    with open(f"{os.getcwd()}/assets/variables/bluetooth.pickle", "rb") as bt:
        bluetooth = pickle.load(bt)
    
    try:
        while True:
            menu_entry_index = terminal_menu.show()
            if menu_entry_index is None:
                raise KeyboardInterrupt
            selection = options[menu_entry_index]
            if selection == "Back":
                raise KeyboardInterrupt
            elif selection == "Restart":
                if bluetooth:
                    player = OMXPlayer(VIDEO_PATH, args="-o alsa")
                else:
                    player = OMXPlayer(VIDEO_PATH, args="-o hdmi")
                while True:
                    if is_process_running("omxplayer.bin"):
                        sleep(1)
                    else:
                        position = player.position()
                        if position >= length - 40:
                            metadata[f"e{ep_num}"]["current_pos"] = 0
                        else:
                            metadata[f"e{ep_num}"]["current_pos"] = position
                        with open(f'{os.getcwd()}/assets/gilmore/json/{season}.json', 'w') as json_file:
                            json.dump(metadata, json_file)
                        player.quit()
                        break
            elif selection == "Resume":
                if bluetooth:
                    player = OMXPlayer(VIDEO_PATH, args="-o alsa")
                    player.set_position(current_pos-10)
                else:
                    player = OMXPlayer(VIDEO_PATH, args="-o hdmi")
                    player.set_position(current_pos-10)
                while True:
                    if is_process_running("omxplayer.bin"):
                        sleep(1)
                    else:
                        position = player.position()
                        if position >= length - 40:
                            metadata[f"e{ep_num}"]["current_pos"] = 0
                        else:
                            metadata[f"e{ep_num}"]["current_pos"] = position
                        with open(f'{os.getcwd()}/assets/gilmore/json/{season}.json', 'w') as json_file:
                            json.dump(metadata, json_file)
                        player.quit()
                        break
    except KeyboardInterrupt:
        episodes(season, main)