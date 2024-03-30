import pickle
import os
import getpass

def password():
    password1 = getpass.getpass("Enter your root password: ")
    password2 = getpass.getpass("Enter it again to confirm: ")
    if password1 == password2:
        pass
    else:
        print("Passwords do not match, please try again.")
        password()
    with open(f"{os.getcwd()}/assets/variables/password.pickle", "wb") as pw:
        pickle.dump(password1, pw)
    print("Password saved successfully!")

print("This utility saves your password to a variable so Python can shutdown the DragonPi from the main menu when selected. The password does NOT leave your device.")

password()