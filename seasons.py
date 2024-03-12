from simple_term_menu import TerminalMenu
import os
import subprocess

def shutdown_with_password(password):
    command = 'echo %s | sudo -S shutdown now > /dev/null 2>&1' % password
    subprocess.run(command, shell=True)

def seasons():
    os.system('clear')
    options = ["Season 1", "Season 2", "Season 3", "Season 4", "Season 5", "Season 6", "Season 7", "A Year in the Life", "Shutdown"]
    terminal_menu = TerminalMenu(options, clear_screen=False, cycle_cursor=False, menu_cursor=None, title="Seasons")
    
    try:
        menu_entry_index = terminal_menu.show()
        selection = options[menu_entry_index] 
        if menu_entry_index is None:
            return
        elif options[menu_entry_index] == "Shutdown":
            sudo_password = 'HiggsKitten'
            shutdown_with_password(sudo_password)
        else:
            if selection.endswith("1"):
                return "s1"
            elif selection.endswith("2"):
                return "s2"
            elif selection.endswith("3"):
                return "s3"
            elif selection.endswith("4"):
                return "s4"
            elif selection.endswith("5"):
                return "s5"
            elif selection.endswith("6"):
                return "s6"
            elif selection.endswith("7"):
                return "s7"
            elif selection == "A Year in the Life":
                return "ayitl"
            else:
                return
    except KeyboardInterrupt:
        pass

