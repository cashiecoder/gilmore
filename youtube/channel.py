from simple_term_menu import TerminalMenu
from .youtube import videos
import os

def remove(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def channel(main):
    options = ["Mrwhosetheboss", "GrayStillPlays", "Keegzn", "Waffloos", "MrBeast", "xNestorio", "", "Refresh", "Back"]
    terminal_menu = TerminalMenu(options, clear_screen=False, cycle_cursor=False, menu_cursor=None, skip_empty_entries=True)

    try:
        while True:
            menu_entry_index = terminal_menu.show()
            if menu_entry_index is None:
                raise KeyboardInterrupt
            selection = options[menu_entry_index] 
            if selection == "Back":
                raise KeyboardInterrupt
            if selection == "Refresh":
                remove("video.mp4")
            else:
                videos(selection, channel, main)
    except KeyboardInterrupt:
        main()
    except Exception as e:
        print(e)