from session import start_session
from menu import setup_menu
if __name__ == "__main__":
    level = setup_menu()
    if level is None: 
        print("Setup incomplete. Session will not start.")
        raise SystemExit(1)
    while True:
        start_session(level)
        repeat = input("Keep practicing? (y/n): ").strip().lower()
        if repeat != "y":
            print("Great job! Goodbye!")
            break

