from simple_term_menu import TerminalMenu

def channel(main):
    options = ["Mrwhosetheboss", "GrayStillPlays", "Keegzn", "Waffloos", "MrBeast", "xNestorio", "", "Back"]
    terminal_menu = TerminalMenu(options, clear_screen=False, cycle_cursor=False, menu_cursor=None, skip_empty_entries=True)

    try:
        while True:
            menu_entry_index = terminal_menu.show()
            if menu_entry_index is None:
                raise KeyboardInterrupt
            selection = options[menu_entry_index] 
            if selection == "Back":
                raise KeyboardInterrupt
            else:
                continue
    except KeyboardInterrupt:
        main(channel)
    except Exception as e:
        print(e)