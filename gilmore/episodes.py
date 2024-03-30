from .info import info
import json
import re
from simple_term_menu import TerminalMenu
import os

def episodes(season, main):
    from .seasons import seasons
    def get_episode_number(episode_name, metadata):
        for key, value in metadata.items():
            if value["name"] == episode_name:
                return key[1:]
        return None
    def remove_prefix(string):
        # Define a regular expression pattern to match digits followed by a colon and space
        pattern = r'\d+:\s'
        # Use re.sub() to replace the pattern with an empty string
        result = re.sub(pattern, '', string)
        return result
    
    with open(f'{os.getcwd()}/assets/gilmore/json/{season}.json') as json_file:
        metadata = json.load(json_file)
    names, list = [], []
    for _, episode_info in metadata.items():
        names.append(episode_info["name"])
    for i, name in enumerate(names, start=1):
        list.append(f'{i}: {name}')
    list.append("")
    list.append("back")

    terminal_menu = TerminalMenu(list, clear_screen=True, cycle_cursor=False, menu_cursor=None, skip_empty_entries=True, title=f"Season {season[1:]}")
    try:
        while True:
            menu_entry_index = terminal_menu.show()
            if menu_entry_index is None:
                raise KeyboardInterrupt
            selection = list[menu_entry_index]
            if selection == "back":
                raise KeyboardInterrupt
            else:
                selection = remove_prefix(selection)
                ep_num = get_episode_number(selection, metadata)
                info(ep_num, metadata, season, main)
            
    except KeyboardInterrupt:
        seasons(main)