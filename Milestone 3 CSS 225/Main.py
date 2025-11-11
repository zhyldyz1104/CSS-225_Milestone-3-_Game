import chapter1, chapter2, chapter3, chapter4


def start_game():
    success = True #to control the game so we can retry in some cases

    start_new_chapter = input("Do you wanna start a game? (y/n): ").strip().lower() #asks user permission
    if start_new_chapter == "y":
        chapter1.play_chapter()
    else:
        print("Thank you! Bye!")
        return #Stops the game after getting "No"

    start_new_chapter = input("Do you want to start Chapter 2? (y/n): ").strip().lower()
    if start_new_chapter == "y":
        chapter2.play_chapter()
    else:
        print("Thank you! Bye!")
        return

    start_new_chapter = input("Do you want to start Chapter 3? (y/n): ").strip().lower()
    if start_new_chapter == "y":
        chapter3.play_chapter()
    else:
        print("Thank you! Bye!")
        return

    start_new_chapter = input("Do you want to start Chapter 4? (y/n): ").strip().lower()
    if start_new_chapter == "y":
        success = chapter4.play_chapter()
    else:
        print("Thank you! Bye!")
        return

    if not success:
        print("\nRestarting from Chapter 1...\n")   #If Chapter 4 is fail
        start_game()  #Staring the game from the very beginning


start_game()
