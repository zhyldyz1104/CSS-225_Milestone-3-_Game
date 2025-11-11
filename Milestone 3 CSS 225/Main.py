import chapter1, chapter2, chapter3, chapter4, globalvariables


def start_game():
    globalvariables.username = input("Please enter your username: ")

    start_new_chapter = input(
        f"{globalvariables.username},Do you wanna start a game? (y/n): ").strip().lower()  # asks user permission
    if start_new_chapter == "y":
        chapter1.play_chapter()
    else:
        print("Thank you! Bye!")
        return  # Stops the game after getting "No"

    start_new_chapter = input(
        "Congrats on completing the chapter! Do you want to start Chapter 2? (y/n): ").strip().lower()
    if start_new_chapter == "y":
        chapter2.play_chapter()
    else:
        print("Thank you! Bye!")
        return

    start_new_chapter = input(
        "Congrats on completing the chapter! Do you want to start Chapter 3? (y/n): ").strip().lower()
    if start_new_chapter == "y":
        chapter3.play_chapter()
    else:
        print("Thank you! Bye!")
        return

    start_new_chapter = input(
        "Congrats on completing the chapter! Do you want to start Chapter 4? (y/n): ").strip().lower()
    if start_new_chapter == "y":
        globalvariables.success = chapter4.play_chapter()
    else:
        print("Thank you! Bye!")
        return

    if not globalvariables.success:
        print("\nRestarting from Chapter 1...\n")  # If Chapter 4 is fail
        start_game()  # Staring the game from the very beginning


if __name__ == "__main__":
    start_game()
