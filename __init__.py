from gilmore.seasons import seasons
from simple_term_menu import TerminalMenu
import pickle
import subprocess
import os

class ShutdownException(Exception):
    pass

def shutdown_with_password():
    with open(f"{os.getcwd()}/assets/variables/password.pickle", "rb") as pw:
        password = pickle.load(pw)
    command = 'echo %s | sudo -S shutdown now > /dev/null 2>&1' % password
    subprocess.run(command, shell=True)

def main():
    import youtube.channel as channel
    options = ["Gilmore Girls", "YouTube", "Bluetooth", "Shutdown"]
    terminal_menu = TerminalMenu(options, clear_screen=False, cycle_cursor=False, menu_cursor=None, title="Gilmore Girls Seasons")
    try:
        while True:
            menu_entry_index = terminal_menu.show()
            if menu_entry_index is None:
                raise KeyboardInterrupt
            selection = options[menu_entry_index]
            if selection == "Shutdown":
                raise ShutdownException
            else:
                if selection == "Gilmore Girls":
                    seasons(main)
                elif selection == "YouTube":
                    channel(main)
    except KeyboardInterrupt:
        main()
    except ShutdownException:
        #shutdown_with_password()
        os._exit(0)
    except Exception as e:
        print(e)

main()