
def setup_menu():
    print("Japanese Setup Check")
    print("1. I have Japanese installed")
    print("2. I do NOT have Japanese installed")
    print("3. Exit")

    choice = input("Select an option (1-3): ").strip()

    match choice:
        case "1":
            print("✅ Japanese is installed.")
            if not check_keyboard():
                return None
            return choose_level()
        case "2":
            print("❌ Japanese not installed.")
            show_install_instructions()
            return None
        case "3":
            print("Goodbye!")
            return None
        case _:
            print("Invalid choice.")
            return setup_menu()
        
def check_keyboard():
    print("\nCan you type Japanese with your keyboard?")
    print("1. Yes")
    print("2. No")
    choice = input("Select (1-2): ").strip()
    match choice:
        case "1":
            print("✅ Keyboard input ready.")
            return True
        case "2":
            print("❌ Keyboard input not set up.")
            show_keyboard_instructions()
            return False
        case _:
            print("Invalid choice.")
            return check_keyboard()            

def choose_level():
    print("\nWhich level would you like?")
    print("1. N4")
    print("2. N3")
    choice = input("Select (1-2): ").strip()
    match choice:
        case "1":
            print("N4 selected.\n")
            return "N4"
        case "2":
            print("N3 selected.\n")
            return "N3"
        case _:
            print("Invalid choice.\n")
            return choose_level()
        
def show_install_instructions():
    print("\nInstall Japanese language in Windows:")
    print("Settings → Time & Language → Language")
    print("Add Japanese, then restart.\n")
    
def show_keyboard_instructions():
    print("\nEnable Japanese keyboard:")
    print("Press Win + Space to switch input methods.")
    print("Use IME to type kana/kanji.\n")        





