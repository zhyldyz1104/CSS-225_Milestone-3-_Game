def start_chapter():
    print("Chapter 4 begins. You travel with the alchemist across the vast desert.")
    print("The wind whispers secrets, and the sun burns away illusions.")


def learn_spiritual_lessons():
    choice = input("Do you want to learn spiritual lessons from the alchemist? (yes/no): ").strip().lower()
    if choice == "yes":
        print("You sit by the fire as the alchemist speaks of the Soul of the World...")
        print("You begin to understand that everything is connected.")
    else:
        print("You choose to continue without spiritual guidance.")
        print("The desert feels colder, and the silence heavier.")


def solve_riddles():
    choice = input("Do you want to solve the alchemist’s riddles? (yes/no): ").strip().lower()
    if choice == "yes":
        print("You ponder the riddles, each one revealing a deeper truth.")
        print("Wisdom flows through you like desert wind.")
        print("You reach the Pyramids. 🏜️✨ Congratulations — you have arrived at your destiny!")
        return True
    else:
        print("You struggle to understand. The path fades.")
        print("You must retry... Returning to the beginning of the game.")
        return False


def play_chapter():
    start_chapter()
    learn_spiritual_lessons()
    success = solve_riddles()
    return success
