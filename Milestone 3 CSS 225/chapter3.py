# chapter3.py

def start_chapter():
    print("Chapter 3 begins. You are summoned by the chieftain of the oasis.")
    print("The air is heavy with incense and the weight of ancient decisions.")


def summoned_by_chieftain():
    print("The chieftain speaks of omens and war, of trust and betrayal.")
    print("He asks you to interpret the signs you've seen.")


def speak_with_alchemist():
    print("You meet the alchemist — a man cloaked in silence and fire.")
    print("He speaks not in answers, but in riddles that stir your soul.")


def accept_guidance():
    print("You accept the alchemist’s guidance.")
    print("He teaches you that true transformation begins within.")
    print("He hands you a flask of oil and says: 'Protect this as you would your heart.'")


def delay_progress():
    print("You hesitate. Doubt clouds your path.")
    print("The alchemist nods, understanding. 'Even the desert waits for those who listen.'")


def proceed_to_desert():
    print("You set out into the desert, the sun blazing and your heart steady.")
    print("The journey has begun — not just across the sands, but into yourself.")


def end_chapter():
    print("Chapter 3 ends. The wind carries your name across the dunes.")


def play_chapter():
    start_chapter()
    summoned_by_chieftain()
    speak_with_alchemist()

    choice = input("Do you accept the alchemist’s guidance? (yes/no): ").strip().lower()
    if choice == "yes":
        accept_guidance()
        proceed_to_desert()
    else:
        delay_progress()

    end_chapter()
