from simple_term_menu import TerminalMenu
import os
from .episodes import episodes

def seasons(main):
    os.system('clear')
    options = ["Season 1", "Season 2", "Season 3", "Season 4", "Season 5", "Season 6", "Season 7", "A Year in the Life", "", "Back"]
    terminal_menu = TerminalMenu(options, clear_screen=False, cycle_cursor=False, menu_cursor=None, title="Gilmore Girls Seasons", skip_empty_entries=True)
    try:
        while True:
            menu_entry_index = terminal_menu.show()
            if menu_entry_index is None:
                raise KeyboardInterrupt
            selection = options[menu_entry_index] 
            if selection == "Back":
                raise KeyboardInterrupt
            else:
                if selection.endswith("1"):
                    episodes("s1", main)
                elif selection.endswith("2"):
                    episodes("s2", main)
                elif selection.endswith("3"):
                    episodes("s3", main)
                elif selection.endswith("4"):
                    episodes("s4", main)
                elif selection.endswith("5"):
                    episodes("s5", main)
                elif selection.endswith("6"):
                    episodes("s6", main)
                elif selection.endswith("7"):
                    episodes("s7", main)
                elif selection == "A Year in the Life":
                    episodes("ayitl", main)
                else:
                    return
    except KeyboardInterrupt:
        main()
    except Exception as e:
        print(e)