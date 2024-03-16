from simple_term_menu import TerminalMenu
import os
import subprocess
import sys
from episodes import episodes

def shutdown_with_password(password):
    command = 'echo %s | sudo -S shutdown now > /dev/null 2>&1' % password
    subprocess.run(command, shell=True)

def seasons():
    os.system('clear')
    options = ["Season 1", "Season 2", "Season 3", "Season 4", "Season 5", "Season 6", "Season 7", "A Year in the Life", "Shutdown"]
    terminal_menu = TerminalMenu(options, clear_screen=False, cycle_cursor=False, menu_cursor=None, title="Seasons")
    try:
        while True:
            menu_entry_index = terminal_menu.show()
            if menu_entry_index is None:
                raise KeyboardInterrupt
            selection = options[menu_entry_index] 
            if selection == "Shutdown":
                sudo_password = 'HiggsKitten'
                shutdown_with_password(sudo_password)
            else:
                if selection.endswith("1"):
                    episodes("s1")
                elif selection.endswith("2"):
                    episodes("s2")
                elif selection.endswith("3"):
                    episodes("s3")
                elif selection.endswith("4"):
                    episodes("s4")
                elif selection.endswith("5"):
                    episodes("s5")
                elif selection.endswith("6"):
                    episodes("s6")
                elif selection.endswith("7"):
                    episodes("s7")
                elif selection == "A Year in the Life":
                    episodes("ayitl")
                else:
                    return
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        print(e)