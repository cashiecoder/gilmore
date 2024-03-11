from simple_term_menu import TerminalMenu
import sys
import os

def main():
    os.system('clear')
    print("welcome.")
    print("\nepisoede info: aisijdf;alshdfljaksj")
    options = ["entry 1info", "entry 2", "entry 3", "exit"]
    terminal_menu = TerminalMenu(options, clear_screen=False, cycle_cursor=False, menu_cursor=None)
    menu_entry_index = terminal_menu.show() 
    if options[menu_entry_index] == "exit":
        sys.exit(0)
    else:
        print(f"You have selected {options[menu_entry_index]}!")

if __name__ == "__main__":
    main()